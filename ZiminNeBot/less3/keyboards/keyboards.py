from aiogram import types


button1 = types.KeyboardButton(text='О владельце')
button2 = types.KeyboardButton(text='/help')
button3 = types.KeyboardButton(text='/info')
button4 = types.KeyboardButton(text='О лисах')
button5 = types.KeyboardButton(text='/raspisaniye')
button6 = types.KeyboardButton(text='/prof')
button7 = types.KeyboardButton(text='До свидания')
button8 = types.KeyboardButton(text='Закрыть')
button9 = types.KeyboardButton(text='Описание')
button10 = types.KeyboardButton(text='Ареал обитания')
button11 = types.KeyboardButton(text='Покажи лису')
button12 = types.KeyboardButton(text='Фольклор')
button13 = types.KeyboardButton(text='Виды')
button14 = types.KeyboardButton(text='/start')



keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6],
    [button7,  button8],
]

# О лисах
keyboard2 = [
    [button9, button10, button11],
    [button12, button13],
    [button14, button8],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)