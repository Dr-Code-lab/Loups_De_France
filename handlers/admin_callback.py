import uuid

from aiogram import F
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.methods import GetChatMember
from aiogram.types import CallbackQuery

from config import bot_slave_id
from keyboards.masha import masha_keyboard
from loader import admin_dp, bot_admin


@admin_dp.callback_query(F.data == "promo_code")
async def select_fee_(call: CallbackQuery):
	promocode = f"""MashaGPT-{str(uuid.uuid1())}"""
	print(promocode)
	subscribe = await bot_admin(GetChatMember(chat_id=bot_slave_id, user_id=call.from_user.id))
	print("START!", subscribe.status, ChatMemberStatus.MEMBER)
	if subscribe.status == ChatMemberStatus.MEMBER:
		await call.message.answer(f"Ваш промокод: {promocode}")
	else:
		await call.message.answer(
			f"Для получения промокода подпишись на канал https://t.me/mashagpt", reply_markup=masha_keyboard
		)
