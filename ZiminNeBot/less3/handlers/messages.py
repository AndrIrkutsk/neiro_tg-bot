from aiogram import F, Router
from aiogram import types
from keyboards.keyboards import kb2, kb1

router = Router()

# Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' == msg_user:
        await message.answer(f'Привет-привет 👋👋, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'До скорой встречи 😉, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')