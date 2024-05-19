from aiogram.fsm.state import StatesGroup, State

class DialogsState(StatesGroup):
    add_task = State()
    choose_student = State()
    remove_task = State()
