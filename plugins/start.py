from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!

You Can too Clone me :-
https://github.com/ProThinkerGang/Anonymous-Bot
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("❤️ Support Group ❤️",
                          url="t.me/FutureCodes")],
    [InlineKeyboardButton("🧑‍💻 Dev 🧑‍💻",
                          url="t.me/Anonymous_machinee")]])


@Client.on_message(filters.command('start') & (filters.private | filters.group))
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
