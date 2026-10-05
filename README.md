# HyperWithdrawAssets
توسط این اسکریپت پایتون دارایی های روی هایپرلیکوید ابندا به USDC تبدیل شده و به ولتی که مشخص کردید منتقل میگردد

حتماً. ساختار را دقیقاً به همین ترتیب می‌چینیم: نیازمندی‌ها → نصب ابزارها برای هر سیستم‌عامل → ساخت متغیرهای محیطی محلی → اجرای کد نهایی.

راهنمای اجرای کد Hyperliquid

1. نیازمندی‌ها

برای اجرای کد به موارد زیر نیاز دارید:

* Python نسخه 3.10 یا بالاتر
* دسترسی به Terminal / PowerShell / Command Prompt
* اینترنت
* فایل کد نهایی پروژه
* کلید خصوصی کیف پولی که موجودی UENA در آن قرار دارد
* آدرس کیف پول مقصد در شبکه Arbitrum برای دریافت USDC

کلید خصوصی فقط روی سیستم خودتان استفاده می‌شود و نباید در کد، GitHub، Telegram، Discord یا هیچ سرویس دیگری قرار گیرد.

⸻

2. نصب Python

macOS

ابتدا Terminal را باز کنید و بررسی کنید Python نصب است:

python3 --version

اگر Python نصب نبود، در صورتی که Homebrew دارید:

brew install python

سپس دوباره بررسی کنید:

python3 --version

باید نسخه‌ای مانند زیر نمایش داده شود:

Python 3.12.x

⸻

Linux

برای Ubuntu / Debian:

sudo apt update
sudo apt install python3 python3-pip python3-venv

سپس:

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

وارد پوشه‌ای شوید که فایل کد نهایی در آن قرار دارد.

در macOS و Linux:

python3 -m venv .venv
source .venv/bin/activate

در Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1

اگر PowerShell اجازه اجرای اسکریپت را نداد:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

سپس دوباره:

.venv\Scripts\Activate.ps1

اکنون کتابخانه‌های موردنیاز را نصب کنید:

pip install hyperliquid-python-sdk eth-account

اگر پروژه دارای فایل requirements.txt است، به‌جای دستور بالا از این استفاده کنید:

pip install -r requirements.txt

⸻

4. ساخت متغیرهای محلی

کد برای امنیت، اطلاعات حساس را مستقیماً داخل فایل Python قرار نمی‌دهد.

دو متغیر محلی باید ساخته شوند:

HL_SECRET_KEY
HL_DEST

HL_SECRET_KEY:

کلید خصوصی کیف پولی که UENA در آن قرار دارد.

HL_DEST:

آدرس کیف پولی که می‌خواهید USDC به آن در شبکه Arbitrum ارسال شود.

⸻

macOS

Terminal را باز کنید و اجرا کنید:

export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

برای بررسی:

echo $HL_DEST

اگر آدرس کیف پول نمایش داده شد، متغیر ساخته شده است.

برای اطمینان، کلید خصوصی را با echo نمایش ندهید.

⸻

Linux

در Terminal:

export HL_SECRET_KEY="0xYOUR_PRIVATE_KEY"
export HL_DEST="0xYOUR_ARBITRUM_ADDRESS"

برای بررسی:

echo $HL_DEST

⸻

Windows PowerShell

در PowerShell:

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

فرض کنید نام فایل نهایی:

withdraw_uena.py

باشد.

macOS

پس از فعال کردن محیط مجازی:

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

در صورت موفقیت فروش UENA، در خروجی باید وضعیت سفارش به شکل filled نمایش داده شود.

نمونه:

UENA order FILLED

پس از آن موجودی USDC بررسی می‌شود و در صورت وجود موجودی کافی، برداشت به آدرس HL_DEST انجام می‌شود.

در صورت موفقیت برداشت، باید چیزی مشابه این مشاهده شود:

Withdrawal response:
{'status': 'ok', ...}

⸻

7. پایان کار

پس از اتمام اجرا، برای حذف متغیرهای محلی از همان Terminal استفاده کنید.

macOS / Linux

unset HL_SECRET_KEY
unset HL_DEST

Windows PowerShell

Remove-Item Env:HL_SECRET_KEY
Remove-Item Env:HL_DEST

Windows CMD

set HL_SECRET_KEY=
set HL_DEST=

اگر Terminal بسته شود، متغیرهایی که با روش بالا ساخته شده‌اند نیز از محیط همان Session حذف می‌شوند.

این نسخه دقیقاً برای قرار دادن در GitHub مناسب است و مراحل را بدون ورود به جزئیات اضافی از نصب تا اجرای کد دنبال می‌کند.
