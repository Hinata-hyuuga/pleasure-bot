from pyrogram import filters, Client
from pyrogram.types import Message

from clients import Bot, cmd, HandleException
from utils.helper import is_participant, ON_START_LINK_CMD, log_pvt_start
from utils.inline import force_sub, start_pannel
from utils.db.users import add_user, present_user
from config import FORCE_SUB
from utils.vars import MD_FORCE_SUB, FORCESUB_TXT, MD_START_URL, START_TXT


@Client.on_message(cmd('start') & filters.private)
async def start_cmd(app: Bot, message: Message): # type: ignore
    User = message.from_user
    IsNew = False
    fstring = "None"
    try:
        if len(message.command) != 1:
            fstring = message.text.split(" ", 1)[1]
        if not await is_participant(app, user_id=User.id, chat_id=FORCE_SUB):
            rereff = f"https://t.me/{app.me.username}?start={fstring}" if fstring != "None" else None
            return await message.reply_web_page(FORCESUB_TXT, url=MD_FORCE_SUB, reply_markup=force_sub(rereff), show_above_text=True)
        
        IsNewUser, subscription = present_user(User.id)
        if not IsNewUser:
            isnew = add_user(user_id=User.id)
        
        strtlink = await ON_START_LINK_CMD(fstring, app, message, isnew)

        try: await log_pvt_start(app=app, User=User, IsNew=isnew, refff=strtlink)
        except: pass

        if fstring == "None":
            await message.reply_web_page(url=MD_START_URL, text=START_TXT, reply_markup=start_pannel(), show_above_text=True)
    except Exception:
        await HandleException(chat=User.id, note="start cmd", message=message)

    await message.reply(text=f"hello {User.mention}, im alive")
