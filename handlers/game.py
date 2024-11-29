from aiogram.filters import Command
from aiogram.types import Message
from loader import dp
from .callback import game


@dp.message(Command('game'))
async def to_command_game(message: Message):
    if message.chat.id in [297780530, 722658060]:
        game.is_game = True
        print("GAME", game.is_game)
        # Тут добавить счетчик плюс один к мастеру игры
        # Отправить всем пользователям сообщение о старте игры
        await message.answer(f"Игра началась.")
