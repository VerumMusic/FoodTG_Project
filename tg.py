from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import hlink
from choose import choose, choose_decs, choose_week
import logging
logging.basicConfig(level=logging.INFO)
from main import opener
import os

TOKEN = load_dotenv
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_day_menu = types.KeyboardButton("📅 Сгенерировать меню на день")
    button_week_menu = types.KeyboardButton("📆 Сгенерировать меню на неделю")
    keyboard.add(button_day_menu, button_week_menu)
    await message.reply(f'{message.from_user.first_name}, 👋 Добро пожаловать!\n\n📅 Нажмите на кнопку "Сгенерировать меню на день", чтобы сгенерировать случайное или выбранное меню на сегодня. \n📆 Или выберите опцию "Сгенерировать меню на неделю", чтобы получить меню, подобранное на всю неделю. ', reply_markup=keyboard)
    logging.info(f"Received /start command from {message.from_user.first_name}")

@dp.message_handler(text="📅 Сгенерировать меню на день")
async def generate_day_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=1)
    random_generation = types.KeyboardButton("🔀 Рандомная генерация")
    choose_generation = types.KeyboardButton("📝 Выборочная генерация")
    kb.add(random_generation, choose_generation)
    kb_inline = types.InlineKeyboardMarkup()
    
    random_gen = types.InlineKeyboardButton("🔀 Рандомная генерация", callback_data="generate_random")
    option_gen = types.InlineKeyboardButton("📝 Выборочная генерация", callback_data="generate_optionally")
    kb_inline.add(*[random_gen, option_gen])
    await message.reply('🔀 Нажмите на кнопку "Рандомная генерация", чтобы получить случайное меню на сегодня. 🍽️\n\n📝 Выберите опцию "Выборочная генерация", чтобы получить меню, специально подобранное для конкретного типа питания или диеты. 🥗', reply_markup=kb_inline)
    logging.info("Received button_day command")
    
    
@dp.callback_query_handler(lambda query: query.data == "generate_random")
async def process_button_click(query: types.CallbackQuery):
    await query.answer("Генерирую рандомное меню на день...")
    
    # Вызываем функцию generate_random
    await generate_random(query.message)
    
    
@dp.callback_query_handler(lambda query: query.data == "generate_optionally")
async def process_button_click(query: types.CallbackQuery):
    
    await generate_optionally(query.message)


@dp.message_handler(text = "🔀 Рандомная генерация")
async def generate_random(message: types.Message):
    day_menu = choose()
    day_menu_message = "\n".join(day_menu).split("|")
    
    for i in day_menu_message:
        if i.startswith("Ссылка"):
            link = await hlink("Рецепт", i.split("Ссылка на рецепт: ")[1])
            await message.answer(f"Ссылка: {link}")
        else:
            await message.answer(i)
            
    await message.reply("Меню на день сгенерировано!")
    logging.info("Received generate_random command")
    
@dp.message_handler(text = "📝 Выборочная генерация") #Выборочная генерация
async def generate_optionally(message: types.Message):
    #написать код для спортивного, правильного/здорового, для диабетиков и вкусного питания.
    kb = types.ReplyKeyboardRemove()
    kb_alot = types.InlineKeyboardMarkup(row_width=2)
    sport_but = types.KeyboardButton("Спортивное питание", callback_data='sport_but')
    right_but = types.KeyboardButton("Правильное питание", callback_data='right_but')
    soon = types.KeyboardButton("Скоро...", callback_data = "soon")
    kb_alot.add(*[sport_but, right_but, soon])
    await message.reply("Выберите подходящую кнопку --", reply_markup=kb_alot)
    logging.info("Received generate_optionally command")
    
@dp.callback_query_handler(lambda query: query.data == "right_but")
async def callback_handler(callback_query: types.CallbackQuery):
    await callback_query.answer("  Генерирую меню для здоровых...  ")
    await healthy(callback_query.message)
    
@dp.callback_query_handler(lambda q: q.data == "soon")
async def clbh(cquery: types.CallbackQuery):
    await cquery.answer("  Скоро...  ")
    await soon(cquery.message)
    
async def soon(msg: types.Message):
    await msg.answer("В ближайшем будущем будут добавлены такие генерации как: 🥗🥦 Питание для диабетиков 🥑🥕  \n🍔🍕 Вкусное питание 🍝🍰  \n🎉🥂 Праздничное меню 🍽️🎂")


    
async def healthy(message: types.Message):
    os.chdir("./database/healthy_food")
    day_menu_message = "\n".join(choose_decs()).split("|")
    for i in day_menu_message:
        await message.answer(i)
    os.chdir("../..")
    logging.info("Received healthy command")
    
@dp.callback_query_handler(lambda q: q.data == "sport_but")
async def callback_handl(c_query: types.CallbackQuery):
    await c_query.answer("  Генерирую меню для здоровых и сильных...  ")
    await sport(c_query.message)

