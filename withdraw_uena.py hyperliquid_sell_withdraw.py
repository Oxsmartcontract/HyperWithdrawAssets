import os
import time
from math import floor, log10

import eth_account
from hyperliquid.exchange import Exchange
from hyperliquid.info import Info
from hyperliquid.utils import constants


SLIPPAGE = 0.05
FEE_BUFFER = 1.01


def valid_px(px, sig=5):
    if px == 0:
        raise ValueError("قیمت نمی‌تواند صفر باشد")

    return round(
        px,
        sig - int(floor(log10(abs(px)))) - 1
    )


def get_user_input():
    print("=" * 60)
    print("Hyperliquid Spot → USDC → Arbitrum")
    print("=" * 60)

    coin = input("نام ارز را وارد کنید (مثلاً UENA): ").strip().upper()

    if not coin:
        raise SystemExit("نام ارز وارد نشده است.")

    size_input = input(
        f"مقدار {coin} برای فروش را وارد کنید: "
    ).strip()

    try:
        size = float(size_input)
    except ValueError:
        raise SystemExit("مقدار واردشده معتبر نیست.")

    if size <= 0:
        raise SystemExit("مقدار فروش باید بزرگ‌تر از صفر باشد.")

    dest = input(
        "آدرس مقصد Arbitrum را وارد کنید: "
    ).strip()

    if not dest:
        raise SystemExit("آدرس مقصد وارد نشده است.")

    if not dest.startswith("0x") or len(dest) != 42:
        raise SystemExit(
            "آدرس مقصد معتبر به نظر نمی‌رسد. "
            "آدرس باید یک آدرس EVM با فرمت 0x... باشد."
        )

    return coin, size, dest


def find_market(info, coin):
    meta = info.spot_meta()

    for market in meta["universe"]:
        base_token = meta["tokens"][market["tokens"][0]]
        quote_token = meta["tokens"][market["tokens"][1]]

        base = base_token["name"]
        quote = quote_token["name"]

        if base == coin and quote == "USDC":
            return market["name"]

    return None


def get_free_balance(state, coin):
    for bal in state["balances"]:
        if bal["coin"] == coin:
            total = float(bal["total"])
            hold = float(bal["hold"])
            return total - hold

    return 0.0


def get_free_usdc(state):
    for bal in state["balances"]:
        if bal["coin"] == "USDC":
            total = float(bal["total"])
            hold = float(bal["hold"])
            return total - hold

    return 0.0


