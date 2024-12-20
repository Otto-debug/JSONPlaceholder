import pytest
from http import HTTPStatus
from pydantic import ValidationError
from src.schemas.albums import AlbumSchema

@pytest.mark.parametrize("album_id, expected_status", [
    (1, HTTPStatus.OK), # Альбом существует
    (2, HTTPStatus.OK), # Альбом существует
    (9999, HTTPStatus.NOT_FOUND) # Альбома не существует
])
def test_get_album(albums_api, album_id, expected_status):
    """
    Тесты на получения альбома(позитивные и негативные сценарии)
    """
    response = albums_api.get_albums(album_id)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            album_data = AlbumSchema(**response.json())
            assert album_data.id == album_id
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")

@pytest.mark.parametrize("new_album, expected_status", [
    ({'title': 'New Album', 'userId': 1}, HTTPStatus.CREATED), # Успешно создан альбом
    ({}, HTTPStatus.BAD_REQUEST), # Пустое тело
    ({'title': "New Album"}, HTTPStatus.BAD_REQUEST) # Неполные данные
])
def test_create_album(albums_api, new_album, expected_status):
    """
    Тесты на создание нового альбома(позитивные и негативные сценарии)
    """
    response = albums_api.create_album(new_album)
    assert response == expected_status

    if response.status_code == HTTPStatus.CREATED:
        try:
            albums_data = AlbumSchema(**response.json())
            assert albums_data.title == new_album['title']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")

@pytest.mark.parametrize("album_id, updated_album, expected_status", [
    (1, {"id": 1, "title": "Updated Album", "userId": 1}, HTTPStatus.OK), # Успешное обновление
    (9999, {"id": 9999, "title": "Updated Album", "userId": 1}, HTTPStatus.NOT_FOUND), # Альбома нет
    (1, {}, HTTPStatus.BAD_REQUEST) # Пустое тело запроса
])
def test_update_albums(albums_api, album_id, updated_album, expected_status):
    """
    Тесты на обновление альбома(позитивные и негативные сценарии)
    """
    response = albums_api.update_album(album_id, updated_album)
    assert response.status_code == expected_status

    if response.status_code == HTTPStatus.OK:
        try:
            albums_data = AlbumSchema(**response.json())
            assert albums_data.title == updated_album['title']
        except ValidationError as e:
            pytest.fail(f"Response schema validation failed: {e}")

@pytest.mark.parametrize("album_id, expected_status", [
    (1, HTTPStatus.OK), # Успешно удалён
    (9999, HTTPStatus.NOT_FOUND) # Альбома нет
])
def test_delete_album(albums_api, album_id, expected_status):
    """
    Тест на удаление альбома(позитивные и негативные сценарии)
    """
    response = albums_api.delete_album(album_id)
    assert response.status_code == expected_status






















