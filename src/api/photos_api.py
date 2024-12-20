from src.api.base_api import BaseAPI

class PhotosAPI(BaseAPI):
    """
    Класс для работы с эндпоинтами /photos
    """

    def get_photos(self, photo_id):
        """
        Возвращает фото по ID
        """
        return self.get(f"/photos/{photo_id}")

    def create_photo(self, photo_data):
        """
        Создание нового фото
        """
        return self.post('/photos', json=photo_data)

    def update_photo(self, photo_id, photo_data):
        """
        Обновление фото
        """
        return self.put(f"/photos/{photo_id}", json=photo_data)

    def delete_photo(self, photo_id):
        """
        Удаление фото
        """
        return self.delete(f"/photo/{photo_id}")
