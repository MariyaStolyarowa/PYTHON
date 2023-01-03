from winreg import QueryInfoKey, QueryValue, QueryValueEx
from aiogram import types, Dispatcher
from keyboards import callback_data, choice, action_callback 
from create_bot import dp, bot
from aiogram.types import Message, CallbackQuery

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!", reply_markup=choice)
  

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Набери на клавиатуре, что тебе нужно посчитать.")
    await bot.send_message(message.from_user.id, "0", reply_markup=choice)

# @dp.callback_query_handler(func = lambda c: c.data)
# async def callback_command(query: types.CallbackQuery):
#     await bot.send_message(query.from_user.id, f"{query.data}", reply_markup=choice)

