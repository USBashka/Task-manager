<img align="left" width="64" height="64" src="https://github.com/user-attachments/assets/c770e217-01ea-47b6-9cd6-7bca2252a831">

# Tasker [![Python 3](https://img.shields.io/badge/Python_3-2A5370?logo=python&logoColor=white)](https://python.org)

Tasker — это консольный менеджер задач. С его помощью можно создавать задачи с различными категориями, устанавливать им
уровни приоритета и отмечать их выполнение. Задачи автоматически сохраняются в JSON-файле, и загружаются из него при
старте приложения.

| Данный проект является тестовым заданием на вакансию Junior Python Developer в компанию Хайталент |
|---------------------------------------------------------------------------------------------------|


## Установка и запуск
Склонируйте репозиторий:
```sh
git clone https://github.com/USBashka/Task-manager
```
Перейдите в директорию проекта:
```sh
cd Task-manager
```
Запустите файл `main.py`:
```sh
python main.py
```

## Использование
Всё взаимодействие с приложением происходит через консоль. Всего есть 9 команд:

### Помощь
Выводит все команды
```
Добро пожаловать в менеджер задач "Tasker"
Для просмотра всех команд введите "помощь"
> помощь
Доступные команды (вводить можно как на английском, так и на русском):
help / помощь   Вывести список команд
current / тек   Показать невыполненные задачи
add / добавить  Создать новую задачу
edit / ред      Изменить задачу
do / выполнить  Отметить, что задача выполнена
del / удалить   Удалить задачу
find / найти    Найти задачу по ключевым словам, категории или статусу
list / список   Показать все задачи
exit / выход    Завершить работу приложения
```

### Тек
Выводит невыполненные задачи
```
> тек
По какой категории показать задачи:
0 - По всем
1 - Обучение
2 - Геймдев
3 - Работа
Категория: 0
Сейчас у вас 4 невыполненные задачи:
  ID  │           Название           │   Категория   │  Дедлайн  │ Приоритет │   Статус   
──────┼──────────────────────────────┼───────────────┼───────────┼───────────┼────────────
     1│    Изучить основы FastAPI    │    Обучение   │ 2024-11-30│   Низкий  │Не выполнена
     2│    Сделать игру Invertale    │    Геймдев    │ Бессрочно │   Низкий  │Не выполнена
     3│         Изучить SQL          │    Обучение   │ 2024-12-10│   Низкий  │Не выполнена
     4│  Сделать GPT Dataset Editor  │     Работа    │ 2025-01-01│   Низкий  │Не выполнена
```

### Добавить
Создаёт новую задачу
```
> добавить
Название новой задачи: Сделать тестовое Хайталент
Описание: Сделать тестовое задание на вакансию Junior Python Developer в Хайталент
Категория: Работа
Дедлайн: 03-12-2024
Выберите приоритет задачи:
1 - Низкий / 2 - Средний / 3 - Высокий
Приоритет: 3
Задача Сделать тестовое Хайталент добавлена под ID 5
```

### Ред
Запрашивает ID задачи и позволяет отредактировать её
```
> ред
ID редактируемой задачи: 2
┌──────┬────╼
│      │ Сделать игру Invertale
│      │ Сделать фан-игру на Годоте
│  2   │ Категория: Геймдев
│      │ Дедлайн: Бессрочно
│      │ Приоритет: Низкий │ Статус: Не выполнена
└──────┴───────────────────────────────────────────────────────────╼
Вводите новые значения полей (если не хотите изменять — оставьте пустыми)
Название:
Описание:
Категория:
Дедлайн: 2025-05-31
Приоритет (1 - Низкий / 2 - Средний / 3 - Высокий):
Задача успешно изменена
```

### Выполнить
Запрашивает ID задачи и отмечает её как выполненную. Если она уже выполнена, позволяет отменить выполнение
```
> выполнить
ID выполненной задачи: 5
Задача Сделать тестовое Хайталент отмечена как выполненная
```

### Удалить
Запрашивает ID задачи и удаляет её
```
> удалить
ID удаляемой задачи: 1
Задача Изучить основы FastAPI удалена
```

### Найти
Запрашивает по какому параметру искать, затем сам параметр, после чего выводит найденые задачи
```
> найти
Выберите, по какому параметру искать задачи:
1 - Ключевые слова / 2 - Категория / 3 - Статус
Параметр поиска: 1
Введите ключевые слова через пробел: годот
Найдено 2 задачи:
┌──────┬────╼
│      │ Сделать игру Invertale
│      │ Сделать фан-игру на Годоте
│  2   │ Категория: Геймдев
│      │ Дедлайн: 2025-05-31
│      │ Приоритет: Низкий │ Статус: Не выполнена
└──────┴───────────────────────────────────────────────────────────╼
┌──────┬────╼
│      │ Сделать GPT Dataset Editor
│      │ Сделать редактор датасетов для файнтюна GPT на Годоте
│  4   │ Категория: Работа
│      │ Дедлайн: 2025-01-01
│      │ Приоритет: Низкий │ Статус: Не выполнена
└──────┴───────────────────────────────────────────────────────────╼
```

### Список
Выводит все задачи
```
> список
  ID  │           Название           │   Категория   │  Дедлайн  │ Приоритет │   Статус   
──────┼──────────────────────────────┼───────────────┼───────────┼───────────┼────────────
     2│    Сделать игру Invertale    │    Геймдев    │ 2025-05-31│   Низкий  │Не выполнена
     3│         Изучить SQL          │    Обучение   │ 2024-12-10│  Средний  │Не выполнена
     4│  Сделать GPT Dataset Editor  │     Работа    │ 2025-01-01│   Низкий  │Не выполнена
     5│  Сделать тестовое Хайталент  │     Работа    │ 2024-12-03│  Высокий  │ Выполнена
```

### Выход
Завершает работу приложения

## Тестирование
Реализовано тестирование с помощью pytest. Для запуска тестов, находясь в директории проекта, используйте команду:
```
pytest tests.py
```
