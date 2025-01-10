from pyrogram.enums import ChatMemberStatus
from config import LogsChannel


def paste_to_text(name, content):
    data = str(content)
    file_path = f"utils/cache/{name}.txt"
    with open(file_path, "w+", encoding="utf8") as file:
        file.write(data)
    return file_path


async def is_participant(app, user_id, chat_id):
    try:
        user = await app.get_chat_member(chat_id, user_id)
        if user.status in {ChatMemberStatus.BANNED, ChatMemberStatus.LEFT}:
            return False
        return True
    except:
        return False

async def log_pvt_start(app, User, IsNew, refff):
    New = "🆕 NEW" if IsNew is True else "♻️ RESTART"
    Link = f"https://t.me/{User.username}" if User.username else f"<a href='tg://openmessage?user_id={User.id}'>User Profile Link</a>"
    await app.send_message(
        LogsChannel,
        f"""<pre>({New}) USER JUST STARTED BOT</pre>
👤: <b>{User.mention}</b>
🔗: <i>{Link}</i>
🆔: [`{User.id}`]    #id{User.id}
▶️: {refff}""",
        disable_web_page_preview=False,
        show_above_text=False,
    )

    

async def ON_START_LINK_CMD(string, app, message):
    User = message.from_user
    if not string: return None
        
    if string in ["default"]:
        #example
        pass
    else: return None
        



def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "min", "hr", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


def convert_bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return "??"
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])
