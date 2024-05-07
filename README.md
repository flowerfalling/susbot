# SusBot

My WeChat bot

## Prepare environment

1. Virtual environment
   1. Build a virtual environment by `python -m venv .venv`
   2. Activate the virtual environment by `.\.venv\Scripts\activate`
   3. Install dependencies by `pip install -r requirements.txt`
2. ComWeChat-Client
   1. Download ComWeChat-Client-v0.0.8 [here](https://github.com/JustUndertaker/ComWeChatBotClient/releases/tag/v0.0.8)
   2. Modify the `ComWeChat-Client-v0.0.8\.env`:
      - enable_http_api = false
      - websocekt_type = "Backward"
   3. Launch WeChat-3.7.0.30 (download [here](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.7.0.30/WeChatSetup-3.7.0.30.exe))
   4. Run `ComWeChat-Client-v0.0.8\ComWeChat-Client-v0.0.8.exe`

## How to start

Run the bot using `nb run`

Or you can run the `bot.py`

## Documentation

See [Docs](https://nonebot.dev/)
