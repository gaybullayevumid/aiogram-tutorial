from aiogram import Bot, Dispatcher, types
from asyncio import run

dp = Dispatcher()

async def echo(message: types.Message, bot:Bot):
    await message.copy_to(chat_id=message.chat.id)
    # await message.reply(message.text)


async def start():
    dp.message.register(echo)
    bot = Bot("6667385868:AAEgEGKSM_YoHyGBAd2Xf4JwBt8tRwen6U8")
    await dp.start_polling(bot)

run(start())