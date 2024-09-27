from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from database.db_sqlite import Database


TOKEN = '6801894956:AAHyT-eLFdNfXQsrpprPl21ln6-31f_3YMc'
ADMIN = 267910201

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
db = Database(path_to_db='database/main.db')
