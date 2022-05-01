from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
    ]

    START = """
"""

    HELP = """
✨ **ʜᴇʟᴘᴇʀ ʙᴏʀ** ✨

/about - ᴛᴇɴᴛᴀɴɢ ʀᴏʙᴏᴛ
/help - ᴄᴀʀᴀ ᴄᴀʀᴀ ʙᴜᴀᴛ sᴇsɪ
/start - ᴍᴇᴍᴜʟᴀɪ ʙᴏᴛ
/generate - ᴍᴇᴍʙᴜᴀᴛ sᴛʀɪɴɢ sᴇsɪ
/cancel - ᴍᴇᴍʙᴀᴛᴀʟ ᴋᴀɴ ᴘʀᴏsᴇs
/restart - ᴍᴇɴɢᴜʟᴀɴɢ sᴇsɪ
"""

    ABOUT = """
**ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ** 
╭━━━━━━━━━━━━━━━━━
┞◈ ɴᴀᴍᴇ ᴍᴇ : ᴛᴏᴊɪ ʀᴏʙᴏᴛ 
┟◈ ᴏᴡɴᴇʀ : [sᴋʏᴋʏ](https://t.me/skytixsz)
┟◈ ғʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](https://docs.pyrogram.org)
┟◈ ʟᴀɴɢᴜᴀɢᴇ : [Python](https://www.python.org)
╰━━━━━━━━━━━━━━━━━
    """
