from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp

@dp.message_handler(Text(equals='assalamu alaykum', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Vaalaykum assalom')

@dp.message_handler(Text(contains='assalom', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Waalaykum assalom')

# boshqa parametrlar
#startswith
#endswith