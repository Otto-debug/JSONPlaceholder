from src.api.base_api import BaseAPI

class PostsAPI(BaseAPI):
    """
    Класс для работы с API /posts
    """
    
    def get_posts(self, post_id=None):
        """
        Получение всех постов или поста по ID

        :param post_id: ID поста(необязательный параметр)
        :return: Ответ API(объект Response)
        """

        endpoint = f"/posts/{post_id}" if post_id else "/posts"
        return self.get(endpoint)

    def create_post(self, payload):
        """
        Создание нового поста

        :param payload: Словарь с данными нового поста
        :return: Ответ API(объект Response)
        """

        return self.post("/posts", json=payload)

    def update_post(self, post_id, payload):
        """
        Полное обновление поста (метод PUT)

        :param post_id: ID поста
        :param payload: Словарь с новыми данным поста
        :return: Ответ API(объект Response)
        """

        return self.put(f'/posts/{post_id}', json=payload)

    def patch_post(self, post_id, payload):
        """
        Частичное обновление поста(метод PATCH)

        :param post_id: ID поста
        :param payload: Словарь с данными для обновления
        :return: Ответ API(объект Response)
        """

        return self.patch(f'/posts/{post_id}', json=payload)

    def delete_post(self, post_id):
        """
        Удаление поста

        :param post_id: ID поста
        :return: Ответ API(объект Response)
        """

        return self.delete(f'/posts/{post_id}')