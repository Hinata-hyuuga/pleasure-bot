version = "v0.1.0"
import asyncio
from pyrogram import Client, filters
from typing import Union
from time import time

boot = 0


#TOKENS
from config import (
    API_HASH, API_ID, BOT_TOKEN, 
    PORT, LogsChannel, CONTACT_URL
)


Bot = Client(
    name="pleasurebot",
    api_hash=API_HASH,
    api_id=API_ID,
    plugins={"root": "plugins"},
    bot_token=BOT_TOKEN
)

async def initiate_bot():
    global boot
    await Bot.start()
    boot = time()
    try:
        self = Bot.me
        await Bot.send_web_page(
            LogsChannel, 
            text=f"❒ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ\n├• ɴᴀᴍᴇ : {self.first_name}\n├• ɪᴅ : [`{self.id}`]\n├• ᴜsᴇʀɴᴀᴍᴇ : @{self.username}\n└• ᴠᴇʀꜱɪᴏɴ : {version}\n",
            url="https://telegra.ph/file/0e09b52a4fe6b71b2e104.jpg", 
            show_above_text=True, 
            prefer_large_media=True,
        )
    except: pass



def callback_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )
    
def cmd(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@{Bot.me.username}"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@{Bot.me.username}"])
  return filters.command(res, prefixes=["/", "$", "!", "."])

import traceback
import sys
async def HandleException(chat=None, note=None, message=None, reason=False, edit_message=False, buttons=None):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    tb_info = traceback.extract_tb(exc_traceback)
    filename, line_num, func_name, code = tb_info[-1]
    
    error_message = f"<pre language='ERROR'>ꜰᴜɴᴄᴛɪᴏɴ: {func_name}\n\nꜰɪʟᴇ: {filename}\n\nʟɪɴᴇ: {line_num}</pre><blockquote>ᴄᴏᴅᴇ: **{code}**</blockquote><blockquote>ᴇʀʀᴏʀ: **{exc_value}**</blockquote>"
    if note: error_message += f"<pre language='NOTE'>{note}</pre>"
    if chat: error_message += f"\n<pre language='EFFECTIVE CHAT'>{chat}</pre>"
    try:
        if message:
            error_message += "» <i>informed user ✔️</i>"
            Nreason = "<blockquote>POWERED NY @ANIMEROBOTS 🩷</blockquote>"
            if reason: 
                error_message += "\n» <i>informed exception error ✔️</i>"
                Nreason = f"\n<pre language='ERROR'>{exc_value}</pre>"
            if edit_message: await message.edit(f"<pre language='AN ERROR OCCURRED!'>Please try again. If the problem persists, contact bot owner & report.</pre>\n<b>📨 {CONTACT_URL}</b>\n\n{Nreason}", disable_web_page_preview=True, reply_markup=buttons)
            else: await message.reply(f"<pre language='AN ERROR OCCURRED!'>Please try again. If the problem persists, contact bot owner & report.</pre>\n<b>📨 {CONTACT_URL}</b>\n\n{Nreason}", disable_web_page_preview=True, reply_markup=buttons)
    except: pass
    await Bot.send_message(
        LogsChannel, 
        text=error_message, 
        reply_markup=buttons,
    )


# webapp.py
from aiohttp import web
from aiohttp_jinja2 import render_template_async, setup
from jinja2 import FileSystemLoader

async def web_ping(request): 
    return await render_template_async('pages/ping.html', request, {})
#async def web_cmd(request): 
#    return await render_template_async('pages/cmdpage.html', request, {})
    
class WebApp:
    def __init__(self):
        self.web_app = web.Application()
        self.setup_routes()

    def setup_routes(self):
        self.web_app.add_routes([
            web.get('/', web_ping),
            #web.get('/cmdpage', web_cmd),
            web.static('/static', 'web/assets')
        ])
        setup(self.web_app, loader=FileSystemLoader('web'), enable_async=True)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.create_task(web._run_app(self.web_app, host="0.0.0.0", port=int(PORT)))












import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "AnimeRobots.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("aiohttp.access").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)