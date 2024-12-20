import pytest
from http import HTTPStatus

from pydantic import ValidationError
from src.schemas.user import UserSchema


@pytest.mark.parametrize("user_id, expected_status", [
    (1, HTTPStatus.OK),  # Пользователь существует
    (2, HTTPStatus.OK),  # Пользователь существует
    (9999, HTTPStatus.NOT_FOUND)  # Пользователя не существует
])
def test_get_user(user_api, user_id, expected_status):
    """
    Тест на получения пользователя(положительные и негативные сценарии)
    """
    response = user_api.get_user(user_id)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            user_data = UserSchema(**response.json())
            assert user_data.id == user_id
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("new_user, expected_status", [
    ({
         "name": "Otto Debug",
         "username": "otto-debug",
         "email": "otto@example.com",
         "address": {"street": "Main St", "suite": "Apt 1", "city": "New-York", "zipcode": "12345"},
         "phone": "555-1234",
         "website": "example.com",
         "company": {"name": "Test Corp", "catchPhrase": "Innovate Everything", "bs": "synergy solutions"}
     }, HTTPStatus.CREATED),  # Успешное создание
    ({}, HTTPStatus.BAD_REQUEST),  # Пустое тело
    ({"name": "Otto Debug"}, HTTPStatus.BAD_REQUEST)  # Неполные данные
])
def test_create_user(user_api, new_user, expected_status):
    """
    Тест на создание пользователя(позитивные и негативные сценарии)
    """
    response = user_api.create_user(new_user)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.CREATED:
        try:
            user_data = UserSchema(**response.json())
            assert user_data.name == new_user['name']
            assert user_data.email == new_user['email']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("user_id, updated_user, expected_status", [
    (1, {
        "id": 1,
        "name": "Updated Name",
        "username": "updatedusername",
        "email": "updated@example.com",
        "address": {"street": "New St", "suite": "Apt 2", "city": "New City", "zipcode": "67890"},
        "phone": "555-5678",
        "website": "newexample.com",
        "company": {"name": "Updated Corp", "catchPhrase": "Innovate More", "bs": "synergy updates"}
    }, HTTPStatus.OK),  # Успешное обновление
    (9999, {"id": 9999, "name": "Updated Name"}, HTTPStatus.NOT_FOUND),  # Пользователь не существует
    (1, {}, HTTPStatus.BAD_REQUEST)  # Пустое тело запроса
])
def test_update_user(user_api, user_id, updated_user, expected_status):
    """
    Тест на обновление пользователя(позитивные и негативные сценарии)
    """
    response = user_api.update_user(user_id, updated_user)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            user_data = UserSchema(**response.json())
            assert user_data.name == updated_user['name']
            assert user_data.email == updated_user['email']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("user_id, expected_status", [
    (1, HTTPStatus.OK),  # Успешно удалён
    (9999, HTTPStatus.NOT_FOUND)  # Пользователь не найден
])
def test_delete_user(user_api, user_id, expected_status):
    """
    Тест на удаление пользователя(положительный и негативный сценарий)
    """
    response = user_api.delete_user(user_id)
    assert response.status_code == expected_status
