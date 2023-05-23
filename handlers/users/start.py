from loader import dp, db

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.inline.start_buttons import start_menu, groups, psycho_answer, crypto_answer, startup_answer, groups_lists, main_menu
from data.config import GROUP


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: Message):
    data_base = db.select_id(message.from_user.id)
    if data_base == []:
        db.add_users_to_db(message.from_user.first_name, message.from_user.id)
    await message.answer(f"Привет! Я бот который поможет тебе выбрать группу по твоим интересам", reply_markup=start_menu)

# Здесь функции-опросы, которые дают ссылки на группы:
@dp.callback_query_handler(text="groups_list", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer("Группы: ", reply_markup=groups_lists)


@dp.callback_query_handler(text="choose_groups", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer("Чем вы интересуетесь?", reply_markup=groups)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@dp.callback_query_handler(text="psychology", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer("Вы психолог?", reply_markup=psycho_answer)

@dp.callback_query_handler(text="da_1", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Ссылка на чат: {GROUP}", reply_markup=main_menu)

@dp.callback_query_handler(text="net_1", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Ссылка на чат: {GROUP}", reply_markup=main_menu)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@dp.callback_query_handler(text="krypto", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer("Вы торгуете криптовалютой?", reply_markup=crypto_answer)

@dp.callback_query_handler(text="da_2", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Ссылка на чат: {GROUP}", reply_markup=main_menu)

@dp.callback_query_handler(text="net_2", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Ссылка на чат: {GROUP}", reply_markup=main_menu)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@dp.callback_query_handler(text="startups", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer("Вы создаете стартап?", reply_markup=startup_answer)

@dp.callback_query_handler(text="da_3", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Ссылка на чат: {GROUP}", reply_markup=main_menu)

@dp.callback_query_handler(text="net_3", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Ссылка на чат: {GROUP}", reply_markup=main_menu)

# Главный меню
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@dp.callback_query_handler(text="main_menu", state="*")
async def choose_groups(call: CallbackQuery):
    await call.message.answer(f"Привет! Я бот который поможет тебе выбрать группу по твоим интересам", reply_markup=start_menu)





