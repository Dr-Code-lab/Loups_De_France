from aiogram.filters import CommandStart
from aiogram.types import Message

from db import get_user, insert_user_record, update_user_referrals
from keyboards.inline import keyboard, keyboard_game
from loader import dp
from log import logger


@dp.message(CommandStart())
async def to_command_start(message: Message):
	"""
	This handler receives messages with `/start` command
	"""
	# Получаем аргументы из команды
	print("START!", type(message.chat.id), type(message.chat.username), type(message.date), message.text)
	print("!!!!", message)
	# Извлекаем реферальный ID из текста сообщения
	command_args = message.text.split(maxsplit=1)
	referral_id = command_args[1] if len(command_args) > 1 else None
	print("?????", type(referral_id), referral_id)
	logger.info(f"{type(message.chat.id)}\t{str(message)}")
	user_data = dict(chat_id=message.chat.id, name=message.chat.username, date=message.date, referral_id=referral_id)
	user_db_record = await get_user(user_id=str(message.chat.id))
	print("USER:", user_db_record)
	if not user_db_record:
		await insert_user_record(user_data)
		print("DONE I?NSERT")
	if referral_id:
		await update_user_referrals(referral_id=referral_id, new_referral_id=str(message.chat.id))
	await message.answer(f"Выберите действие:", reply_markup=keyboard)
	await message.answer(f"Сыграем?", reply_markup=keyboard_game.as_markup())
