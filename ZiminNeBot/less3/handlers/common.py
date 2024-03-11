from aiogram import types, F, Router
from aiogram.filters.command import Command
from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox

router = Router()

# Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name} 👋', reply_markup=kb1)


# Хэндлер на команду /stop, До свидания
@router.message(Command('stop'))
@router.message(Command('Стоп'))
@router.message(Command('До свидания'))
@router.message(F.text.lower() == 'стоп')
@router.message(F.text.lower() == 'до свидания')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')


# Хэндлер на команду /help
@router.message(Command('help'))
@router.message(Command('Помощь'))
async def cmd_help(message: types.Message):
    await message.answer(f'Наберите команды или перейдите по ссылкам: /info, /user, /raspisaniye, /fox, /prof. \n '
                         f'Словосочетания "ты кто" или "лиса" в предложениях дают реакции 😊.')

# Хэндлер на команду /info
@router.message(Command('info'))
async def cmd_info(message: types.Message):
    await message.answer(f'Андрей Зимин учится на курсе fullstack-разработчик и нейрохищник.')


# Хэндлер на команду /user
@router.message(Command('user'))
async def cmd_user(message: types.Message):
    await message.answer(f'Андрей Зимин')


# Хэндлер на команду /raspisaniye
@router.message(Command('raspisaniye'))
async def cmd_rasp(message: types.Message):
    await message.answer(
        f'Разработка контент-плана для социальных сетей - 13.03.2024 г. 00:00 - 02:00 Ирk. \n'
        f'Креативы для рекламы и контент-маркетин - 15.03.2024 г. 00:00 - 02:00 Ирк. \n'
        f'Рубрики и интерактивные коммуникации - 16.03.2024 г. 18:00 - 20:00 Ирк. \n'
        f'Разбор заданий. Курс: Креативы для рекламы и контент-маркетинг - 17.03.2024 г. 18:00 - 20:00 Ирк. \n'
        f'Создание креативов для контент-планов - 19.03.2024 г. 23:00 - 01:00 Ирк. \n'
        f'Материалы к теме "Оптимизация работы с нейросетью - 20.03.2024 г \n'
        f'Креативы для рекламы и контент-маркетинг - 22.03.2024 г. 00:00 - 02:00 Ирк. \n'
    )

# Хэндлер на команду - О владельце
@router.message(Command('О владельце'))
@router.message(F.text.lower() == 'о владельце')
async def cmd_info_user(message: types.Message):
    await message.answer(f'Я бывший повар-кондитер 4 разряда. В веб-разработке не первый день, знаю основы JavaScript, PhP, '
                         f'немного jQuery, MySQL, а также HTML5 и CSS3. Участвовал в создании своего проекта сайта знакомств '
                         f'наподобии Tabor.ru с использованием ООП Php.')


# Хэндлер на команду - Закрыть
@router.message(Command('Закрыть'))
@router.message(F.text.lower() == 'закрыть')
async def cmd_close_button(message: types.Message):
    await message.reply(f'Закрываю клавиатуру', reply_markup=types.ReplyKeyboardRemove())


# Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
    # await bot.send_photo(message.from_user.id, photo=img_fox)


# Хэндлер на команду - Описание
@router.message(Command('Описание'))
@router.message(F.text.lower() == 'описание')
async def cmd_for_fox(message: types.Message):
    await message.answer(f'лиса́ — хищное млекопитающее семейства псовых, наиболее распространённый и самый крупный '
                         f'вид рода лисиц. Длина тела 60—90 см, хвоста — 40—60 см, масса — 6—10 кг.')


# Хэндлер на команду - ареал обитания
@router.message(Command('ареал обитания'))
@router.message(F.text.lower() == 'ареал обитания')
async def cmd_areal_fox(message: types.Message):
    await message.answer(f'Лисица распространена весьма широко: на всей территории Европы, Северной Африки (Египет, Алжир, '
                         f'Марокко, северный Тунис), большей части Азии (вплоть до северной Индии, южного Китая и Индокитая), '
                         f'в Северной Америке от арктической зоны до северного побережья Мексиканского залива.')


# Хэндлер на команду - фольклор
@router.message(Command('Фольклор'))
@router.message(F.text.lower() == 'фольклор')
async def cmd_folclor(message: types.Message):
    await message.answer(f'Лиса является частым персонажем фольклора о животных. В восточно-славянских сказках лиса обычно '
                         f'зовётся Лиса Патрикеевна. Многие примеры подобных сказок включены в состав сборника Афанасьева. '
                         f'В средневековом фольклоре Европы важную роль играет лис Ренар (Рейнеке-лис)[2]. В странах Восточной '
                         f'Азии распространены легенды о лисах-оборотнях. Согласно академику В. Н. Топорову, в японской мифологии '
                         f'лисица (кицунэ) — «вестница богини Инари, обладающая колдовскими чарами и способностью воплощаться в '
                         f'человека»[2] . Сходны мифы о лисах-оборотнях известны также в Корее (кумихо) и Китае (хули-цзин).')


# Хэндлер на команду - фольклор
@router.message(Command('Виды'))
@router.message(F.text.lower() == 'виды')
async def cmd_view_fox(message: types.Message):
    await message.answer(f'- Бенгальская лисица (Vulpes bengalensis) \n'
                         f'- Афганская лисица (Vulpes cana)\n'
                         f'- Южноафриканская лисица (Vulpes chama)\n'
                         f'- Корсак (Vulpes corsac)\n'
                         f'- Тибетская лисица (Vulpes ferrilata)\n'
                         f'- Песец (Vulpes lagopus)\n'
                         f'- Американская лисица (Vulpes macrotis)\n'
                         f'- Африканская лисица (Vulpes pallida)\n'
                         f'- Песчаная лисица (Vulpes rueppellii)\n'
                         f'- Американский корсак (Vulpes velox)\n'
                         f'- Обыкновенная лисица (Vulpes vulpes)\n'
                         f'- Фенек (Vulpes zerda)')