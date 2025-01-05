import asyncio
from clients import WebApp, initiate_bot, LOGGER
from config import HOST

async def init():
    await initiate_bot()
    if HOST == "VPS":
        LOGGER("APP").info("BOT STARTED ✅")
    else:
        web_app = WebApp()
        web_app.run()
        LOGGER("APP").info("BOT+WEB STARTED ✅")
        

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_forever()