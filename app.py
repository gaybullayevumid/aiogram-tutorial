from aiogram import Bot, Dispatcher, types
from asyncio import run

import functions
from functions import *
from aiogram.types import BotCommand
from aiogram.filters import Command

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(5323321097, "Bot ishga tushdi! ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(5323321097, "Bot ishdan toxtadi! ❌")


# async def echo(message: types.Message, bot:Bot):
#     await message.copy_to(chat_id=message.chat.id)
#     # await message.reply(message.text)


async def start():
    dp.startup.register(startup_answer)

    dp.message.register(functions.start_answer, Command("start"))
    dp.message.register(functions.help_answer, Command("help"))
    dp.message.register(functions.get_user_info)

    dp.shutdown.register(shutdown_answer)

    bot = Bot("6667385868:AAEgEGKSM_YoHyGBAd2Xf4JwBt8tRwen6U8")
    await bot.set_my_commands([
        BotCommand(command='/start', description='Botni ishga tushirish.'),
        BotCommand(command='/help', description='Yordam.')
    ])
    await dp.start_polling(bot, polling_timeout=1)

run(start())