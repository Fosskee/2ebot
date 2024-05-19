import server

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="➕ Добавить задачу", callback_data="add_task")],
    [InlineKeyboardButton(text="📃 Просмотреть список задач", callback_data="list_tasks")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

names = []
for name in (server.read_roles().keys()): names.append([InlineKeyboardButton(text=name, callback_data=name)])
names = InlineKeyboardMarkup(inline_keyboard=names)
