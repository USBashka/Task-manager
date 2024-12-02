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
            print( "┌──────┬────╼")
            print(f"│      │ {Style.B}{task.title}{RESET}")
            print(f"│      │ {task.description}")
            print(f"│{t_id}│ Категория: {task.category}")
            print(f"│      │ Дедлайн: {task.due_date}")
            print(f"│      │ Приоритет: {task.priority} │ Статус: {task.status}")
            print( "└──────┴───────────────────────────────────────────────────────────╼")


def get_plural(word: str, number: int) -> str:
    """Возвращает слово в указанном числе"""

    words: dict[str, list[str]] = {
        "задача": ["задачи", "задач"],
        "невыполненная": ["невыполненные", "невыполненных"],
        "найдена": ["найдено", "найдено"]
    }

    if word in words:
        if 10 < number < 20:
            return words[word][1]
        elif number % 10 == 1:
            return word
        elif 1 < number % 10 < 5:
            return words[word][0]
        else:
            return words[word][1]
    else:
        return word


def show_help() -> None:
    """Показывает доступные команды и их краткое описание"""

    print("Доступные команды (вводить можно как на английском, так и на русском):")
    for command in commands.keys():
        print(Style.B + command + RESET, commands[command], sep="\t")


def show_current(manager: TaskManager) -> None:
    """Запрашивает категорию и выводит невыполненные задачи по ней, либо по всем"""

    current_tasks: list[Task] = []
    print("По какой категории показать задачи:")
    print("0 - По всем")
    for i, c in enumerate(manager.categories, start=1):
        print(f"{i} - {c}")
    category: str = input("Категория: ").strip()
    if category:
        if category == "0" or category == "По всем":
            current_tasks = manager.get_current_tasks()
            if current_tasks:
                un_tasks: str = get_plural("невыполненная", len(current_tasks)) + " " + get_plural("задача", len(current_tasks))
                print(f"Сейчас у вас {len(current_tasks)} {un_tasks}:")
            else:
                print("Сейчас у вас нет невыполненных задач")
        elif category.isdigit():
            category_number: int = int(category)
            if category_number <= len(manager.categories):
                category = manager.categories[category_number-1]
                current_tasks = manager.get_current_tasks(category)
                if current_tasks:
                    un_tasks: str = get_plural("невыполненная", len(current_tasks)) + " " + get_plural("задача", len(current_tasks))
                    print(f"Сейчас у вас {len(current_tasks)} {un_tasks} в категории {category}:")
                else:
                    print("Сейчас у вас нет невыполненных задач в категории {category}")
            else:
                print("Такой категории нету")
        elif category in manager.categories:
            current_tasks = manager.get_current_tasks(category)
            if current_tasks:
                un_tasks: str = get_plural("невыполненная", len(current_tasks)) + " " + get_plural("задача", len(current_tasks))
                print(f"Сейчас у вас {len(current_tasks)} {un_tasks} в категории {category}:")
            else:
                print("Сейчас у вас нет невыполненных задач в категории {category}")
        else:
            print("Такой категории нету")
    else:
        current_tasks = manager.get_current_tasks()
        if current_tasks:
            un_tasks: str = get_plural("невыполненная", len(current_tasks)) + " " + get_plural("задача", len(current_tasks))
            print(f"Сейчас у вас {len(current_tasks)} {un_tasks}:")
        else:
            print("Сейчас у вас нет невыполненных задач")
        
    print_tasks(current_tasks)


def add_task(manager: TaskManager) -> None:
    """Запрашивает информацию о новой задаче и добавляет её в вистему"""

    title: str = input("Название новой задачи: ")
    if not title:
        print("Название не может быть пустым")
        return
    desc: str = input("Описание: ")
    category: str = input("Категория: ")
    due_date: str = input("Дедлайн: ")
    print("Выберите приоритет задачи:")
    print("1 - Низкий / 2 - Средний / 3 - Высокий")
    priority: str = input("Приоритет: ")
    match priority.lower().strip():
        case "1" | "низкий" | "1 - низкий":
            priority = "Низкий"
        case "2" | "средний" | "2 - средний":
            priority = "Низкий"
        case "3" | "высокий" | "3 - высокий":
            priority = "Низкий"
        case _:
            print("Недопустимое значение приоритета")
            return
    task: Task = manager.add_task(title, desc, category, due_date, priority)
    manager.save_data()
    print(f"Задача {task.title} добавлена под ID {task.id}")


