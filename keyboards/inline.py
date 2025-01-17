from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

keyboard = InlineKeyboardMarkup(
	inline_keyboard=[
		[
		InlineKeyboardButton(
			text="Пополнить баланс",
			callback_data='donat'
			),
		InlineKeyboardButton(
			text="Пригласить друга",
			callback_data='ref_link'
			)],
		[
		InlineKeyboardButton(
			text="Узнать баланс",
			callback_data='balance'
		),
	]]
)

keyboard_game = InlineKeyboardBuilder()
keyboard_game.button(text=f'Войти в игру', callback_data='play_game')

keyboard_fee = InlineKeyboardBuilder()
keyboard_fee.button(text=f'Самозанятость 6%', callback_data='6')
for i in [7, 8, 9, 10]:
	keyboard_fee.button(text=f'ИП {i}%', callback_data=f'{i}')
	keyboard_fee.adjust(1, 2)
