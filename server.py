from typing import List, Dict



def add_task(task: str) -> str:
    answer = f'''\tЗадача
<b>{task}</b>
успешно добавлена!✔️'''
    return answer


def remove_task(task: str):
    answer = f'''\tЗадача
<b>{task}</b>
успешно удалена!🚮'''
    return answer


def read_roles() -> Dict[str, str]:

    roles = {
        'Petr' : 'loves kitchen chores',
        'Nastya' : 'loves cooking',
        'Alex' : 'lazy person'
        }
    return roles


def list_tasks(name: str) -> List[str]:
    tasks = ['Clean the bathroom']
    return tasks