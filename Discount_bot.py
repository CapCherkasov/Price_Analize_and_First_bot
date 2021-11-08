import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink

from main import collect_data

bot = Bot((token := "2123557330:AAEPq3qc9dc_ohX7eWi89B7Vqr4aK6lasfw"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ["Кроссовки"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Кроссовки со скидкой", reply_markup=keyboard)


@dp.message_handler(Text(equals="Кроссовки"))
async def get_discount_sneakers(message: types.Message):
    await message.answer('Пожалуйста, ждите, я сканирую сайт...')

    collect_data()

    with open("result_data.json") as file:
        data = json.load(file)

    for item in data:
        card = f"{hlink(item.get('title'), item.get('link'))}\n" \
               f"{hbold('Цена: ')} {item.get('price_base')}\n" \
               f"{hbold('Цена со скидкой: ')} {item.get('discount_percent')}%: {item.get('price_sale')}"

        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
