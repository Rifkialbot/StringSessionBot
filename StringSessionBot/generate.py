from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "sɪʟᴀʜ ᴋᴀɴ ᴘɪʟɪʜ sᴛʀɪɴɢ ʏᴀɴɢ ɪɴɢɪɴ ᴀɴᴅᴀ ɢᴜɴᴀᴋᴀɴ\n𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎 : ʙᴏᴛ ᴍᴜsɪᴄ\n𝑻𝒆𝒍𝒆𝒕𝒉𝒐𝒏 : ᴜsᴇʀʙᴏᴛ ᴀᴛᴀᴜ ʙᴏᴛ ᴍᴀɴᴀɢᴇʀ"
buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram1"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ᴠ1 [ɴᴇᴡ]", callback_data="pyrogram"),
    ],
    # [
    #     InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot"),
    #     InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot"),
    # ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"ᴍᴇᴍᴜʟᴀɪ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴇsɪ : {ty}")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'ᴛᴏʟᴏᴍɢ ʙᴇʀɪᴋᴀɴ `API_ID` ᴀɴᴅᴀ', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('ᴀᴘɪ ɪᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ, ᴍᴏʜᴏɴ ᴍᴇᴍᴜʟᴀɪ ᴋᴇᴍʙᴀʟɪ sᴇsɪ ʙᴀʀᴜ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'ᴛᴏʟᴏɴɢ ʙᴇʀɪᴋᴀɴ `API_HASH` ᴀɴᴅᴀ', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "sᴇᴋᴀʀᴀɴɢ ᴛᴏʟᴏɴɢ ʙᴇʀɪᴋᴀɴ `ɴᴏᴍᴇʀ ᴛᴇʟᴇᴘᴏɴ` ʟᴀʟᴜ ᴛᴜɴɢɢᴜ sᴀᴍᴘᴀɪ ᴄᴏᴅᴇ ᴅᴀᴛᴀɴɢ. \nExample : `+628....`'"
    else:
        t = "sᴇᴋᴀʀᴀɴɢ ᴛᴏʟᴏɴɢ ʙᴇʀɪᴋᴀɴ `BOT_TOKEN` \nCᴏɴᴛᴏʜ : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ᴏᴛᴘ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
        await client.start(bot_token=phone_number)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply('`API_ID` ᴅᴀɴ `API_HASH` ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʙᴜᴀᴛ ʟᴀʜ sᴇsɪ ʙᴀʀᴜ ᴀɴᴅᴀ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply('`PHONE_NUMBER` ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʙᴜᴀᴛ ʟᴀʜ sᴇsɪ ʙᴀʀᴜ ᴀɴᴅᴀ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "sɪʟᴀʜᴋᴀɴ ᴘᴇʀɪᴋsᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴅᴀʀɪ ᴀᴋᴜɴ ʀᴇsᴍᴜ ᴛᴇʟᴇɢʀᴀᴍ. ᴊɪᴋᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴀɴᴅᴀ `12345`, **ᴛᴏʟᴏɴɢ ᴛᴀᴍʙᴀʜ ᴋᴀɴ sᴘᴀsɪ sᴘᴇʀᴛɪ** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('ʙᴀᴛᴀs ᴡᴀᴋғᴜ ᴛᴇʀᴄᴀᴘᴀɪ ʜᴀɴʏᴀ 10 ᴍᴇɴɪᴛ. ᴛᴏʟᴏɴɢ ʙᴜᴀᴛ sᴇsɪ ʙᴀʀᴜ ᴋᴇᴍʙᴀʟɪ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply('OTP is invalid. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply('OTP is expired. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, 'ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪғ ᴋᴀɴ ᴠᴇʀɪғɪᴋᴀsɪ ᴅᴜᴀ ʟᴀɴɢᴋᴀʜ, sᴜʟᴀʜ ᴋᴀɴ ᴋᴜʀɪᴍ ᴘᴀssᴡᴏʀʟᴅ ᴀɴᴅᴀ.', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('ʙᴀᴛᴀs ᴡᴀᴋᴛᴜ ᴛᴇʀᴄᴀᴘᴀɪ ʜᴀɴʏᴀ 5 ᴍᴇɴɪᴛ. ʙᴜᴀᴛ ʟᴀʜ sᴇsɪ ʙᴀʀᴜ ᴀɴᴅᴀ.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply('ᴘᴀssᴡᴏʟᴅ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ʙᴜᴀᴛ ʟᴀʜ sᴇsɪ ʙᴀʀᴜ ᴀɴᴅᴀ ᴋᴇᴍʙᴀʟɪ.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} STRING SESSION** \n\n`{string_session}` \n\nᴅɪ ʙᴜᴀᴛ ᴏʟᴇʜ : @Skytrixszbot"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "ʙᴇʀʜᴀsɪʟ ᴍᴇᴍʙᴜᴀᴛ {} sᴛʀɪɴɢ sᴇssɪᴏɴ. \n\nᴄᴇᴋ ᴅɪ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ᴍɪʟɪᴋ ᴀɴᴅᴀ! \n\nᴅɪ ʙᴜᴀᴛ ᴏʟᴇʜ : @skytrixsz".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("ᴘʀᴏsᴇs ᴅɪ ʙᴀᴛᴀʟ ᴋᴀɴ!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("ᴍᴇɴɢᴜʟᴀɴɢ sᴇsɪ ʙᴏᴛ!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Cancelled the generation process!", quote=True)
        return True
    else:
        return False
