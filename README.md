Hyperliquid UENA Sell & Withdraw

راهنمای اجرای کد برای فروش UENA در Hyperliquid و انتقال موجودی USDC به یک آدرس در شبکه Arbitrum.

⸻

1. نیازمندی‌ها

برای اجرای کد به موارد زیر نیاز دارید:

* Python 3.10 یا بالاتر
* دسترسی به Terminal در macOS/Linux یا PowerShell / CMD در Windows
* اتصال اینترنت
* فایل کد نهایی پروژه
* Private Key کیف پولی که UENA در آن قرار دارد
* آدرس کیف پول مقصد در شبکه Arbitrum

⚠️ امنیت: کلید خصوصی فقط روی سیستم خودتان استفاده می‌شود. آن را داخل کد، GitHub، Telegram، Discord یا هیچ سرویس دیگری قرار ندهید.

⸻

2. نصب Python

macOS

ابتدا Terminal را باز کنید و بررسی کنید Python نصب است:

python3 --version

اگر Python نصب نبود و Homebrew روی سیستم شما نصب است:

brew install python

سپس دوباره بررسی کنید:

python3 --version

باید نسخه‌ای مشابه زیر نمایش داده شود:

Python 3.12.x

⸻

Linux

برای Ubuntu / Debian:

sudo apt update
sudo apt install python3 python3-pip python3-venv

سپس نسخه Python را بررسی کنید:

python3 --version

و:

pip3 --version

⸻

Windows

PowerShell را باز کنید و اجرا کنید:

python --version

اگر Python نصب نیست، Python 3 را نصب کنید و سپس دوباره دستور بالا را اجرا کنید.

همچنین بررسی کنید:

pip --version

⸻

3. نصب کتابخانه‌های موردنیاز

ابتدا وارد پوشه‌ای شوید که فایل کد نهایی در آن قرار دارد.

macOS / Linux

یک محیط مجازی Python ایجاد کنید:

python3 -m venv .venv

سپس آن را فعال کنید:

source .venv/bin/activate

Windows PowerShell

python -m venv .venv

سپس:

.venv\Scripts\Activate.ps1

اگر PowerShell اجازه اجرای اسکریپت را نداد:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

سپس دوباره:

.venv\Scripts\Activate.ps1

⸻

نصب کتابخانه‌ها

اگر پروژه دارای فایل requirements.txt است:

pip install -r requirements.txt

در غیر این صورت:

pip install hyperliquid-python-sdk eth-account

⸻

4. ساخت متغیرهای محیطی محلی

برای امنیت، اطلاعات حساس مستقیماً داخل فایل Python قرار نمی‌گیرند.

دو متغیر محیطی موردنیاز هستند:

HL_SECRET_KEY
HL_DEST

HL_SECRET_KEY

Private Key کیف پولی که UENA در آن قرار دارد.

HL_DEST

آدرس کیف پول مقصد که USDC باید به آن در شبکه Arbitrum ارسال شود.

⚠️ هیچ‌وقت Private Key را در GitHub یا فایل عمومی پروژه قرار ندهید.

⸻

macOS

در Terminal اجرا کنید:

export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

برای بررسی اینکه آدرس مقصد تنظیم شده است:

echo $HL_DEST

برای امنیت، Private Key را با echo نمایش ندهید.

⸻

Linux

در Terminal اجرا کنید:

export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

برای بررسی:

echo $HL_DEST

⸻

Windows PowerShell

در PowerShell اجرا کنید:

$env:HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
$env:HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

برای بررسی:

echo $env:HL_DEST

⸻

Windows Command Prompt

اگر از CMD استفاده می‌کنید:

set HL_SECRET_KEY=0xYOUR_PRIVATE_KEY
set HL_DEST=0xYOUR_ARBITRUM_ADDRESS

برای بررسی:

echo %HL_DEST%

⸻

5. اجرای کد نهایی

فرض کنید نام فایل Python پروژه:

withdraw_uena.py

باشد.

macOS

python3 withdraw_uena.py

⸻

Linux

python3 withdraw_uena.py

⸻

Windows PowerShell

python withdraw_uena.py

⸻

Windows CMD

python withdraw_uena.py

⸻

6. بررسی نتیجه

در صورت موفقیت فروش UENA، باید در خروجی وضعیت سفارش مشابه زیر مشاهده شود:

UENA order FILLED

سپس کد موجودی USDC را بررسی کرده و در صورت وجود موجودی کافی، برداشت را به آدرس HL_DEST انجام می‌دهد.

در صورت موفقیت برداشت، خروجی مشابه زیر نمایش داده می‌شود:

Withdrawal response:
{'status': 'ok', ...}

⸻

7. حذف متغیرهای محیطی

پس از پایان کار، برای حذف متغیرهای محیطی از همان Terminal یا PowerShell استفاده کنید.

macOS / Linux

unset HL_SECRET_KEY
unset HL_DEST

Windows PowerShell

Remove-Item Env:HL_SECRET_KEY
Remove-Item Env:HL_DEST

Windows CMD

set HL_SECRET_KEY=
set HL_DEST=

⸻

8. امنیت

هرگز موارد زیر را انجام ندهید:

* ❌ قرار دادن Private Key داخل فایل Python
* ❌ قرار دادن Private Key داخل GitHub
* ❌ قرار دادن Private Key داخل README.md
* ❌ ارسال Private Key در Telegram یا Discord
* ❌ ارسال Private Key برای افراد دیگر
* ❌ قرار دادن Private Key در فایل .env که قرار است Commit شود

اگر از Git استفاده می‌کنید، بهتر است موارد زیر را داخل .gitignore قرار دهید:

.env
.venv/
__pycache__/
*.pyc

⸻

خلاصه اجرای سریع

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"
python3 withdraw_uena.py
unset HL_SECRET_KEY
unset HL_DEST

Windows PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
$env:HL_DEST="0xYOUR_ARBITRUM_ADDRESS"
python withdraw_uena.py
Remove-Item Env:HL_SECRET_KEY
Remove-Item Env:HL_DEST