def edit_task(manager: TaskManager) -> None:
    """Запрашивает ID задачи и позволяет изменить её поля"""

    task_id: str = input("ID редактируемой задачи: ")
    if task_id.isdigit():
        task: Task = manager.get_task_by_id(int(task_id))
        if task:
            print_tasks([task])
            print("Вводите новые значения полей (если не хотите изменять — оставьте пустыми)")
            new_title: str = input("Название: ")
            new_desc: str = input("Описание: ")
            new_category = input("Категория: ")
            new_due_date = input("Дедлайн: ")
            new_priority: str = input("Приоритет (1 - Низкий / 2 - Средний / 3 - Высокий): ")
            match new_priority.lower().strip():
                case "1" | "низкий" | "1 - низкий":
                    new_priority = "Низкий"
                case "2" | "средний" | "2 - средний":
                    new_priority = "Низкий"
                case "3" | "высокий" | "3 - высокий":
                    new_priority = "Низкий"
                case _:
                    new_priority = ""
            manager.edit_task(int(task_id), title=new_title, description=new_desc, category=new_category,
                              due_date=new_due_date, priority=new_priority)
            manager.save_data()
            print("Задача успешно изменена")
        else:
            print("Задачи с таким ID не найдено")
    else:
        print("ID задачи может состоять только из цифр")


def do_task(manager: TaskManager) -> None:
    """Запрашивает ID задачи и отмечает её как выполненную"""

    task_id: str = input("ID выполненной задачи: ")
    if task_id.isdigit():
        task: Task = manager.get_task_by_id(int(task_id))
        if task:
            if task.status != "Выполнена":
                task.status = "Выполнена"
                print(f"Задача {task.title} отмечена как выполненная")
            else:
                undo: str = input(f"Задача {task.title} уже выполнена. Отменить выполнение? (Да/Нет): ").lower().strip()
                match undo:
                    case "yes" | "y" | "да" | "д":
                        task.status = "Не выполнена"
                        print(f"Задача отмечена как невыполненная")
                    case _:
                        print("Хорошо, пусть всё остаётся как есть")
            manager.save_data()
        else:
            print("Задачи с таким ID не найдено")
    else:
        print("ID задачи может состоять только из цифр")


def delete_task(manager: TaskManager) -> None:
    """Запрашивает ID задачи и удаляет её"""

    task_id: str = input("ID удаляемой задачи: ")
    if task_id.isdigit():
        deleted_task: Task = manager.delete_task(int(task_id))
        if deleted_task:
            print(f"Задача {deleted_task.title} удалена")
        else:
            print("Задачи с таким ID не найдено")
    else:
        print("ID задачи может состоять только из цифр")


def find_task(manager: TaskManager) -> None:
    """Запрашивает по какому параметру искать, затем сам параметр, после чего выводит подходящие задачи"""

    print("Выберите, по какому параметру искать задачи: ")
    print("1 - Ключевые слова / 2 - Категория / 3 - Статус")
    matched_tasks: list[Task] = []
    param: str = input("Параметр поиска: ").lower().strip()
    match param:
        case "1" | "ключевые слова" | "1 - ключевые слова":
            keywords: list[str] = input("Введите ключевые слова через пробел: ").lower().strip().split(" ")
            matched_tasks = manager.get_tasks_by_keywords(keywords)
        case "2" | "категория" | "2 - категория":
            category: str = input("Введите категорию: ")
            matched_tasks = manager.get_tasks_by_category(category)
        case "3" | "статус" | "3 - статус":
            status: str = input("Введите статус (1 - Не выполнена / 2 - Выполнена)").lower().strip()
            match status:
                case "1" | "не выполнена" | "1 - не выполнена":
                    status = "Не выполнена"
                case "2" | "выполнена" | "2 выполнена":
                    status = "Выполнена"
            matched_tasks = manager.get_tasks_by_status(status)
    if matched_tasks:
        number: int = len(matched_tasks)
        print(f"{get_plural("найдена", number).capitalize()} {number} {get_plural("задача", number)}:")
        print_tasks(matched_tasks)
    else:
        print("Задач с такими параметрами не найдено")


def show_list(manager: TaskManager) -> None:
    """Выводит все задачи"""

    if manager.tasks:
        print_tasks(manager.tasks)
    else:
        print("Вы ещё не добавили ни одной задачи. Используйте команду \"добавить\"")


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
        print(f"{Color.RED}{Style.B}{e}{RESET}")



if __name__ == "__main__":
    main()