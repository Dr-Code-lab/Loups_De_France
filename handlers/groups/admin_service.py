from aiogram import types

from loader import admin_dp


@admin_dp.chat_member()
async def welcome_message(chat_member: types.ChatMemberUpdated):
	print(f"new: {chat_member.new_chat_member.status}")
	print(f"old: {chat_member.old_chat_member.status}")
	await chat_member.answer(f"Hi!")
