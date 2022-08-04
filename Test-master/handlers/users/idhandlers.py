from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

SUPERUSERS = [588619602]
BLACKLIST = [1564]

@dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_example(msg: types.Message):
    await msg.answer('Xush kelibsiz, SuperUser!')