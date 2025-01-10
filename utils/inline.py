from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def force_sub(Channel, ReffLink):
    button = [
        [InlineKeyboardButton(text="🔷 JOIN", url=Channel)],
    ]
    if ReffLink:
        button.append([InlineKeyboardButton(text="Restart Using InviteLink", url=ReffLink)])
    return InlineKeyboardMarkup(button)


def start_pannel():
    return None