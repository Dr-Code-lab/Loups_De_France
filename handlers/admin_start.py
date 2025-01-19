from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.masha import masha_keyboard
from loader import admin_dp


@admin_dp.message(CommandStart())
async def to_command_start(message: Message):
	"""
	This handler receives messages with `/start` command
	"""
	await message.answer(
		f"Для получения промокода подпишись на канал https://t.me/mashagpt", reply_markup=masha_keyboard
		)

# %%
