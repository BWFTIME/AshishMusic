import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AshishX import app  

photo = [
    "https://i.postimg.cc/g0j4wY4H/20231127-214133.png",
    "https://telegra.ph/file/0c87c715c94cee2322a4b.jpg",
    "https://i.postimg.cc/gjb3zdns/20231127-215452.png",
    "https://telegra.ph/file/7a6b51ee0077724254ca7.jpg",
    "https://telegra.ph/file/23c520bf48a83347923ce.jpg",
    "https://i.postimg.cc/g0j4wY4H/20231127-214133.png",
    "https://telegra.ph/file/23c520bf48a83347923ce.jpg",
    "https://telegra.ph/file/75b30a4bd492c1afcbdbf.jpg",
    "https://telegra.ph/file/f609b2ba20991f445513c.jpg",
    "https://telegra.ph/file/87d82843ed13a098b165f.jpg",
    "https://telegra.ph/file/029e639384809f9e5a07a.jpg",
    "https://telegra.ph/file/90bf00fb0506f65611361.jpg",
    "https://telegra.ph/file/567f7eacd5dec10afff2c.jpg",
    "https://telegra.ph/file/211980c02b0ffe343f370.jpg",
    "https://i.postimg.cc/gjb3zdns/20231127-215452.png",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ🧸 {message.from_user.mention} 🌲𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ💐**\n\n"
                f"**[🥀✰𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ♦️ꭙ** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✨❏ 𝐂ʜᴀᴛ 𝐔.𝐍 🍃∘°** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🍷 𝐔ʀ 𝐈d 💖** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🍧𝐔ʀ 𝐔.𝐍🍒** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💒𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🕊️🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"⛩️ 𝐖ᴇʟᴄᴏᴍᴇ 𝐁σт 𝐀ᴅᴅ ⛩️", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
