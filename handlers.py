import config
import server
import kb
from aiogram import F, Router, types, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from states import DialogsState


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


router = Router()
bot = Bot(token=config.BOT_TOKEN)


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(text="Добро пожаловать в планировщик задач для команды студентов!\n\n <b>Что ты хочешь сделать?</b>", reply_markup=kb.menu)

@router.callback_query(F.data == "add_task")
async def add_task_dialog(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text="Напиши задачу и сервер подберёт подходящее время и студентов для выполнения ✨")
    await state.set_state(DialogsState.add_task)

@router.message(DialogsState.add_task)
async def add_task(msg: Message, state: FSMContext):
    await msg.answer(server.add_task(msg.text), reply_markup=kb.menu)
    await state.clear()

@router.callback_query(F.data == "list_tasks")
async def list_tasks_dialog(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(text="Задачи какого студента вывести? 👤", reply_markup=kb.names)
    await state.set_state(DialogsState.choose_student)

@router.callback_query(DialogsState.choose_student)
async def add_task(clbck: CallbackQuery, state: FSMContext):
    tasks = []
    for task in (server.list_tasks(clbck.data)): tasks.append([InlineKeyboardButton(text="❌ " + task, callback_data=task)])
    tasks = InlineKeyboardMarkup(inline_keyboard=tasks)
    await clbck.message.answer(f'список задач для <b>{clbck.data}</b> 👤\nНажмите на задачу, чтобы удалить её 🚮', reply_markup=tasks)
    await state.set_state(DialogsState.remove_task)

@router.callback_query(DialogsState.remove_task)
async def remove_task(clbck: Message, state: FSMContext):
    await clbck.message.answer(server.remove_task(clbck.data), reply_markup=kb.menu)
    await state.clear()