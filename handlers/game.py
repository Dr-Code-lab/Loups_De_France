from aiogram.filters import Command
from aiogram.types import Message

from loader import dp
from .callback import game
from log import logger


@dp.message(Command('game'))
async def to_command_game(message: Message):
	if message.chat.id in [297780530, 722658060] and not game.is_game:
		game.is_game = True
		game.free_places = list(range(1, 11))
		logger.info("GAME", game.is_game)
		# Тут добавить счетчик плюс один к мастеру игры
		# Отправить всем пользователям сообщение о старте игры
		await message.answer(f"Игра началась!")
	else:
		await message.answer(f"Предыдущая игра еще не закончилась!\nНеобходимо обнулиться перед началом новой сессии!")
