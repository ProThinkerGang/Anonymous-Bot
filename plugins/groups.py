from pyrogram import (
    Client,
    filters
    )


@Client.on_message(filters.group)
async def leave(client, message):
    await message.copy(message.chat.id,caption="")
