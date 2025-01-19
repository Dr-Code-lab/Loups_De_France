from sqlalchemy import ARRAY, BigInteger, Boolean, Column, DateTime, Float, Integer, String

from db import Base


class BotUsersTable(Base):
	__tablename__ = 'ldf_players'

	id = Column(BigInteger, primary_key=True, autoincrement=True)
	chat_id = Column(BigInteger)
	name = Column(String, default=None)
	date = Column(DateTime(timezone=True))
	balance = Column(Float, default=0)
	place = Column(Integer, default=0)
	is_sheriff = Column(Boolean, default=False)
	is_don = Column(Boolean, default=False)
	is_mafia = Column(Boolean, default=False)
	is_master_games = Column(Boolean, default=False)
	status = Column(String, default="4len")
	club_name = Column(String, default="Loups de Paris")
	referral_id = Column(String, default=None)
	referrals = Column(ARRAY(String), default=[])
