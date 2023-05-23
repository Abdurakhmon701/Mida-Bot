from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS
from keyboards.inline.admin_buttons import admin_menu, admin_panel


from states.states_for_admin import MessageState

from utils.db_api.convert import db_to_xlsx

# Проверка Админа
@dp.message_handler(Command('admin'), state="*")
async def chat_admin(message: Message, state: FSMContext):
    for admin in ADMINS:
        if message.from_user.id == int(admin):
            await message.answer(f"Выберите опцию:", reply_markup=admin_menu)
        else:
            await message.answer("Вам нет доступа к этому раздела!")
    await MessageState.first.set()

# Отправка сообщения всем пользователям в БД, вводите с клавиатуры сообщение и оно рассылается всем пользователям
@dp.callback_query_handler(text="send_message_to_users",state=MessageState.first)
async def choose_groups(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите сообщение: ")
    await MessageState.second.set()

@dp.message_handler(state=MessageState.second)
async def choose_groups(message: Message, state: FSMContext):
    message_for_users = message.text
    users = db.select_all_users()
    for i in users:
        user = i[2]
        await bot.send_message(chat_id=user, text=message_for_users, reply_markup=admin_panel)
    await state.finish()
# Назад в главное в меню
@dp.callback_query_handler(text="back_to_admin", state="*")
async def choose_groups(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text="Выберите опцию:", reply_markup=admin_menu)

# Создание и отправка таблица в личку админа
@dp.callback_query_handler(text="reload-users", state="*")
async def send_file_callback(call: CallbackQuery):
    db_name = 'users.db'
    table_name = 'users'
    db_to_xlsx(db_name, table_name) # Создание таблицы .xlsx
    for admin in ADMINS:
        with open('users.xlsx', 'rb') as file:
            await bot.send_document(chat_id=admin, document=file)
            await call.message.answer(text="Успешно!", reply_markup=admin_panel)


