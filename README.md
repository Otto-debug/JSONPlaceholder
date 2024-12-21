# Тестирование REST API JSONPlaceholder

## Обзор
Этот проект предоставляет автоматические тесты для REST API JSONPlaceholder. Он охватывает различные эндпоинты с использованием CRUD-операций, чтобы убедиться, что API работает корректно. Проект построен с учетом масштабируемости и включает в себя надёжные тестовые практики.

## Основные функции
- Тесты для эндпоинтов:
  - `/posts`
  - `/comments`
  - `/albums`
  - `/photos`
  - `/todos`
  - `/users`
- Валидация ответов API с использованием схем Pydantic.
- Детальная генерация отчётов с помощью Allure.
- Логирование для отслеживания выполнения тестов.
- Поддержка позитивных и негативных сценариев тестирования.

---

## Структура проекта

## Структура проекта

```plaintext
project/
│
├── tests/                    # Содержит тестовые случаи
│   ├── test_posts.py         # Тесты для эндпоинта /posts
│   ├── test_comments.py      # Тесты для эндпоинта /comments
│   ├── test_albums.py        # Тесты для эндпоинта /albums
│   ├── test_photos.py        # Тесты для эндпоинта /photos
│   ├── test_todos.py         # Тесты для эндпоинта /todos
│   └── test_users.py         # Тесты для эндпоинта /users
│
├── src/                      # Исходный код проекта
│   ├── api/                  # Классы для взаимодействия с API
│   │   ├── base_api.py       # Базовый класс API для общих методов
│   │   ├── posts_api.py      # Класс API для /posts
│   │   ├── comments_api.py   # Класс API для /comments
│   │   ├── albums_api.py     # Класс API для /albums
│   │   ├── photos_api.py     # Класс API для /photos
│   │   ├── todos_api.py      # Класс API для /todos
│   │   └── users_api.py      # Класс API для /users
│   └── schemas/              # Схемы валидации ответов API
│       ├── post_schema.py    # Схема для /posts
│       ├── comment_schema.py # Схема для /comments
│       ├── album_schema.py   # Схема для /albums
│       ├── photo_schema.py   # Схема для /photos
│       ├── todo_schema.py    # Схема для /todos
│       └── user_schema.py    # Схема для /users
│
├── logs/                     # Логи выполнения
│   └── ...                   # Лог-файлы
│
├── reports/                  # Отчёты Allure
│   └── ...                   # HTML-отчёты
│
├── conftest.py               # Фикстуры и конфигурации Pytest
├── README.md                 # Документация проекта
└── requirements.txt          # Зависимости Python
```

---

## Эндпоинты и операции
### Поддерживаемые операции:
- **GET**: Получение данных из API.
- **POST**: Создание новых ресурсов.
- **PUT/PATCH**: Обновление существующих ресурсов.
- **DELETE**: Удаление ресурсов.

### Примеры:
#### GET `/posts/1`
Ответ:
```json
{
    "id": 1,
    "title": "test",
    "body": "bar",
    "userId": 1
}
```

#### POST `/posts`
Запрос:
```json
{
    "title": "test",
    "body": "bar",
    "userId": 1
}
```
Ответ:
```json
{
    "id": 101,
    "title": "test",
    "body": "bar",
    "userId": 1
}
```

---

## Настройка проекта

### Предварительные требования
- Python 3.10+
- pip

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Otto-debug/JSONPlaceholder.git
   cd JSONPlaceholder
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

---

## Запуск тестов
### Запуск всех тестов:
```bash
pytest tests/ --alluredir=reports/
```

### Генерация отчёта Allure:
```bash
allure serve reports/
```
