import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

# Токен бота (замініть на ваш)
TOKEN = "7702003437:AAFO3pnQVJsvZkXAy_KlKMXLM1T2Dpy7ylA"

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Створення екземпляра бота
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Використовуємо In-Memory Storage для збереження стану вибору мови
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()
dp.include_router(router)

# Словник для підтримки двох мов
LANGUAGES = {
    "uk": {
        "start": "Привіт! Я твій бот для запису на послугу. Обери мову:",
        "choose": "Оберіть мову 🌍",
        "book": "📅 Записатися",
        "my_bookings": "📝 Мої записи",
        "cancel": "❌ Скасувати запис",
        "select_time": "Виберіть дату і час для запису:",
        "your_bookings": "Ось ваші записи:"
    },
    "en": {
        "start": "Hello! I'm your appointment bot. Choose a language:",
        "choose": "Choose a language 🌍",
        "book": "📅 Book an appointment",
        "my_bookings": "📝 My bookings",
        "cancel": "❌ Cancel booking",
        "select_time": "Select a date and time for your appointment:",
        "your_bookings": "Here are your bookings:"
    }
}

# Клавіатура для вибору мови
language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_uk")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")]
    ]
)

# Збереження вибору мови
user_languages = {}

# Хендлер команди /start
@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(LANGUAGES["uk"]["start"], reply_markup=language_keyboard)

# Обробник вибору мови
@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery, state: FSMContext):
    lang = callback.data.split("_")[1]  # "uk" або "en"
    user_languages[callback.from_user.id] = lang

    # Створюємо головну клавіатуру
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=LANGUAGES[lang]["book"])],
            [KeyboardButton(text=LANGUAGES[lang]["my_bookings"])]
        ],
        resize_keyboard=True
    )

    await callback.message.answer(LANGUAGES[lang]["choose"], reply_markup=keyboard)
    await callback.answer()

# Кнопка для запису
@router.message(lambda message: message.text in [LANGUAGES["uk"]["book"], LANGUAGES["en"]["book"]])
async def cmd_book(message: types.Message):
    lang = user_languages.get(message.from_user.id, "uk")  # За замовчуванням українська
    await message.answer(LANGUAGES[lang]["select_time"])

# Кнопка для перегляду своїх записів
@router.message(lambda message: message.text in [LANGUAGES["uk"]["my_bookings"], LANGUAGES["en"]["my_bookings"]])
async def cmd_my_bookings(message: types.Message):
    lang = user_languages.get(message.from_user.id, "uk")
    await message.answer(LANGUAGES[lang]["your_bookings"])

# Хендлер для скасування запису
@router.message(lambda message: message.text.startswith(LANGUAGES["uk"]["cancel"]) or message.text.startswith(LANGUAGES["en"]["cancel"]))
async def cmd_cancel(message: types.Message):
    lang = user_languages.get(message.from_user.id, "uk")
    booking_id = message.text.split(' ')[-1]  # Припускаємо, що ID запису після пробілу
    await message.answer(f"{LANGUAGES[lang]['cancel']} {booking_id}!")

# Функція для запуску бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
