from aiogram import Bot, Dispatcher, executor, types
import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Hey!")


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
