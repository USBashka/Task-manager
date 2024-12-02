"""Основные классы приложения"""
from dataclasses import dataclass, asdict
import json

from formatting import Color, Style, RESET

    

@dataclass
class Task:
    """Класс задачи"""

    id: int  # Уникальный идентификатор
    title: str  # Название
    description: str  # Описание
    category: str  # Категория
    due_date: str  # Срок выполнения в свободном формате
    priority: str  # Приоритет (Низкий/Средний/Высокий)
    status: str  # Статус (Выполнена/Не выполнена)


class TaskManager:
    """Класс менеджера"""

    DATA_PATH: str = "data.json"

    last_id: int = 0  # ID последней добавленной задачи
    categories: list[str] = []  # Все категории
    tasks: list[Task] = []  # Список задач

    def save_data(self, path: str = DATA_PATH) -> None:
        """Сохраняет базу в указанный JSON-файл"""

        try:
            data: dict = {
                "last_id": self.last_id,
                "categories": self.categories,
                "tasks": [asdict(task) for task in self.tasks]
            }
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"{Color.RED}{Style.B}Ошибка сохранения: {e}{RESET}")
    
    def load_data(self, path = DATA_PATH) -> None:
        """Загружает базу из указанного файла"""

        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.last_id = data["last_id"]
            self.categories = data["categories"]
            self.tasks = [Task(**task) for task in data["tasks"]]
        except FileNotFoundError:
            pass  # Если файла пока нет — ничего страшного
        except Exception as e:
            print(f"{Color.RED}{Style.B}Ошибка загрузки: {e}{RESET}")
    
    def get_current_tasks(self, category: str = "") -> list[Task]:
        """Возвращает все не выполненные задачи с указанной категорией"""

        matched_tasks: list[Task] = []
        current_tasks: list[Task] = []

        if category:
            matched_tasks = self.get_tasks_by_category(category)
        else:
            matched_tasks = self.tasks
        
        for task in matched_tasks:
            if task.status == "Не выполнена":
                current_tasks.append(task)
        return current_tasks
    
    def add_task(self, title: str, desc: str, category: str, due_date: str, priority: str) -> Task:
        """Добавляет новую задачу"""

        task: Task = Task(self.last_id+1, title, desc, category, due_date, priority, "Не выполнена")
        self.last_id += 1
        self.tasks.append(task)
        if category not in self.categories:
            self.categories.append(category)
        return task
    
    def edit_task(self, id: int, **kwargs) -> Task:
        """Редактирует задачу, меняя указанные поля"""

        task: Task = self.get_task_by_id(id)
        old_category: str
        if task:
            if "category" in kwargs:
                old_category = task.category
                if kwargs["category"] not in self.categories:
                    self.categories.append(kwargs["category"])
            
            for kwarg in kwargs:
                if kwargs[kwarg]:
                    setattr(task, kwarg, kwargs[kwarg])
            
            if old_category and not self.get_tasks_by_category(old_category):
                self.categories.pop(self.categories.index(old_category))
            return task

    def delete_task(self, id: int) -> Task | None:
        """Удаляет задачу"""

        for i, t in enumerate(self.tasks):
            if t.id == id:
                deleted_task = self.tasks.pop(i)
                if not self.get_tasks_by_category(deleted_task.category):
                    self.categories.pop(self.categories.index(deleted_task.category))
                return deleted_task
    
    def get_tasks_by_keywords(self, keywords: list[str]) -> list[Task]:
        """Возвращает задачи, в названии или описании которых есть ключевые слова"""

        matched_tasks: list[Task] = []
        for task in self.tasks:
            for keyword in keywords:
                if keyword not in task.title.lower() and keyword not in task.description.lower():
                    break
            else:
                matched_tasks.append(task)
        return matched_tasks
    
    def get_tasks_by_category(self, category: str) -> list[Task]:
        """Возвращает задачи с указанной категорией"""

        matched_tasks: list[Task] = []
        for task in self.tasks:
            if task.category == category:
                matched_tasks.append(task)
        return matched_tasks
    
    def get_tasks_by_status(self, status: str) -> list[Task]:
        """Возвращает задачи с указанным статусом"""

        matched_tasks: list[Task] = []
        for task in self.tasks:
            if task.status == status:
                matched_tasks.append(task)
        return matched_tasks
    
    def get_task_by_id(self, id: int) -> Task | None:
        """Возвращает задачу с указанным ID"""

        for task in self.tasks:
            if task.id == id:
                return task
