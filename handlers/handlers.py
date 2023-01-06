from aiogram import types
from repository.user.repository import UserRepository
from services.user.service import UserService


def register(dp):
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

    @dp.message_handler()
    async def echo(message: types.Message):
        user = message.from_user
        user_repository = UserRepository()
        user_service = UserService(user_repository)
        user_service.add(first_name=user.first_name,
                         user_name=user.username,
                         language_code=user.language_code)
        await message.answer(message)
