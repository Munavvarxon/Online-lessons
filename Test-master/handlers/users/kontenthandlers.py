from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer('Bu qanday rasm ?')
#
# @dp.message_handler(content_types='photo')
# async def photo_handler(msg: types.Message):
#     await msg.answer('Bu kimning rasmi ?')

@dp.message_handler(content_types='sticker')
# @dp.message_handler(content_types=types.Message.sticker)
async def emoji_handler(msg: types.Message):
    await msg.answer('😊')

@dp.message_handler(content_types='contact')
# @dp.message_handler(content_types=types.Message.contact)
async def contact_handler(msg: types.Message):
    await msg.answer('Kim bu odam')

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def audio_handler(msg: types.Message):
    await msg.answer('Yaxshi eshitmadim')

@dp.message_handler(content_types='document')
async def document_handler(msg: types.Message):
    await msg.answer('Bu qanday hujjat')