async def sport(message: types.Message):
    os.chdir("database\sport_food")
    try:
        day_menu_msg = "\n".join(choose_decs()).split("|")
        for i in day_menu_msg:
            await message.answer(i)
        await message.reply_sticker(sticker='CAACAgIAAxkBAAELprRl7MZSsWaGbSPGwomhkuKIoVmgCQACMgoAAm4y2AAB_W-265DwO000BA')
    except Exception as Ex:
        await message.answer("Похоже что-то пошло не так, вероятнее всего база данных не обновлена, пробую обновиться...")
        logging.info(Ex)
    os.chdir("../..")
    logging.info(f"Received sport command")
    

@dp.message_handler(text="📆 Сгенерировать меню на неделю") #повторить все то же что и в генерации на день, только умножить на 7 дней
async def generate_week_menu(message: types.Message):
    kb_inline = types.InlineKeyboardMarkup(row_width=1)
    random_gen = types.InlineKeyboardButton("🔀 Рандомная генерация", callback_data="generate_random_week")
    option_gen = types.InlineKeyboardButton("📝 Выборочная генерация", callback_data="generate_optionally_week")
    kb_inline.add(*[random_gen, option_gen])
    await message.reply('🔀 Нажмите на кнопку "Рандомная генерация", чтобы получить случайное меню на неделю. 🍽️ \n\n📝 Выберите опцию "Выборочная генерация", чтобы получить меню, специально подобранное для конкретного типа питания или диеты. 🥗', reply_markup=kb_inline)
    
@dp.callback_query_handler(lambda q: q.data == "generate_random_week")
async def clb(cquery: types.CallbackQuery):
    await cquery.answer("  Генерирую рандомное меню...  ")
    await random_week(cquery.message)
    
@dp.callback_query_handler(lambda q: q.data == "generate_optionally_week")
async def clb2(cq: types.Message):
    await opt_week(cq.message)
    
async def opt_week(msg: types.Message):
    kb = types.ReplyKeyboardRemove()
    kb_alot = types.InlineKeyboardMarkup()
    sport_but = types.KeyboardButton("Спортивное питание", callback_data='sport_but_week')
    right_but = types.KeyboardButton("Правильное питание", callback_data='right_but_week')
    kb_alot.add(*[sport_but, right_but])
    await msg.reply("Выберите подходящую кнопку --", reply_markup=kb_alot)
    logging.info("Received generate_optionally_week command")
    
@dp.callback_query_handler(lambda q: q.data == "sport_but_week")
async def call_sport(c: types.CallbackQuery):
    await c.answer("  Генерирую недельное меню спортсмена...  ")
    await week_sport(c.message)
    
async def week_sport(msg: types.Message):
    if os.path.exists("./database/sport_food"):
        os.chdir("./database/sport_food")
    else:
        raise FileExistsError("Wrong Folder!")
    menu = "".join(choose_week()).split("|")
    for i in menu:
        await msg.answer(i)
    await msg.answer("Спортивное меню сгенерировано!")
    await msg.reply_sticker(sticker='CAACAgIAAxkBAAELprJl7MUMdRju1O54rKwzFbI0g-BtWgACugADmY-lBwojZMP_GhdkNAQ')
    os.chdir("../..")
    logging.info("Received sport_week_gen command!")
    
@dp.callback_query_handler(lambda q: q.data == "right_but_week")
async def call_right(c: types.CallbackQuery):
    await c.answer("  Генерирую правильное недельное меню...  ")
    await week_right(c.message)
    
async def week_right(msg: types.Message):
    os.chdir("./database/healthy_food")
    menu = "".join(choose_week()).split("|")
    for i in menu:
        await msg.answer(i)
    await msg.answer("Правильное меню сгенерировано!")
    await msg.answer_sticker(sticker='CAACAgUAAxkBAAELprZl7MkBNMUf5GPuT-9iB071X1sb5QACNBAAAnE13ALftpkhnzLlzjQE')
    os.chdir("../..")
    
async def random_week(msg: types.Message):
    if os.path.exists("./database"):
        os.chdir("./database")
    lst = "".join(choose_week()).split("|")
    
    for elem in lst:
        await msg.answer(elem)
    logging.info("received random_gen_week cmd")
    os.chdir("..")


@dp.message_handler(content_types=types.ContentType.ANY, commands=None)
async def handle_message(message: types.Message):
    await message.answer("Я вас не понимаю, пожалуйста введите одну из команд, либо /start")
    


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
#🔀 Нажмите на кнопку "Рандомная генерация", чтобы получить случайное меню на сегодня. 🍽️\n\n📝 Выберите опцию "Выборочная генерация", чтобы получить меню, специально подобранное для конкретного типа питания или диеты. 🥗