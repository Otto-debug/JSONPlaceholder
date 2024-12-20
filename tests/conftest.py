import pytest
import logging

from src.api.posts_api import PostsAPI
from src.api.comments_api import CommentsAPI
from src.api.albums_api import AlbumsAPI
from src.api.photos_api import PhotosAPI
from src.api.todo_api import TodoAPI
from src.api.user_api import UserAPI

"""
### Объяснение
1. **`base_url`**:
   - Фикстура с `scope="session"`, чтобы определить базовый URL один раз за тестовую сессию.

2. **`posts_api`**:
   - Создаёт экземпляр `PostsAPI` для использования в тестах.
   - Автоматически предоставляет доступ к методам `/posts`.

3. **`setup_logging`**:
   - Устанавливает формат и уровень логирования для всей тестовой сессии.
   - Отображает логи прямо в консоли Pytest.

4. **`pytest_configure`**:
   - Добавляет мета-данные в Allure-отчёты, например, название проекта и имя тестировщика.

5. **`pytest_runtest_makereport`**:
   - Автоматически добавляет информацию об ошибках в отчёт Allure, если тест упал.
   - Пример показывает, как можно приложить логи или другую информацию к отчёту.
"""

@pytest.fixture(scope='session')
def base_url():
    """
    Базовый URL для тестирующего API
    """
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope='session')
def posts_api(base_url):
    """
    Фикстура для инициализации API-клиента PostsAPI
    :param base_url: Базовый URL API
    :return: Экземпляр PostsAPI
    """
    return PostsAPI(base_url)

@pytest.fixture(scope="session")
def comments_api(base_url):
    """
    Фикстура для /comments
    Создаёт единственный экземпляр клиента для всей сессии тестов
    :param base_url: Базовый URL API
    :return: Экземпляр CommentsAPI
    """
    return CommentsAPI(base_url="https://jsonplaceholder.typicode.com")

@pytest.fixture(scope='session')
def albums_api(base_url):
    """
    Фикстура для /albums
    :param base_url: Базовый URL API
    :return: Экземпляр AlbumsAPI
    """
    return AlbumsAPI(base_url="https://jsonplaceholder.typicode.com")

@pytest.fixture(scope="session")
def photo_api(base_url):
    """
    Фикстура для /photos
    """
    return PhotosAPI(base_url="https://jsonplaceholder.typicode.com")

@pytest.fixture(scope="session")
def todo_api(base_url):
    """
    Фикстура для /todos
    """
    return TodoAPI(base_url="https://jsonplaceholder.typicode.com")

@pytest.fixture(scope="session")
def user_api(base_url):
    """
    Фикстура для /users
    """
    return UserAPI(base_url="https://jsonplaceholder.typicode.com")


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    """
    Настройка логирования для тестов
    Логирование отображается в консоли для упрощения отладки
    """

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Настройка для специфичного логгера "API"
    api_logger = logging.getLogger("API")
    api_logger.setLevel(logging.DEBUG)  # Логировать больше деталей для API


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Конфигурация Pytest для интеграции Allure
    Добавляет мета-данные проекта в Allure-отчёты
    """

    # Настройка Allure
    if hasattr(config, "option"):
        allure_dir = getattr(config.option, 'alluredir', None)
        if allure_dir:
            logging.info(f"Allure reports will be saved in: {allure_dir}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для добавление шагов в Allure на основании статуса теста.
    Автоматически добавляет статус теста(успех, провал, ошибка)
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        from allure_commons._allure import attach
        from allure_commons.types import AttachmentType

        # Добавление данных в отчёт при провале теста
        attach(body=str(report.longrepr),
               name="Test Failure Log",
               attachment_type=AttachmentType.TEXT)