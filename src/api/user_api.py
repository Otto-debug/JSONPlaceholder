from src.api.base_api import BaseAPI

class UserAPI(BaseAPI):
    """
    Класс для работы с эндпоинтами /users
    """
    def get_user(self, user_id):
        """
        Получение пользователя по ID
        """
        return self.get(f"/users/{user_id}")

    def create_user(self, user_data):
        """
        Создание пользователя
        """
        return self.post(f"/users", json=user_data)

    def update_user(self, user_id, user_data):
        """
        Обновление пользователя
        """
        return self.put(f"/users/{user_id}", json=user_data)

    def delete_user(self, user_id):
        """
        Удаление пользователя
        """
        return self.delete(f"/users/{user_id}")
