from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выгрузить пользователей", callback_data='reload-users'),
            InlineKeyboardButton(text="Отправить сообщение пользователям", callback_data='send_message_to_users')
        ],
])

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Возврат в админ панель", callback_data='back_to_admin'),
        ],
])

xlsx = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отправить файл", callback_data='send_xlsx'),
        ],
])
