import logging
from requests import Response
import requests

logger = logging.getLogger("API")

class BaseAPI:
    """
    Базовый класс для взаимодействия с API
    Этот класс представляет методы для отправки HTTP-запросов и логирования.
    """

    def __init__(self, base_url: str):
        """
        Инициализация базового API-класса

        :param base_url: Базовый URL API, например: "https://jsonplaceholder.typicode.com
        """
        self.base_url = base_url

    def request(self, method: str, endpoint: str, **kwargs) -> Response:
        """
        Отправляет HTTP-запросы к API

        :param method: HTTP-метод(например: "GET", "POST", "PUT", "DELETE", "PATCH")
        :param endpoint: Конечная точка API(например: "/posts" или "/posts/1")
        :param kwargs: Дополнительные параметры для метода requests(например, json=payload, headers=headers)
        :return: Объект Response от библиотеки requests
        """

        url = f"{self.base_url}{endpoint}"
        try:
            logger.info(f'Making {method} request to {url} with params: {kwargs}')
            response = requests.request(method, url, **kwargs)
            logger.info(f'Response status: {response.status_code}')
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.error(f'Request failed: {e}')
            raise


    def get(self, endpoint: str, **kwargs) -> Response:
        """
        Отправляет GET-запрос

        :param endpoint: Конечная точка API(например: "/posts, /posts/1")
        :param kwargs: Дополнительные параметры (например: тело запроса json=payload)
        :return: Объект Response
        """

        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> Response:
        """
        Отправляет POST-запрос

        :param endpoint: Конечная точка API(например, "/posts")
        :param kwargs: Дополнительные параметры (например: тело запроса json=payload)
        :return: Объект Response
        """
        
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> Response:
        """
        Отправляет PUT-запрос

        :param endpoint: Конечная точка API(например: "/posts/1")
        :param kwargs: Дополнительные параметры(например: json=payload)
        :return: Объект Response
        """

        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> Response:
        """
        Отправляет PATCH-запрос

        :param endpoint: Конечная точка API(например: "/posts/1")
        :param kwargs: Дополнительные параметры(например: json=payload)
        :return: Объект Response
        """

        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        """
        Отправляет DELETE-запрос

        :param endpoint: Конечная точка API(например: "/posts/1")
        :param kwargs: Дополнительные параметры(например: json=payload)
        :return: Объект Response
        """

        return self.request("DELETE", endpoint, **kwargs)

    