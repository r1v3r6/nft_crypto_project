import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

API_TOKEN = "7946679475:AAH-r7EYEZ3eZrRldaD8Makf9r2Anm_mfck"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    print("Получена команда /start")  # Отладочный 
    print(message)  # <== добавьте это
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎰 Играть",
                    web_app=WebAppInfo(url="https://example.com")  # замени на свою ссылку
                )
            ]
        ]
    )
    await message.answer(
        "Привет! Добро пожаловать в NFT Казино 🃏\n\nНажми кнопку ниже, чтобы начать игру.",
        reply_markup=keyboard
    )

async def main():
    try:
        print("Бот запускается...")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(main())

