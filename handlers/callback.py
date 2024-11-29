import random
from aiogram import F
from aiogram.types import CallbackQuery
from loader import dp
from models import Game
from db import get_user, insert_user_record


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
            user = await get_user(user_id=str(call.message.chat.id))
            print("@@@@", user)
            if user.balance > 4:
                user.balance -= 5
                user_data = dict(chat_id=call.message.chat.id,
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
                game.busy_places.append(place)
                await call.message.answer(f"Бинго! Ваше место за столом:\n\n{place}")
            else:
                print(f"Balance for {call.message.chat.id}: {user.balance} not enough")
                await call.message.answer(f"Упс! Пополните баланс и попробуйте снова")
    else:
        await call.message.answer(f"Упс! Подождите начала игры и попробуйте снова")
