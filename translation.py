from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    TECH_VJ_START_TEXT = """
<b>ʜᴇʟʟᴏ {} 👋

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀᴅᴠᴀɴᴄᴇ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ

ɢɪᴠᴇ ᴍᴇ ᴀɴʏ ʟɪɴᴋ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪɴᴛᴏ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ

ᴛʜɪs ʙᴏᴛ ɪs ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href="https://t.me/ANKAN_Contact_BOT">ᴀɴᴋᴀɴ</a></b>
"""

    TECH_VJ_HELP_TEXT = """
<b>⚡ ғᴇᴀᴛᴜʀᴇs :-

❍ ᴜᴘʟᴏᴀᴅ ʏᴛ-ᴅʟᴘ sᴜᴘᴘᴏʀᴛᴇᴅ ʟɪɴᴋs ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ.

❍ ᴜᴘʟᴏᴀᴅ ʜᴛᴛᴘ/ʜᴛᴛᴘs ᴀs ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ.

❍ ᴜᴘʟᴏᴀᴅ ᴢᴇᴇ5, sᴏɴʏ.ʟɪᴠᴇ, ᴠᴏᴏᴛ ᴀɴᴅ ᴍᴜᴄʜ ᴍᴏʀᴇ.

❍ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ.

❍ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ʙʏ /broadcast ᴄᴏᴍᴍᴀɴᴅ

☺️ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ :-

➻ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɢᴏᴏɢʟᴇ ᴅʀɪᴠᴇ | ʏᴛᴅʟ | ᴅɪʀᴇᴄᴛ ʟɪɴᴋs.

➻ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴏᴘᴛɪᴏɴ.

➻ ᴛʜᴇɴ ʙᴇ ʀᴇʟᴀxᴇᴅ ʏᴏᴜʀ ғɪʟᴇ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ sᴏᴏɴ..</b> 
"""

    TECH_VJ_ABOUT_TEXT = """
<b>♻️ ᴍʏ ɴᴀᴍᴇ : ᴜнᴅ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ

🗿 ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/UHD_Bots">ᴜʜᴅ ʙᴏᴛs™</a>

🌐 Sᴇʀᴠᴇʀ : <a href="https://heroku.com/">ʜᴇʀᴏᴋᴜ</a>

📑 ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.java.com">ᴊᴀᴠᴀ</a>

📚 Lɪʙʀᴀʀʏ : <a href="https://docs.pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ</a>

🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href="https://t.me/ANKAN_Contact_BOT">ᴀɴᴋᴀɴ</a></b>

"""

    
    TECH_VJ_START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🗿 ᴜʜᴅ ɴᴇᴛᴡᴏʀᴋ', url='https://t.me/UHD_NETWORK')
        ], [
            InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+fx7ngJZDyFlhNTM1'),
            InlineKeyboardButton('❤️ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/UHD_Bots')
        ], [
            InlineKeyboardButton('❓ ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🤖 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('💝 ᴅᴏɴᴀᴛᴇ ᴜs 💖', url='https://graph.org/Donate-06-01')
        ]]
    )
    TECH_VJ_HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔥 ᴜʜᴅ ɴᴇᴛᴡᴏʀᴋ', url='https://t.me/UHD_NETWORK')
        ], [
            InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+fx7ngJZDyFlhNTM1'),
            InlineKeyboardButton('❤️ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/UHD_Bots')
        ], [
            InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('💖 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('❌ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    TECH_VJ_ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔥 ᴜʜᴅ ɴᴇᴛᴡᴏʀᴋ', url='https://t.me/UHD_NETWORK')
        ], [
            InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/+fx7ngJZDyFlhNTM1'),
            InlineKeyboardButton('❤️ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/UHD_Bots')
        ], [
            InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('💖 ᴀʙᴏᴜᴛ', callback_data='help')
        ], [
            InlineKeyboardButton('❌ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    
    TECH_VJ_ERROR = "<b>ᴇʀʀᴏʀ : {}</b>"

    
    TECH_VJ_FORMAT_SELECTION = "<b>ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ғᴏʀᴍᴀᴛ: ғɪʟᴇ ꜱɪᴢᴇ ᴍɪɢʜᴛ ʙᴇ ᴀᴘᴘʀᴏxɪᴍᴀᴛᴇ \nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ, ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ʙᴇғᴏʀᴇ ᴏʀ ǫᴜɪᴄᴋʟʏ ᴀғᴛᴇʀ ᴛᴀᴘᴘɪɴɢ ᴏɴ ᴀɴʏ ᴏғ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ.\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ /delthumbnail ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴀᴜᴛᴏ-ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ.</b>"
    TECH_VJ_SET_CUSTOM_USERNAME_PASSWORD = """<b>Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴇᴍɪᴜᴍ ᴠɪᴅᴇᴏꜱ, ᴘʀᴏᴠɪᴅᴇ ɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ғᴏʀᴍᴀᴛ:\nURL | ғɪʟᴇɴᴀᴍᴇ | ᴜꜱᴇʀɴᴀᴍᴇ | ᴘᴀꜱꜱᴡᴏʀᴅ</b>"""
    TECH_VJ_DOWNLOAD_START = "<b>📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...</b>"
    TECH_VJ_UPLOAD_START = "<b>📤 ᴜᴘʟᴏᴀᴅɪɴɢ...</b>"
    TECH_VJ_RCHD_TG_API_LIMIT = "<b>ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ.\nᴅᴇᴛᴇᴄᴛᴇᴅ ғɪʟᴇ ꜱɪᴢᴇ: {}\nꜱᴏʀʀʏ. ʙᴜᴛ, ɪ ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇꜱ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 𝟸GB ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ API ʟɪᴍɪᴛᴀᴛɪᴏɴꜱ.</b>"
    TECH_VJ_AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>ᴛʜᴀɴᴋꜱ ғᴏʀ ᴜꜱɪɴɢ ᴍᴇ\n\nJᴏɪɴ : @UHD_Bots</b>"
    TECH_VJ_AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "<b>ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ.\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ.\n\n@UHD_Bots</b>"
    TECH_VJ_SAVED_CUSTOM_THUMB_NAIL = "<b>ᴄᴜꜱᴛᴏᴍ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ. Tʜɪꜱ ɪᴍᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴛʜᴇ ᴠɪᴅᴇᴏ / ғɪʟᴇ.</b>"
    TECH_VJ_DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ ꜱᴜᴄᴄᴇꜱғᴜʟʟʏ.</b>"
    TECH_VJ_CUSTOM_CAPTION_UL_FILE = "<b>{}</b>"
    TECH_VJ_NO_VOID_FORMAT_FOUND = "<b>ᴇʀʀᴏʀ...\nTᴇᴄʜ VJ ꜱᴀɪᴅ: {}</b>"
    TECH_VJ_REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>ʀᴇᴘʟʏ /generatecustomthumbnail ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ, ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙᴀɪʟ</b>"
    TECH_VJ_ERR_ONLY_TWO_MEDIA_IN_ALBUM = """<b>ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ ꜱʜᴏᴜʟᴅ ᴄᴏɴᴛᴀɪɴ ᴏɴʟʏ ᴛᴡᴏ ᴘʜᴏᴛᴏꜱ. ᴘʟᴇᴀꜱᴇ ʀᴇ-ꜱᴇɴᴅ ᴛʜᴇ ᴍᴇᴅɪᴀ ᴀʟʙᴜᴍ, ᴀɴᴅ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ, ᴏʀ ꜱᴇɴᴅ ᴏɴʟʏ ᴛᴡᴏ ᴘʜᴏᴛᴏꜱ ɪɴ ᴀɴ ᴀʟʙᴜᴍ.\nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ /ʀᴇɴᴀᴍᴇ ᴄᴏᴍᴍᴀɴᴅ ᴀғᴛᴇʀ ʀᴇᴄᴇɪᴠɪɴɢ ғɪʟᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ɪᴛ ᴡɪᴛʜ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴜᴘᴘᴏʀᴛ.</b>"""
    TECH_VJ_CANCEL_STR = "<b>ᴘʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟʟᴇᴅ</b>"
    TECH_VJ_ZIP_UPLOADED_STR = "<b>ᴜᴘʟᴏᴀᴅᴇᴅ {} ғɪʟᴇꜱ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ</b>"
    TECH_VJ_SLOW_URL_DECED = "<b>Gᴏꜱʜ ᴛʜᴀᴛ ꜱᴇᴇᴍꜱ ᴛᴏ ʙᴇ ᴀ ᴠᴇʀʏ ꜱʟᴏᴡ URL. Sɪɴᴄᴇ ʏᴏᴜ ᴡᴇʀᴇ ꜱᴄʀᴇᴡɪɴɢ ᴍʏ ʜᴏᴍᴇ, I ᴀᴍ ɪɴ ɴᴏ ᴍᴏᴏᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜɪꜱ ғɪʟᴇ. ᴍᴇ ᴀ ғᴀꜱᴛ URL ꜱᴏ ᴛʜᴀᴛ I ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴛᴏ Tᴇʟᴇɢʀᴀᴍ, ᴡɪᴛʜᴏᴜᴛ ᴍᴇ ꜱʟᴏᴡɪɴɢ ᴅᴏᴡɴ ғᴏʀ ᴏᴛʜᴇʀ ᴜꜱᴇʀꜱ.</b>"

    TECH_VJ_ERROR_YTDLP = "<b>ᴘʟᴇᴀꜱᴇ ʀᴇᴘᴏʀᴛ ᴛʜɪꜱ ɪꜱꜱᴜᴇ ᴏɴ https://yt-dl.org/bug . ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴛʜᴇ ʟᴀᴛᴇꜱᴛ ᴠᴇʀꜱɪᴏɴ; ꜱᴇᴇ  https://yt-dl.org/update ᴏɴ ʜᴏᴡ ᴛᴏ ᴜᴘᴅᴀᴛᴇ. ʙᴇ ꜱᴜʀᴇ ᴛᴏ ᴄᴀʟʟ ʏᴏᴜᴛᴜʙᴇ-ᴅʟ ᴡɪᴛʜ ᴛʜᴇ --ᴠᴇʀʙᴏꜱᴇ ғʟᴀɢ ᴀɴᴅ ɪɴᴄʟᴜᴅᴇ ɪᴛꜱ ᴄᴏᴍᴘʟᴇᴛᴇ ᴏᴜᴛᴘᴜᴛ.</b>"
