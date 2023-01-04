from winreg import QueryInfoKey, QueryValue, QueryValueEx
from aiogram import types, Dispatcher
from keyboards import callback_data, choice, action_callback 
from create_bot import dp, bot
from aiogram.types import Message, CallbackQuery
import re
value = ''
old_value = ''
list = []
list_oper = []
list_elemens = []
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!", reply_markup=choice)
    

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Набери на клавиатуре, что тебе нужно посчитать.")
    await bot.send_message(message.from_user.id, "0", reply_markup=choice)

@dp.callback_query_handler(lambda c: c.data !='' )
async def callback_func(query: types.CallbackQuery):
    global value, old_value, list, list_oper,list_elemens
    
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = '0'
    elif data == '+':
        list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
        # list_elemens = re.split(r"[-|+|*|/]+", value)
        # print(list)
        value += f' {data} '
        # list_oper.append('+')
        # print(list_oper)
        # list_elemens.append('+')
        # print(list_elemens)
        # print(value)
    elif data == '-':
        list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
        # list_elemens = re.split(r"[-|+|*|/]+", value)
        # print(list)
        value += f' {data} '
        # list_oper.append('-')
        # print(list_oper)
        # list_elemens.append('-')
        # print(list_elemens)
        # print(value)
    elif data == '*':
        list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
        # list_elemens = re.split(r"[-|+|*|/]+", value)
        # print(list)
        value += f' {data} '
        # list_oper.append('*')
        # print(list_oper)
        # list_elemens.append('*')
    elif data == '/':
        list = re.split(r"[-|+|*|/]+", value) # для контроля лишней точки
        # list_elemens = re.split(r"[-|+|*|/]+", value)
        # print(list)
        value += f' {data} '
        # list_oper.append('/')
        # print(list_oper)
        # list_elemens.append('/')
        
    elif data == '<':
        value = value[:-1] if len(value) != 1 else '0'
    elif data == '.': 
        list = re.split(r"[-|+|*|/]+", value)
        # print(list)
        if list[-1].count('.') != 0: # если в последнем элементе списка есть '.', то вторую не даст поставить
            pass
        else:
            value += data
           
    elif data == '=':
        list_elemens = value.split()
        print(list_elemens)
        actions = {
	    "*": lambda x, y: str(float(x) * float(y)),
	    "/": lambda x, y: str(float(x) / float(y)),
	    "+": lambda x, y: str(float(x) + float(y)),
	    "-": lambda x, y: str(float(x) - float(y))}
        
        # list = re.split(r"[-|+|*|/]+", value) 
        # list_elemens = re.split(r"[-|+|*|/]+", value)
        # print(list_elemens)
        
        list_oper_ind = [i for i,e in enumerate(list_elemens) if e in '*/']
        while list_oper_ind:
            ind_op = list_oper_ind[0]
            a, b, c = list_elemens[ind_op-1:ind_op+2]
            list_elemens[ind_op-1:ind_op+2] = [actions[b](a,c)]
            print(list_elemens[ind_op-1:ind_op+2])
            list_oper_ind = [i for i,e in enumerate(list_elemens) if e in '*/']
        print(list_elemens)
        while len(list_elemens) > 1:
            a, b, c = list_elemens[:3]
            list_elemens[:3] = [actions[b](a,c)]

        value = list_elemens[0]

    else:
        if value == "0":
            value = data
        else:
            value += data
    # await query.message.edit_text(f"{value}", reply_markup=choice)
    if value != old_value:
        if value == " ":
            await query.message.edit_text("0", reply_markup=choice)
            # await bot.edit_message_text(chat_id=query.message.chat.id, massage_id = query.message.message.id, text = "0", reply_markup=choice)
        else:
            await query.message.edit_text(f"{value}", reply_markup=choice)
            # await bot.edit_message_text(chat_id=query.message.chat.id, massage_id = query.message.message.id, text = value, reply_markup=choice)
    old_value = value


    # await query.message.edit_text(f"{query.data}", reply_markup=choice)
