import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("bot.log")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s ** %(filename)s:%(lineno)d ** %(funcName)s ** %(levelname)s ** %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)