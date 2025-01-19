from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"key": "value", ...}

db_url = config.get("DB_URL")
token = config.get("BOT_TOKEN")
admin_token = config.get("BOT_ADMIN")
ip = config.get("IP")

bot_slave_id = config.get("SLAVE_ID")
