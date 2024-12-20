import pytest

from http import HTTPStatus
from pydantic import ValidationError
from src.schemas.photos import PhotoSchema


@pytest.mark.parametrize("photo_id, expected_status", [
    (1, HTTPStatus.OK),  # Фото существует
    (2, HTTPStatus.OK),  # Фото существует
    (9999, HTTPStatus.NOT_FOUND)  # Фото не существует
])
def test_get_photo(photo_api, photo_id, expected_status):
    """
    Тест на возвращение фото(позитивные и негативные сценарии)
    """
    response = photo_api.get_photos(photo_id)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            photo_data = PhotoSchema(**response.json())
            assert photo_data.id == photo_id
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("new_photo, expected_status", [
    ({"title": "New Photo", "url": "http://example.com/photo.jpg", "thumbnailUrl": "http://example.com/thumbnail.jpg",
      "albumId": 1}, HTTPStatus.CREATED),  # Успешное создание
    ({}, HTTPStatus.BAD_REQUEST),  # Пустое тело
    ({"title": "New Photo"}, HTTPStatus.BAD_REQUEST)  # Неполные данные
])
def test_create_photo(photo_api, new_photo, expected_status):
    """
    Тест на создание фото(позитивные и негативные сценарии)
    """
    response = photo_api.create_photo(new_photo)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.CREATED:
        try:
            photo_data = PhotoSchema(**response.json())
            assert photo_data.title == new_photo['title']
            assert photo_data.url == new_photo['url']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")


@pytest.mark.parametrize("photo_id, updated_photo, expected_status", [
    (1, {"id": 1, "title": "Updated Photo", "url": "http://example.com/updated.jpg",
         "thumbnailUrl": "http://example.com/updated_thumbnail.jpg", "albumId": 1}, HTTPStatus.OK),
    # Успешное обновление
    (9999, {"id": 9999, "title": "Updated Photo", "url": "http://example.com/updated.jpg",
            "thumbnailUrl": "http://example.com/updated_thumbnail.jpg", "albumId": 1}, HTTPStatus.NOT_FOUND),
    # Фото не существует
    (1, {}, HTTPStatus.BAD_REQUEST)  # Пустое тело запроса
])
def test_update_photo(photo_api, photo_id, updated_photo, expected_status):
    """
    Обновление фото(позитивные и негативные сценарии)
    """
    response = photo_api.update_photo(photo_id, updated_photo)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            photo_data = PhotoSchema(**response.json())
            assert photo_data.title == updated_photo['title']
            assert photo_data.url == updated_photo['url']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")

@pytest.mark.parametrize("photo_id, expected_status", [
    (1, HTTPStatus.OK), # Успешно удалён
    (9999, HTTPStatus.NOT_FOUND) # Фото не существует
])
def test_delete_photo(photo_api, photo_id, expected_status):
    """
    Удаление фото(позитивные и негативные сценарии)
    """
    response = photo_api.delete_photo(photo_id)
    assert response.status_code == expected_status