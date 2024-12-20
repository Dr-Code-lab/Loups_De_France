from aiogram.filters import Command
from aiogram.types import Message

from loader import dp
from .callback import game


@dp.message(Command('clean'))
async def to_command_clean(message: Message):
	if message.chat.id in [297780530, 722658060] and not game.is_game:
		game.is_game = False
		game.busy_places = []
		game. current_players = []
		await message.answer(f"Игра обнулилась.")
	else:
		await message.answer(f"Действиие доступно только администратору игры")

