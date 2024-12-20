import pytest
from http import HTTPStatus

from pydantic import ValidationError
from src.schemas.todos import TodoSchema


@pytest.mark.parametrize("todo_id, expected_status", [
    (1, HTTPStatus.OK),  # Задача существует
    (2, HTTPStatus.OK),  # Задача существует
    (9999, HTTPStatus.NOT_FOUND)  # Задачи не существует
])
def test_get_todo(todo_api, todo_id, expected_status):
    """
    Тест на получение задачи(положительные и негативные сценарии)
    """
    response = todo_api.get_todos(todo_id)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            todo_data = TodoSchema(**response.json())
            assert todo_data.id == todo_id
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("new_todo, expected_status", [
    ({"title": "New Task", "completed": False, "userId": 1}, HTTPStatus.CREATED),  # Успешное создание
    ({}, HTTPStatus.BAD_REQUEST),  # Пустое тело
    ({"title": "New Task"}, HTTPStatus.BAD_REQUEST)  # Неполные данные
])
def test_create_todo(todo_api, new_todo, expected_status):
    """
    Тест на создание задач(позитивные и негативные сценарии)
    """
    response = todo_api.create_todos(new_todo)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.CREATED:
        try:
            todo_data = TodoSchema(**response.json())
            assert todo_data.title == new_todo['title']
            assert todo_data.completed == new_todo['completed']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("todo_id, updated_todo, expected_status", [
    (1, {"id": 1, "title": "Updated Task", "completed": True, "userId": 1}, HTTPStatus.OK),  # Успешное обновление
    (9999, {"id": 9999, "title": "Updated Task", "completed": True, "userId": 1}, HTTPStatus.NOT_FOUND),
    # Задача не существует
    (1, {}, HTTPStatus.BAD_REQUEST)  # Пустое тело запроса
])
def test_updated_todo(todo_api, todo_id, updated_todo, expected_status):
    """
    Тест на обновление задачи(позитивные и негативные сценарии)
    """
    response = todo_api.updated_todos(todo_id, updated_todo)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            todo_data = TodoSchema(**response.json())
            assert todo_data.title == updated_todo['title']
            assert todo_data.completed == updated_todo['completed']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("todo_id, expected_status", [
    (1, HTTPStatus.OK),  # Успешно удалён
    (9999, HTTPStatus.NOT_FOUND)  # Не существует
])
def test_delete_todo(todo_api, todo_id, expected_status):
    """
    Тест на удаление задачи(позитивные и негативные сценарии)
    """
    response = todo_api.delete_todos(todo_id)
    assert response.status_code == expected_status
