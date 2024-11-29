from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder


masha_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="MashaGPT",
                         url='https://t.me/mashagpt'),
    InlineKeyboardButton(text="Получить промокод",
                         callback_data='promo_code'),
]])
