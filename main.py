# import asyncio
# from aiogram import Router, Bot, types, Dispatcher
# from aiogram.types import ParseMode
import asyncio
from idlelib.undo import Command

# async def salom_ber():
#     print("Salom")
#     await asyncio.sleep(2)
#     print("Hayr")
#
#
# asyncio.run(salom_ber())


# async def function_1():
#     print("Funksiya 1 boshlanyapti")
#     await asyncio.sleep(5)
#     print("Funksiya 1 tugadi")
#
#
# async def function_2():
#     print("Funksiya 2 boshlanyapti")
#     await asyncio.sleep(3)
#     print("Funksiya 2 tugadi")
#
# async def main():
#     task1 = asyncio.create_task(function_1())
#     task2 = asyncio.create_task(function_2())
#
#     await task1
#     await task2
#
# asyncio.run(main())

# import asyncio
# from aiogram import Router, Bot, Dispatcher
# from aiogram.types import Message
# from aiogram.filters import Command
#
#
# API_TOKEN = "6667385868:AAEgEGKSM_YoHyGBAd2Xf4JwBt8tRwen6U8"
#
# # bot and dispatcher settings
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # create router
# router = Router()
#
# @router.message()
# async def echo_bot(message: Message):
#     await message.answer(message.text)
#
# @router.message(Command("start"))
# async def start_handler(message: Message):
#     await message.answer("Hi! Welcome to echo bot")
#
# # add router to dispatcher
# dp.include_router(router)
#
# async def main():
#     print("Bot ishga tushdi")
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())