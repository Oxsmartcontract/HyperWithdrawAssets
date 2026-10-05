# Hyperliquid UENA Sell & Withdraw

راهنمای اجرای کد برای فروش **UENA** در Hyperliquid و انتقال موجودی **USDC** به یک آدرس در شبکه Arbitrum.

---

## 1. نیازمندی‌ها

برای اجرای کد به موارد زیر نیاز دارید:

- **Python 3.10 یا بالاتر**
- دسترسی به **Terminal** در macOS/Linux یا **PowerShell / CMD** در Windows
- اتصال اینترنت
- فایل کد نهایی پروژه
- **Private Key** کیف پولی که UENA در آن قرار دارد
- آدرس کیف پول مقصد در شبکه **Arbitrum**

> ⚠️ **امنیت:** کلید خصوصی فقط روی سیستم خودتان استفاده می‌شود. آن را داخل کد، GitHub، Telegram، Discord یا هیچ سرویس دیگری قرار ندهید.

---

# 2. نصب Python

## macOS

ابتدا Terminal را باز کنید و بررسی کنید Python نصب است:

```bash
python3 --version
```

اگر Python نصب نبود و Homebrew روی سیستم شما نصب است:

```bash
brew install python
```

سپس دوباره بررسی کنید:

```bash
python3 --version
```

باید نسخه‌ای مشابه زیر نمایش داده شود:

```text
Python 3.12.x
```

---

## Linux

برای Ubuntu / Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

سپس:

```bash
python3 --version
```

و:

```bash
pip3 --version
```

---

## Windows

PowerShell را باز کنید:

```powershell
python --version
```

اگر Python نصب نیست، Python 3 را نصب کنید و سپس دوباره دستور بالا را اجرا کنید.

همچنین بررسی کنید:

```powershell
pip --version
```

---

# 3. نصب کتابخانه‌های موردنیاز

ابتدا وارد پوشه‌ای شوید که فایل کد نهایی در آن قرار دارد.

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

اگر PowerShell اجازه اجرای اسکریپت را نداد:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

سپس:

```powershell
.venv\Scripts\Activate.ps1
```

## نصب کتابخانه‌ها

اگر پروژه دارای `requirements.txt` است:

```bash
pip install -r requirements.txt
```

در غیر این صورت:

```bash
pip install hyperliquid-python-sdk eth-account
```

---

# 4. ساخت متغیرهای محیطی محلی

برای امنیت، اطلاعات حساس مستقیماً داخل فایل Python قرار نمی‌گیرند.

دو متغیر موردنیاز:

```text
HL_SECRET_KEY
HL_DEST
```

### `HL_SECRET_KEY`

Private Key کیف پولی که UENA در آن قرار دارد.

### `HL_DEST`

آدرس کیف پول مقصد که USDC باید به آن در شبکه **Arbitrum** ارسال شود.

> ⚠️ هیچ‌وقت Private Key را در GitHub یا فایل عمومی پروژه قرار ندهید.

---

## macOS

```bash
export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"
```

برای بررسی:

```bash
echo $HL_DEST
```

> برای امنیت، Private Key را با `echo` نمایش ندهید.

---

## Linux

```bash
export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"
```

برای بررسی:

```bash
echo $HL_DEST
```

---

## Windows PowerShell

```powershell
$env:HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
$env:HL_DEST="0xYOUR_ARBITRUM_ADDRESS"
```

برای بررسی:

```powershell
echo $env:HL_DEST
```

---

## Windows Command Prompt

```cmd
set HL_SECRET_KEY=0xYOUR_PRIVATE_KEY
set HL_DEST=0xYOUR_ARBITRUM_ADDRESS
```

برای بررسی:

```cmd
echo %HL_DEST%
```

---

# 5. اجرای کد نهایی

فرض کنید نام فایل Python پروژه:

```text
withdraw_uena.py
```

باشد.

## macOS

```bash
python3 withdraw_uena.py
```

## Linux

```bash
python3 withdraw_uena.py
```

## Windows PowerShell

```powershell
python withdraw_uena.py
```

## Windows CMD

```cmd
python withdraw_uena.py
```

---

# 6. بررسی نتیجه

در صورت موفقیت فروش UENA، باید در خروجی وضعیت سفارش مشابه زیر مشاهده شود:

```text
UENA order FILLED
```

سپس کد موجودی USDC را بررسی کرده و در صورت وجود موجودی کافی، برداشت را به آدرس `HL_DEST` انجام می‌دهد.

در صورت موفقیت برداشت:

```text
Withdrawal response:
{'status': 'ok', ...}
```

---

# 7. حذف متغیرهای محیطی

پس از پایان کار:

## macOS / Linux

```bash
unset HL_SECRET_KEY
unset HL_DEST
```

## Windows PowerShell

```powershell
Remove-Item Env:HL_SECRET_KEY
Remove-Item Env:HL_DEST
```

## Windows CMD

```cmd
set HL_SECRET_KEY=
set HL_DEST=
```

---

# 8. امنیت

**هرگز موارد زیر را انجام ندهید:**

- ❌ قرار دادن Private Key داخل فایل Python
- ❌ قرار دادن Private Key داخل GitHub
- ❌ قرار دادن Private Key داخل `README.md`
- ❌ ارسال Private Key در Telegram یا Discord
- ❌ ارسال Private Key برای افراد دیگر
- ❌ قرار دادن Private Key در فایل `.env` که قرار است Commit شود

اگر از Git استفاده می‌کنید، موارد زیر را داخل `.gitignore` قرار دهید:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## خلاصه اجرای سریع

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

python3 withdraw_uena.py

unset HL_SECRET_KEY
unset HL_DEST
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

$env:HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
$env:HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

python withdraw_uena.py

Remove-Item Env:HL_SECRET_KEY
Remove-Item Env:HL_DEST
```
