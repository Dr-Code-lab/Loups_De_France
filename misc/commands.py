from aiogram.types import BotCommand

from loader import bot


async def set_my_commands():
	commands = [BotCommand(command='start', description='Начать расчет!'),
				BotCommand(command='game', description='Начать игру!'),
				BotCommand(command='clean', description='Обнулить данные!')]

	await bot.set_my_commands(commands)
