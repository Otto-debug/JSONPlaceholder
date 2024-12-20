from src.api.comments_api import BaseAPI

class AlbumsAPI(BaseAPI):
    """
    Класс для работы с эндпоинтами /albums
    """

    def get_albums(self, album_id):
        """
        Получить альбом по ID
        """
        return self.get(f'/albums/{album_id}')

    def create_album(self, album_data):
        """
        Создать новый альбом
        """
        return self.post("/albums", json=album_data)

    def update_album(self, album_id, album_data):
        """
        Обновить альбом по ID
        """
        return self.put(f'/albums/{album_id}', json=album_data)

    def delete_album(self, album_id):
        """
        Удаление альбома по ID
        """
        return self.delete(f'/albums/{album_id}')