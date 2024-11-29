import random
from aiogram import F
from aiogram.types import CallbackQuery
from loader import dp
from models import Game
from keyboards.inline import keyboard_game
from db import update_user_place


game = Game()


@dp.callback_query(F.data == "donat")
async def put_donat(call: CallbackQuery):
    await call.message.answer(f"Переведите ваш донат на карту №:\n\n1234567890")


@dp.callback_query(F.data == "ref_link")
async def get_referral_link(call: CallbackQuery):
    await call.message.answer(f"Ваша реферальная ссылка:\n\nhttps://t.me/LoupsDeFrance_bot?start={call.message.chat.id}\n\nперешлите её другу")


@dp.callback_query(F.data == "play_game")
async def select_place(call: CallbackQuery):
    if game.is_game:
        print(call.message)
        range_places = [n for n in range(1, 11) if n not in game.busy_places] # чекнуть места тут
        if not range_places:
            await call.message.answer(f"Упс! кажется вам не осталось места, попробуйте снова позднее")
        place = random.choice(range_places)
        if place:
            is_ok = await update_user_place(player_id=str(call.message.chat.id), place=place)
            if is_ok:
                game.busy_places.append(place)
                await call.message.answer(f"Бинго! Ваше место за столом:\n\n{place}")
            else:
                await call.message.answer(f"Упс! Пополните баланс и попробуйте снова")
    else:
        await call.message.answer(f"Упс! Подождите начала игры и попробуйте снова")
