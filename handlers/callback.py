import random

from aiogram import F
from aiogram.types import CallbackQuery

from db import get_user, insert_user_record
from loader import dp
from models import Game

game = Game()


@dp.callback_query(F.data == "donat")
async def put_donat(call: CallbackQuery):
	await call.message.answer(
		f"""Переведите ваш донат на карту №:\n\n
		Nom : VSEVOLOD AFANASJEV IBAN: DE41100110012628258599 BIC: NTSBDEB1XXX"""
	)


@dp.callback_query(F.data == "ref_link")
async def get_referral_link(call: CallbackQuery):
	await call.message.answer(
		f"Ваша реферальная ссылка:\n\nhttps://t.me/LoupsDeFrance_bot?start={call.message.chat.id}\n\nперешлите её другу"
		)


@dp.callback_query(F.data == "play_game")
async def select_place(call: CallbackQuery):
	if game.is_game and call.message.chat.id not in game.current_players:
		print(call.message)
		if not game.free_places:
			await call.message.answer(f"Упс! кажется вам не осталось места, попробуйте снова позднее")
		place = random.choice(game.free_places)
		if place:
			user = await get_user(user_id=str(call.message.chat.id))
			print("@@@@", user)
			if user.balance >= 5:
				user.balance -= 5
				user_data = dict(
					chat_id=call.message.chat.id,
					name=call.message.chat.username,
					date=call.message.date,
					referral_id=user.referral_id,
					referrals=user.referrals,
					place=place,
					balance=user.balance,
					status="4len",
					club_name="Loups de Paris",
					)
				await insert_user_record(user_data)
				print(f"Place for {call.message.chat.id}: {place}")
				game.free_places.remove(place)
				game.busy_places.append(place)
				game.current_players.append(call.message.chat.id)
				await call.message.answer(
					f"""Бинго! Ваше место за столом:\n\n{place}\n\n
					в игре уже {len(game.current_players)} игроков"""
				)
			else:
				print(f"Balance for {call.message.chat.id}: {user.balance} not enough")
				await call.message.answer(f"Упс! Пополните баланс и попробуйте снова")
	elif call.message.chat.id in game.current_players:
		await call.message.answer(f"Упс! Кажется вы уже на своем месте")
	else:
		await call.message.answer(f"Упс! Дождитесь начала игры и попробуйте снова")
