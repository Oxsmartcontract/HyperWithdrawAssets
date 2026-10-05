# Hyperliquid Any Asset Sell & Withdraw

راهنمای اجرای کد برای فروش **هر دارایی Spot** در Hyperliquid، تبدیل آن به **USDC** و انتقال USDC به یک آدرس در شبکه **Arbitrum**.

---

## 1. نیازمندی‌ها

- Python 3.10+
- اتصال اینترنت
- Terminal در macOS/Linux یا PowerShell در Windows
- Private Key کیف پولی که دارایی در آن قرار دارد

> ⚠️ Private Key را داخل کد، GitHub، Telegram یا Discord قرار ندهید.

---

## 2. نصب Python

### macOS

```bash
python3 --version
```

در صورت نیاز:

```bash
brew install python
```

### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Windows

```powershell
python --version
```

---

## 3. نصب کتابخانه‌ها

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

در صورت خطای دسترسی:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

سپس:

```bash
pip install hyperliquid-python-sdk eth-account
```

---

## 4. تنظیم Private Key

کد Private Key را از متغیر محیطی `HL_SECRET_KEY` دریافت می‌کند.

### macOS / Linux

```bash
export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
```

### Windows PowerShell

```powershell
$env:HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
```

> ⚠️ Private Key را با `echo` نمایش ندهید.

---

## 5. اجرای برنامه

### برای اجرای برنامه باید فایل hyperliquid_sell_withdraw.py را قبلا روی سیسستم خودتان دانلود کرده باشید(بهترین کار این است بعد از دانلود فایل آنرا به یک پوشه انتقال دهید و از داخل همان پوشه یک پنجره کامند برای اجرا آن باز نمائید) 
```text
hyperliquid_sell_withdraw.py
```

باشد.

### macOS / Linux

```bash
python3 hyperliquid_sell_withdraw.py
```

### Windows

```powershell
python hyperliquid_sell_withdraw.py
```

برنامه هنگام اجرا از شما می‌پرسد:

```text
نام ارز را وارد کنید:
مقدار ارز برای فروش را وارد کنید:
آدرس مقصد Arbitrum را وارد کنید:
```

سپس مارکت `COIN/USDC` را پیدا کرده، دارایی را می‌فروشد و در صورت **Fill شدن سفارش**، USDC را به آدرس مقصد در Arbitrum برداشت می‌کند.

قبل از فروش باید تأیید کنید:

```text
YES
```

و قبل از برداشت:

```text
WITHDRAW
```

---

## 6. حذف Private Key

پس از پایان کار:

### macOS / Linux

```bash
unset HL_SECRET_KEY
```

### Windows PowerShell

```powershell
Remove-Item Env:HL_SECRET_KEY
```

---

## 7. امنیت

هرگز:

- ❌ Private Key را داخل فایل Python قرار ندهید.
- ❌ آن را در GitHub Commit نکنید.
- ❌ آن را داخل `README.md` قرار ندهید.
- ❌ آن را برای دیگران ارسال نکنید.

در صورت استفاده از Git، این موارد را در `.gitignore` قرار دهید:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

---

## اجرای سریع

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install hyperliquid-python-sdk eth-account
export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
python3 hyperliquid_sell_withdraw.py
unset HL_SECRET_KEY
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install hyperliquid-python-sdk eth-account
$env:HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
python hyperliquid_sell_withdraw.py
Remove-Item Env:HL_SECRET_KEY
```
