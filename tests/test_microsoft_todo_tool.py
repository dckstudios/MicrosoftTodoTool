import pytest
from microsoft_todo_tool import MicrosoftTodoTool

# Mocking el access_token para el test
MOCK_ACCESS_TOKEN = "your_mock_access_token"

def test_get_tasks():
    tool = MicrosoftTodoTool()
    
    # Llamada al método get_tasks
    tasks = tool.get_tasks(MOCK_ACCESS_TOKEN)
    
    # Asegurarse de que la respuesta es una lista (o un dict, dependiendo de la estructura de la respuesta)
    assert isinstance(tasks, list)  # o assert isinstance(tasks, dict)

    # Puedes agregar más assertions según lo que esperes de la respuesta

def test_update_task():
    tool = MicrosoftTodoTool()
    
    # Mocking datos para el test
    MOCK_TASK_ID = "your_mock_task_id"
    NEW_TITLE = "Test Title"
    DUE_DATE = "2023-08-30T14:00:00.000Z"
    
    # Llamada al método update_task
    updated_task = tool.update_task(MOCK_ACCESS_TOKEN, MOCK_TASK_ID, NEW_TITLE, DUE_DATE)
    
    # Asegurarse de que la tarea se actualizó correctamente
    assert updated_task.get("title") == NEW_TITLE
    assert updated_task.get("dueDateTime", {}).get("dateTime") == DUE_DATE

    # Puedes agregar más assertions según lo que esperes de la respuesta
