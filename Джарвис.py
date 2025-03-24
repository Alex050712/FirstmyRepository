from Кнопки import kb1
from aiogram import Bot, Dispatcher, types, F, Router
import asyncio
import adress
import logging
from aiogram.filters.command import Command
import datetime
from photo2 import fox
history = []


n = fox()
use_token = adress.token
logging.basicConfig(level=logging.INFO)
bot = Bot(token = use_token)
dp = Dispatcher()
router = Router()


@dp.message(Command('start'))
async def command_start(message: types.Message):
    m = message.message_id
    await message.chat.delete_message(m)
    await message.answer('Привет всем😄')
    await message.answer('Чтобы узнать команды введи команду:/Инструкция')
@dp.message(Command('Инструкция'))
async def command_start(message: types.Message):
    await message.answer('Инструкция:')
    await message.answer('/Пивет - Джарвис_чат попреветствует вас.')
    await message.answer('/Сейчас - Джарвис_чат выводит время и дату.')
    await message.answer('/Лиса - Джарвис_чат выведит фото лисы или лис.')
    await message.answer('/Клавиатура - Джарвис_чат выводит клавиатуру чата.')
    await message.answer('Внимание! - Джарвис_чат имеет цензур-функцию.')


@dp.message(Command('Привет'))
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}!✋')
@dp.message(Command('Клавиатура'))
async def command_start(message: types.Message):
    await message.answer(text = 'Клавиатура:',reply_markup=kb1)
@dp.callback_query(F.data == 'Привет')
async def kb(callback: types.CallbackQuery):
    await callback.message.answer(f'Привет!✋')
@dp.callback_query(F.data == 'Сейчас')
async def kb(callback: types.CallbackQuery):
    dt = datetime.datetime.now()
    await callback.message.answer(f'Сейчас{dt}🕓')




@dp.message(Command('Сейчас'))
async def command_start(message: types.Message):
    dt = datetime.datetime.now()
    await  message.answer(f'Сейчас{dt}🕓')
@dp.message(Command('8_марта'))
async def command_start(message: types.Message):
    await  message.answer("С 8 марта!🎉")
    await message.answer("💐")
@dp.message(Command('История'))
async def command_start(message: types.Message):
    m = message.message_id
    await message.chat.delete_message(m)
    await message.answer(f"{history}")
@dp.message(Command('Лиса'))
async def command_start(message: types.Message):
    n = fox()
    await bot.send_photo(message.chat.id, n)
@dp.message(F.text)
async def command_start(message: types.Message):
    user_message = message.text
    who = message.from_user.username
    history.append(user_message)
    print(f'{who}:{user_message}')
    if 'Дурак' in message.text:
        m = message.message_id
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'дурак' in message.text:
        m = message.message_id
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'Дура' in message.text:
        m = message.message_id
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'дура' in message.text:
        m = message.message_id
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'дебил' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'Дебил' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'идиот' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'Идиот' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'Дубина' in message.text:
        m = message.message_id
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'дубина' in message.text:
        m = message.message_id
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'Тупой' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'тупой' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'Тупая' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
    elif 'тупая' in message.text:
        m = message.message_id
        await bot.ban_chat_member(chat_id=-1002236134027, user_id=message.from_user.id)
        await message.chat.delete_message(m)
        await message.answer("Не ругайся!")
















async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())


