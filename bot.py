from config import TOKEN
import pandas as pd
import logging
from aiogram import Bot, Dispatcher, executor, types
import knopkaa as kb
from aiogram.dispatcher.filters import Text

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
data=pd.read_csv("barber.csv")
@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
      await bot.send_message(message.from_user.id, "Добро пожаловать в «Барбершоп Uncle Chill». Барбершоп «Дядя Chill» — это место, где можно выпить чашечку кофе или угоститься другим любимым напитком, поиграть в бильярд, сделать стрижку или тату, провести мужскую косметологию, маникюр и педикюр, оставаясь верным традициям мужского этикета.С помощью нашего бота, вы сможете записаться онлайн на любой вид наших услуг, ознакомиться с ценами и барным меню, а так же задать любой интересующий Вас вопрос",reply_markup=kb.menu)

@dp.message_handler(Text(equals="🧭 Онлайн-запись"))
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите категорию услуг из списка ниже ⬇️', reply_markup=kb.onlzap)
@dp.message_handler(Text(equals="⬅️ Главное меню"))
async def process_hello(message: types.Message):
      await bot.send_message(message.from_user.id, "Добро пожаловать в «Барбершоп Uncle Chill». Барбершоп «Дядя Chill» — это место, где можно выпить чашечку кофе или угоститься другим любимым напитком, поиграть в бильярд, сделать стрижку или тату, провести мужскую косметологию, маникюр и педикюр, оставаясь верным традициям мужского этикета.С помощью нашего бота, вы сможете записаться онлайн на любой вид наших услуг, ознакомиться с ценами и барным меню, а так же задать любой интересующий Вас вопрос",reply_markup=kb.menu)

@dp.message_handler(Text(equals="☎️ Контакты"))
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, "📍 Адрес: г.Ташкент, ул. Матбуотчилар, 17"
"☎️ Номер телефона: +998 97 776-66-92"
"🌎 Сайт: http://unchlechill.uz"
"📌 Facebook: https://www.facebook.com/barbershop.unclechill/"
"📌 Instagram: https://www.instagram.com/barbershop_unclechill/"
"🤖 Telegram-бот: https://t.me/unclechill_bot️")
@dp.message_handler(Text(equals="❓ Задать вопрос"))
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите ваш вопрос и на него ответят в ближайшее время наши сотрудники.️', reply_markup=kb.questkn)
@dp.message_handler()
async def process_reply(message: types.Message):
      await message.reply("Название заведения: La Creme, "
                          "Сайт: https://lacreme.kz , "
                          "Инстаграм: https://www.instagram.com/la_creme_astana/, "
                          "Местоположение: https://2gis.kz/nur_sultan/firm/70000001022996764 " 



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
