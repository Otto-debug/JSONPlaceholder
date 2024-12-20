import pytest
from http import HTTPStatus
from pydantic import ValidationError

from src.schemas.post import PostSchema

@pytest.mark.parametrize("post_id, expected_status",
                         [
                             (1, HTTPStatus.OK), # Пост существует
                             (2, HTTPStatus.OK), # Пост существует
                             (9999, HTTPStatus.NOT_FOUND) # Пост не существует
                         ])
def test_get_post(posts_api, post_id, expected_status):
    """
    Тест на получение поста(позитивные и негативные сценарии)
    """
    response = posts_api.get_posts(post_id)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            post_data = PostSchema(**response.json())
            assert post_data.id == post_id
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("new_post, expected_status", [
    ({"title": "foo", "body": "bar", "userId": 1}, HTTPStatus.CREATED), # Успешное создание
    ({}, HTTPStatus.BAD_REQUEST),                                      # Пустое тело
    ({"title": "foo"}, HTTPStatus.BAD_REQUEST)                         # Не хватает обязательных полей
])
def test_create_post(posts_api, new_post, expected_status):
    """
    Тест на создание поста(позитивны и негативные сценарии)
    """
    response = posts_api.create_post(new_post)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.CREATED:
        try:
            post_data = PostSchema(**response.json())
            assert post_data.title == new_post['title']
            assert post_data.body == new_post['body']
            assert post_data.userId == new_post['userId']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")

@pytest.mark.parametrize("post_id, updated_post, expected_status",[
    (1, {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}, HTTPStatus.OK), # Успешное обновление
    (9999, {"id": 9999, "title": "updated title", "body": "updated body", "userId": 9999}, HTTPStatus.NOT_FOUND), # Поле не найдено
    (1, {}, HTTPStatus.BAD_REQUEST) # Пустое тело запроса
])
def test_update_post(posts_api, post_id, updated_post, expected_status):
    """
    Тест на обновление поста(позитивные и негативные сценарии)
    """
    response = posts_api.update_post(post_id, updated_post)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            post_data = PostSchema(**response.json())
            assert post_data.title == updated_post['title']
            assert post_data.body == updated_post['body']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")

@pytest.mark.parametrize("post_id, expected_status",[
    (1, HTTPStatus.OK), # Успешное удаление
    (9999, HTTPStatus.NOT_FOUND) # Пост отсутствует
])
def test_delete_post(posts_api, post_id, expected_status):
    """
    Тест на удаление поста(позитивные и негативные сценарии)
    """
    response = posts_api.delete(post_id)
    assert response.status_code == expected_status



























