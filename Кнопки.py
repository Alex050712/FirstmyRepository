from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button1 = InlineKeyboardButton(text = 'Привет', callback_data='Привет')
button2 = InlineKeyboardButton(text = 'Сейчас', callback_data='Сейчас')
kb1 = InlineKeyboardMarkup(inline_keyboard = [[button1 , button2]
                                              ])