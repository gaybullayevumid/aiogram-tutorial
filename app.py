import asyncio
import types

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = "6667385868:AAEgEGKSM_YoHyGBAd2Xf4JwBt8tRwen6U8"

# bot and Dispatcher settings
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# create router
router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum, EchoBotga xush kelibsiz")

@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Botdan foydalanish uchun biror nima yozing!")

@router.message(Command("about"))
async def about_handler(message: types.Message):
    await message.answer("Bu bot shunchaki test uchun yaratildi!")

@router.message()
async def echo(message: Message):
    await message.answer(message.text)

dp.include_router(router)

async def main():
    print("Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())