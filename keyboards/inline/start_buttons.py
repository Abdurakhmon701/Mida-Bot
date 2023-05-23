from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import GROUP

start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подобрать группу", callback_data='choose_groups'),
            InlineKeyboardButton(text="Список групп", callback_data='groups_list')
        ],
])

groups = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Психология", callback_data='psychology'),
            InlineKeyboardButton(text="Криптовалюта", callback_data='krypto'),
            InlineKeyboardButton(text="Стартапы", callback_data='startups'),
        ],
])

psycho_answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data='da_1'),
            InlineKeyboardButton(text="Нет", callback_data='net_1'),
        ],
])

crypto_answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data='da_2'),
            InlineKeyboardButton(text="Нет", callback_data='net_2'),
        ],
])

startup_answer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data='da_3'),
            InlineKeyboardButton(text="Нет", callback_data='net_3'),
        ],
])

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Вернуться в меню", callback_data='main_menu'),
        ],
])

groups_lists = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Психология", url=f"{GROUP}"),
            InlineKeyboardButton(text="Криптовалюта", url=f"{GROUP}"),
            InlineKeyboardButton(text="Стартапы", url=f"{GROUP}"),
        ],
])




