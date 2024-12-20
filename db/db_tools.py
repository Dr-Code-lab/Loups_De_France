from sqlalchemy import desc, select

from db import Base, BotUsersTable
from loader import db_session, engine
from log import logger


async def create_table():
	async with engine.begin() as connect_db:
		logger.info("start ENGINE")
		existing_tables = await connect_db.run_sync(
			engine.dialect.has_table,
			table_name='ldf_players',
			schema='public'
			)
		logger.info("end ENGINE: ", existing_tables)
		if not existing_tables:
			logger.info("start CREATION")
			await connect_db.run_sync(Base.metadata.create_all)


async def insert_user_record(user_data):
	async with db_session() as session:
		user = BotUsersTable(**user_data)
		session.add(user)
		logger.info("start CREATION")
		await session.commit()


async def update_user_referrals(referral_id: str, new_referral_id: str):
	async with db_session() as session:
		user = await session.get(BotUsersTable, int(referral_id))
		if user is None:
			logger.info(f"User with ID {referral_id} not found.")
		else:
			logger.info(f"User with ID {user.id} !!!")
		logger.info(user.referrals)
		user.referrals = user.referrals + [new_referral_id]
		user.referrals = list(set(user.referrals))

		try:
			await session.flush()
			await session.commit()
			logger.info("Changes committed successfully.")
		except Exception as e:
			logger.info(f"Error committing changes: {e}")

		updated_user = await session.get(BotUsersTable, int(referral_id))
		logger.info(f"Updated referrals: {updated_user.referrals}")


async def get_user(user_id: str):
	async with db_session() as session:
		stmt = (
			select(BotUsersTable)
			.where(BotUsersTable.chat_id == int(user_id))
			.order_by(desc(BotUsersTable.date))
		)
		result = await session.execute(stmt)
		user = result.scalars().first()

		if user is None:
			logger.info(f"User with ID {user_id} not found.")
		else:
			logger.info(f"User with ID {user.id}: {user}")
		return user
