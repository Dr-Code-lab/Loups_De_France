from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from aiogram import Bot, Dispatcher
# import redis
# from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
import config


engine = create_async_engine(url=config.db_url, echo=True)
db_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

storage = MemoryStorage()
admin_storage = MemoryStorage()
bot = Bot(token=config.token)
bot_admin = Bot(token=config.admin_token)
dp = Dispatcher(bot=bot, storage=storage)
admin_dp = Dispatcher(bot=bot_admin, storage=admin_storage)
