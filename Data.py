# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna Bot-Bot MAS GACOR
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk Mengecek Kecepatan Bot
 ├ /id - Cek Id Akun Kamu
 └ /uptime - Untuk Melihat Status Bot 

👨‍💻 Asupan Gratis: </b><a href='https://t.me/konsumasgacor'>@konsumasgacor</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b><i><u>Apa Sebenarnya Bot ini?</u></i>

@{} adalah <u>bot penyedia asupan gratis</u> untuk para Gacolers se-Indonesia.\n

<i><u>Apa itu Gacolers?</u></i>

adalah sebutan untuk member dan penikmat Jasa Mas Gacor se-Indonesia. <i>Kontak Dukungan:</i>

 • Admin: @{}
 • Channel Backup: <a href='https://t.me/videogacorindo'>@videogacorindo</a>
 • Bot Support Centre: <a href='https://t.me/mngcbot'>@BotKendala</a>\n

👨‍💻 Asupan Gratis: </b><a href='https://t.me/konsumasgacor'>@konsumasgacor</a>
<i>-©Mas Gacor Indonesia</i>.\n\n
"""
