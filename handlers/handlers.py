from aiogram import types


def register(dp):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        print(message)
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message)
