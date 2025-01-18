from aiogram import Bot
from aiogram.types import Message


async def get_user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    matn = (f"{message.from_user.mention_html('USER')} INFO:\n\n"
            f"Ism-Familiya: {message.from_user.full_name}\n"
            f"ID: {message.from_user.id}\n"
            )
    if user.bio: matn += f"Tarjimai holi: {user.bio}"
    if message.from_user.username: matn += f"Username: @{message.from_user.username}"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption=matn, parse_mode="HTMl")
    else:
        await message.answer(matn, parse_mode="HTML")



async def start_answer(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Salom, {message.from_user.mention_html(f"{message.from_user.first_name}")}", parse_mode='HTML')

async def help_answer(message: Message, bot: Bot):
    matn = f"""
        <b>Bot buyruqlari:</b>
        
        /start - Botni ishga tushurish
        /help - Yordam!
    """

    await bot.send_message(message.from_user.id, matn, parse_mode='HTML')