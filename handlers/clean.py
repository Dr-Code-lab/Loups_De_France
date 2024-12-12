from aiogram.filters import Command
from aiogram.types import Message

from loader import dp
from .callback import game


@dp.message(Command('clean'))
async def to_command_clean(message: Message):
	game.is_game = False
	game.busy_places = []
	game. current_players = []
	await message.answer(f"Игра обнулилась.")
