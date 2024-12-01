"""Главный модуль приложения"""
from models import Task, TaskManager
from formatting import Color, Style, RESET



commands: dict[str, str] = {
    "help / помощь": "Вывести список команд",
    "current / тек": "Показать невыполненные задачи",
    "add / добавить": "Создать новую задачу",
    "edit / ред": "Изменить задачу",
    "do / выполнить": "Отметить, что задача выполнена",
    "del / удалить": "Удалить задачу",
    "find / найти": "Найти задачу по ключевым словам, категории или статусу",
    "list / список": "Показать все задачи",
    "exit / выход": "Завершить работу приложения"
}



def print_tasks(tasks: list[Task]) -> None:
    """Выводит задачи в виде красивой таблицы или списка карточек, если задач меньше трёх"""

    if len(tasks) > 2:
        print(f"{Style.B}  ID  │           Название           │   Категория   │  Дедлайн  │ Приоритет │   Статус   {RESET}")
        print(          "──────┼──────────────────────────────┼───────────────┼───────────┼───────────┼────────────")
        for task in tasks:
            print(
                str(task.id).rjust(6),
                task.title.center(30),
                task.category.center(15),
                task.due_date.center(11),
                task.priority.center(11),
                task.status.center(12),
                sep="│"
            )
    else:
        for task in tasks:
            t_id: str = str(task.id).center(6)
            print(f"┌──────┬────╼")
            print(f"│      │ {Style.B}{task.title}{RESET}")
            print(f"│      │ {task.description}")
            print(f"│{t_id}│ Категория: {task.category}")
            print(f"│      │ Дедлайн: {task.due_date}")
            print(f"│      │ Приоритет: {task.priority} │ Статус: {task.status}")
            print(f"└──────┴───────────────────────────────────────────────────────────╼")



def show_current(manager: TaskManager) -> None:
    """Запрашивает категорию и выводит невыполненные задачи по ней, либо по всем"""

    print("По какой категории показать задачи:")
    print("0 - По всем")
    for i, c in enumerate(manager.categories, start=1):
        print(f"{i} - {c}")
    current_tasks: list[Task] = manager.get_current_tasks()
    print_tasks(current_tasks)


def show_help() -> None:
    """Показывает доступные команды и их краткое описание"""

    print("Доступные команды (вводить можно как на английском, так и на русском):")
    for command in commands.keys():
        print(Style.B + command + RESET, commands[command], sep="\t")


def main() -> None:
    """Точка входа"""

    print("Добро пожаловать в менеджер задач \"Tasker\"")
    tasker = TaskManager()
    tasker.load_data()
    print("Для просмотра всех команд введите \"помощь\"")

    try:
        while True:
            command: str = input(f"> {Color.YELLOW}")
            print(RESET, end="")
            match command.lower().strip():
                case "help" | "помощь":
                    show_help()
                case "current" | "тек":
                    show_current(tasker)
                case "add" | "добавить":
                    add_task(tasker)
                case "edit" | "ред":
                    edit_task(tasker)
                case "do" | "выполнить":
                    do_task(tasker)
                case "del" | "удалить":
                    delete_task(tasker)
                case "find" | "найти":
                    find_task(tasker)
                case "list" | "список":
                    show_list(tasker)
                case "exit" | "выход":
                    print("До свидания!")
                    break
                case _:
                    print(f"{Color.RED}Такой команды не существует{RESET}")
    
    except (EOFError, KeyboardInterrupt):
        print(f"{RESET}До свидания!")
    except Exception as e:
        print(f"{Color.RED}{Style.B}e{RESET}")



if __name__ == "__main__":
    main()