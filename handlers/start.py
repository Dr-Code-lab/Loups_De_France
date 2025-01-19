from aiogram.filters import CommandStart
from aiogram.types import Message

from db import get_user, insert_user_record, update_user_referrals
from keyboards.inline import keyboard, keyboard_game
from loader import dp
from log import logger
from log import logger


@dp.message(CommandStart())
async def to_command_start(message: Message):
	"""
	This handler receives messages with `/start` command
	"""
	# Получаем аргументы из команды
	logger.info("START!", type(message.chat.id), type(message.chat.username), type(message.date), message.text)
	logger.info("!!!!", message)
	# Извлекаем реферальный ID из текста сообщения
	command_args = message.text.split(maxsplit=1)
	referral_id = command_args[1] if len(command_args) > 1 else None
	logger.info("?????", type(referral_id), referral_id)
	logger.info(f"{type(message.chat.id)}\t{str(message)}")
	user_data = dict(chat_id=message.chat.id, name=message.chat.username, date=message.date, referral_id=referral_id)
	user_db_record = await get_user(user_id=str(message.chat.id))
	logger.info("USER:", user_db_record)
	if not user_db_record:
		await insert_user_record(user_data)
		logger.info("DONE INSERT")
	if referral_id:
		await update_user_referrals(referral_id=referral_id, new_referral_id=str(message.chat.id))
	await message.answer(
		"""Добро пожаловать в Loups de France! 🐺\n
		Этот бот создан для того, чтобы сделать ваш игровой опыт ещё удобнее и интереснее!
		"""
	)
	await message.answer(
		f"""С помощью бота Loups de France вы сможете:\n
		• 💳 Пополнять баланс для участия в играх через карту.\n
		• 🪑 Гарантировать место за игровым столом, пополняя баланс заранее.\n
		• 📊 Следить за своей игровой статистикой и успехами.\n
		• 👥 Легко приглашать друзей на мероприятия.\n
		• И многое другое — новые функции уже в разработке!
		"""
	)
	await message.answer(
		f"""💳 Пополняйте баланс через карту, чтобы получать выгодные бонусы!\n
		Спасибо, что вы с нами! 🎲\n\n
		Если у вас есть вопросы или предложения, пишите администратору.
		"""
	)
	await message.answer(f"Выберите действие:", reply_markup=keyboard)
	await message.answer(f"Сыграем?", reply_markup=keyboard_game.as_markup())
