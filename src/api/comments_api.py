from src.api.base_api import BaseAPI


class CommentsAPI(BaseAPI):
    """
    Класс для работы с эндпоинтами /comments
    """

    def get_comment(self, comment_id):
        """
        Получить комментарии по ID

        :param comment_id: ID comment
        :return: Объект API
        """
        return self.get(f'/comments/{comment_id}')

    def create_comment(self, comment_data):
        """
        Создать комментарий по ID

        :param comment_data: JSON данные
        :return: Объект API
        """
        return self.post('/comments', json=comment_data)

    def update_comment(self, comment_id, comment_data):
        """
        Обновить комментарии по ID

        :param comment_id: ID comment
        :param comment_data: JSON данные
        :return: Объект API
        """
        return self.put(f'/comments/{comment_id}', json=comment_data)

    def delete_comment(self, comment_id):
        """
        Удалить комментарий по ID

        :param comment_id: ID comment
        :return: Объект API
        """
        return self.delete(f'/comments/{comment_id}')

