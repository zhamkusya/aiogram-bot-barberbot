from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧭 Онлайн-запись"),
        ],
        [
            KeyboardButton(text="☎️ Контакты"),
            KeyboardButton(text="❓ Задать вопрос")
        ],

[
            KeyboardButton(text="🖼 Галерея"),
            KeyboardButton(text="💰 Цены на услуги")
        ],
        [ KeyboardButton(text="⚙️ Настройки")]],
    resize_keyboard=True
)
onlzap = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💇‍♂️ Мужские стрижки"),
        ],
        [
            KeyboardButton(text="⬅️ Главное меню")
        ]],
    resize_keyboard=True
)
questkn = ReplyKeyboardMarkup(
    keyboard=[[


            KeyboardButton(text="⬅️ Главное меню")
        ]],
    resize_keyboard=True
)
barbers= ReplyKeyboardMarkup(
    keyboard=[[


            KeyboardButton(text="⬅️ Главное меню")
        ]],
    resize_keyboard=True
)

