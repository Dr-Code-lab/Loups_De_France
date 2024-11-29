from db import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Float, Integer, ARRAY


class BotUsersTable(Base):
    __tablename__ = 'ldf_users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, default=None)
    date = Column(DateTime(timezone=True))
    referral_id = Column(String, default=None)
    referrals = Column(ARRAY(String), default=[])
    balance = Column(Float, default=0)
    club_name = Column(String, default="Loups de Paris")
    status = Column(String, default="4len")
    quantity_games = Column(Integer, default=0)
    sheriff_games = Column(Integer, default=0)
    don_games = Column(Integer, default=0)
    mafia_games = Column(Integer, default=0)
    master_games = Column(Integer, default=0)
    place = Column(Integer, default=0)
