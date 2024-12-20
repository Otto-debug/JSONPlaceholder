from src.api.base_api import BaseAPI

class TodoAPI(BaseAPI):
    """
    Класс для работы с эндпоинтами /todos
    """
    def get_todos(self, todo_id):
        """
        Возвращает задачу по ID
        """
        return self.get(f"/todos/{todo_id}")

    def create_todos(self, todos_data):
        """
        Создание новой задачи
        """
        return self.post('/todos', json=todos_data)

    def updated_todos(self, todo_id, todos_data):
        """
        Обновление задачи
        """
        return self.put(f"/todos/{todo_id}", json=todos_data)

    def delete_todos(self, todo_id):
        """
        Удаление задачи
        """
        return self.delete(f"/todos/{todo_id}")