def main():

    # ============================================================
    # 1. دریافت اطلاعات از کاربر
    # ============================================================

    coin, size, dest = get_user_input()

    # ============================================================
    # 2. دریافت Private Key
    # ============================================================

    secret = os.environ.get("HL_SECRET_KEY")

    if not secret:
        raise SystemExit(
            "متغیر محیطی HL_SECRET_KEY پیدا نشد."
        )

    wallet = eth_account.Account.from_key(secret)

    print()
    print(f"Wallet: {wallet.address}")
    print(f"Coin: {coin}")
    print(f"Sell size: {size}")
    print(f"Destination: {dest}")
    print()

    # ============================================================
    # 3. اتصال به Hyperliquid
    # ============================================================

    info = Info(
        constants.MAINNET_API_URL,
        skip_ws=True
    )

    exchange = Exchange(
        wallet,
        constants.MAINNET_API_URL,
        account_address=wallet.address
    )

    # ============================================================
    # 4. پیدا کردن مارکت COIN/USDC
    # ============================================================

    print(f"Searching for {coin}/USDC market...")

    pair = find_market(info, coin)

    if pair is None:
        raise SystemExit(
            f"مارکت {coin}/USDC در Hyperliquid Spot پیدا نشد."
        )

    print(f"Market: {pair}")

    # ============================================================
    # 5. بررسی موجودی ارز
    # ============================================================

    print()
    print(f"Checking {coin} balance...")

    state = info.spot_user_state(wallet.address)

    free_coin = get_free_balance(state, coin)

    print(f"Free {coin}: {free_coin}")

    if free_coin <= 0:
        raise SystemExit(
            f"هیچ موجودی آزاد از {coin} پیدا نشد."
        )

    if size > free_coin:
        raise SystemExit(
            f"مقدار درخواستی بیشتر از موجودی آزاد است.\n"
            f"Requested: {size} {coin}\n"
            f"Available: {free_coin} {coin}"
        )

    # ============================================================
    # 6. گرفتن قیمت فعلی
    # ============================================================

    print()
    print("Getting current market price...")

    mids = info.all_mids()

    if pair not in mids:
        raise SystemExit(
            f"قیمت {pair} در allMids پیدا نشد."
        )

    mid = float(mids[pair])

    print(f"Mid price: {mid}")

    # ============================================================
    # 7. محاسبه قیمت فروش
    # ============================================================

    raw_limit_px = mid * (1 - SLIPPAGE)
    limit_px = valid_px(raw_limit_px)

    print(f"Raw limit price: {raw_limit_px}")
    print(f"Valid limit price: {limit_px}")

    estimated_usdc = size * limit_px

    print()
    print(f"Estimated USDC: {estimated_usdc}")

    # ============================================================
    # 8. تأیید نهایی
    # ============================================================

    print()
    print("=" * 60)
    print("ORDER SUMMARY")
    print("=" * 60)
    print(f"Market       : {pair}")
    print(f"Sell         : {size} {coin}")
    print(f"Limit price  : {limit_px} USDC")
    print(f"Est. receive : {estimated_usdc:.6f} USDC")
    print(f"Destination  : {dest}")
    print("=" * 60)

    confirm = input(
        "\nبرای ارسال سفارش عبارت YES را وارد کنید: "
    ).strip()

    if confirm != "YES":
        raise SystemExit("عملیات توسط کاربر لغو شد.")

    # ============================================================
    # 9. فروش ارز
    # ============================================================

    print()
    print(f"Selling {size} {coin}...")

    sell = exchange.order(
        pair,
        False,
        size,
        limit_px,
        {
            "limit": {
                "tif": "Ioc"
            }
        }
    )

    print()
    print("Order response:")
    print(sell)

    if sell.get("status") != "ok":
        raise SystemExit(
            "سفارش توسط API رد شد."
        )

    # ============================================================
    # 10. بررسی نتیجه سفارش
    # ============================================================

    statuses = (
        sell
        .get("response", {})
        .get("data", {})
        .get("statuses", [])
    )

    print()
    print("Order statuses:")
    print(statuses)

    filled = False

    for status in statuses:

        if "filled" in status:
            filled = True

            print()
            print("ORDER FILLED")

            if "filled" in status:
                filled_data = status["filled"]

                print(
                    f"Filled size: "
                    f"{filled_data.get('totalSz', 'Unknown')}"
                )

                print(
                    f"Average price: "
                    f"{filled_data.get('avgPx', 'Unknown')}"
                )

            break

        if "error" in status:
            print()
            print("ORDER ERROR:")
            print(status["error"])

    if not filled:
        raise SystemExit(
            "سفارش پر نشد؛ بنابراین برداشت USDC انجام نمی‌شود."
        )

    # ============================================================
    # 11. صبر برای به‌روزرسانی موجودی
    # ============================================================

    print()
    print("Waiting for USDC balance update...")

    time.sleep(3)

    # ============================================================
    # 12. گرفتن موجودی جدید
    # ============================================================

    state = info.spot_user_state(wallet.address)

    print()
    print("Updated spot balances:")

    for bal in state["balances"]:
        print(
            f"{bal['coin']}: "
            f"total={bal['total']} "
            f"hold={bal['hold']}"
        )

    # ============================================================
    # 13. پیدا کردن USDC آزاد
    # ============================================================

    usdc = get_free_usdc(state)

    print()
    print(f"Free USDC: {usdc}")

    if usdc <= 0:
        raise SystemExit(
            "هیچ USDC آزادی برای برداشت پیدا نشد."
        )

    # ============================================================
    # 14. محاسبه مبلغ برداشت
    # ============================================================

    amount = round(usdc - FEE_BUFFER, 2)

    print(f"Withdraw amount: {amount} USDC")

    if amount <= 0:
        raise SystemExit(
            "USDC بعد از کسر buffer یک USDC کافی نیست."
        )

    # ============================================================
    # 15. تأیید برداشت
    # ============================================================

    print()
    print("=" * 60)
    print("WITHDRAWAL SUMMARY")
    print("=" * 60)
    print(f"USDC available : {usdc}")
    print(f"Withdraw       : {amount} USDC")
    print(f"Destination    : {dest}")
    print("Network        : Arbitrum")
    print("=" * 60)

    confirm = input(
        "\nبرای انجام برداشت عبارت WITHDRAW را وارد کنید: "
    ).strip()

    if confirm != "WITHDRAW":
        raise SystemExit(
            "برداشت توسط کاربر لغو شد."
        )

    # ============================================================
    # 16. برداشت USDC به Arbitrum
    # ============================================================

    print()
    print(f"Withdrawing {amount} USDC...")
    print(f"Destination: {dest}")

    wd = exchange.withdraw_from_bridge(
        amount,
        dest
    )

    print()
    print("Withdrawal response:")
    print(wd)

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    main()
