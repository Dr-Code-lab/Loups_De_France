from aiogram import types

from loader import admin_dp
from log import logger


@admin_dp.chat_member()
async def welcome_message(chat_member: types.ChatMemberUpdated):
	logger.info(f"new: {chat_member.new_chat_member.status}")
	logger.info(f"old: {chat_member.old_chat_member.status}")
	await chat_member.answer(f"Hi!")
