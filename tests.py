"""Модуль тестов"""
import pytest
import os
import json
from models import Task, TaskManager



@pytest.fixture
def task_manager():
    """Создаёт новый экземпляр TaskManager перед каждым тестом"""
    return TaskManager()


@pytest.fixture
def temp_data_file(tmp_path):
    """Создаёт временный файл для тестов сохранения/загрузки данных"""
    return tmp_path / "test_data.json"


def test_add_task(task_manager):
    """Проверка добавления задачи"""
    task_manager.add_task(
        title="Тестовая задача",
        desc="Это просто тестовая задача",
        category="Тестирование",
        due_date="2024-12-31",
        priority="Высокий"
    )
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Тестовая задача"
    assert task_manager.tasks[0].status == "Не выполнена"


def test_get_current_tasks(task_manager):
    """Проверка получения текущих задач"""
    task_manager.add_task(
        title="Невыполненная задача",
        desc="Это текущая задача",
        category="Текущие",
        due_date="2024-12-31",
        priority="Низкий"
    )
    task_manager.add_task(
        title="Выполненная задача",
        desc="Об этой задаче можно забыть",
        category="Готовые",
        due_date="2024-12-31",
        priority="Низкий"
    )
    task_manager.tasks[2].status = "Выполнена"
    pending_tasks = task_manager.get_current_tasks()
    assert len(pending_tasks) == 2
    assert pending_tasks[1].title == "Невыполненная задача"


def test_get_tasks_by_category(task_manager):
    """Проверка поиска по категории"""
    task_manager.add_task(
        title="Задача категории А",
        desc="Принадлежит категории А",
        category="А",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(
        title="Задача категории Б",
        desc="Принадлежит категории Б",
        category="Б",
        due_date="2024-12-31",
        priority="Средний"
    )
    category_a_tasks = task_manager.get_tasks_by_category("Б")
    assert len(category_a_tasks) == 1
    assert category_a_tasks[0].category == "Б"


def test_delete_task(task_manager):
    """Проверка удаления задачи"""
    
    task_to_delete: Task = task_manager.add_task(
        title="Удаляемая задача",
        desc="Эту задачу нужно удалить",
        category="Удаление",
        due_date="2024-12-31",
        priority="Низкий"
    )
    task_manager.add_task(
        title="Оставляемая задача",
        desc="Эту задачу нельзя удалять",
        category="Удаление",
        due_date="2024-12-31",
        priority="Средний"
    )
    
    task_manager.delete_task(task_to_delete.id)
    
    assert len(task_manager.tasks) == 6
    assert task_manager.tasks[5].title == "Оставляемая задача"
