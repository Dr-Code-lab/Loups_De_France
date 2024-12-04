import asyncio

from db import create_table
from handlers import dp
from loader import bot
from log import logger
from misc import set_my_commands


async def main():
	logger.info("Starting bot")
	await create_table()
	# start
	await set_my_commands()
	try:
		await dp.start_polling(bot)
	finally:
		logger.info("Stopping bot")
		await dp.storage.close()
		await bot.session.close()
	return "some json"


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except (KeyboardInterrupt, SystemExit):
		logger.error("EXIT!")
