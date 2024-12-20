import pytest
from http import HTTPStatus
from pydantic import ValidationError

from src.schemas.comments import CommentsSchema


@pytest.mark.parametrize("comment_id, expected_status", [
    (1, HTTPStatus.OK),  # Комментарий существует
    (2, HTTPStatus.OK),  # Комментарий существует
    (9999, HTTPStatus.NOT_FOUND)  # Комментария не существует
])
def test_get_comment(comments_api, comment_id, expected_status):
    """
    Тест на получения комментария(положительные и негативные сценарии)
    """
    response = comments_api.get_comment(comment_id)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            comment_data = CommentsSchema(**response.json())
            assert comment_data.id == comment_id
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("new_comment, expected_status", [
    ({"name": "Test Comment", "email": "test@example.com", "body": "This is a test comment.", "postId": 1},
     HTTPStatus.CREATED),  # Успешное создание
    ({}, HTTPStatus.BAD_REQUEST),  # Пустое тело
    ({"name": "Test Comment"}, HTTPStatus.BAD_REQUEST)  # Неполные данные
])
def test_create_comment(comments_api, new_comment, expected_status):
    """
    Тест на создание комментария (положительные и негативные сценарии)
    """
    response = comments_api.create_comment(new_comment)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.CREATED:
        try:
            comment_data = CommentsSchema(**response.json())
            assert comment_data.name == new_comment['name']
            assert comment_data.email == new_comment['email']
            assert comment_data.body == new_comment['body']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("comment_id, updated_comment, expected_status", [
    (1, {"id": 1, "name": "Updated Comment", "email": "updated@example.com", "body": "Updated body", "postId": 1},
     HTTPStatus.OK),  # Успешное обновление
    (9999, {"id": 9999, "name": "Updated Comment", "email": "updated@example.com", "body": "Updated body", "postId": 1},
     HTTPStatus.NOT_FOUND),  # Комментария нет
    (1, {}, HTTPStatus.BAD_REQUEST)  # Пустое тело запроса
])
def test_update_comment(comments_api, comment_id, updated_comment, expected_status):
    """
    Тест на обновление комментария (положительные и негативные тесты
    """
    response = comments_api.update_comment(comment_id, updated_comment)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            comment_data = CommentsSchema(**response.json())
            assert comment_data.name == updated_comment['name']
            assert comment_data.email == updated_comment['email']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("comment_id, expected_status", [
    (1, HTTPStatus.OK),  # Успешное удаление
    (9999, HTTPStatus.BAD_REQUEST)
])
def test_comment_delete(comments_api, comment_id, expected_status):
    """
    Тест на удаление комментария (положительные и отрицательные тесты)
    """
    response = comments_api.delete_comment(comment_id)
    assert response.status_code == expected_status
