from superagi.tools.base_tool import BaseTool
import requests

class MicrosoftTodoTool(BaseTool):
    name = "MicrosoftTodoTool"
    description = "Herramienta para interactuar con la API de Microsoft Graph para Microsoft To-Do"

    def get_tasks(self, access_token):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.get('https://graph.microsoft.com/v1.0/me/todo/lists', headers=headers)
        return response.json()

    def update_task(self, access_token, task_id, new_title, due_date):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'title': new_title,
            'dueDateTime': {
                'dateTime': due_date,
                'timeZone': 'UTC'
            }
        }
        response = requests.patch(f'https://graph.microsoft.com/v1.0/me/todo/lists/{task_id}', headers=headers, json=data)
        return response.json()

    # Puedes agregar más métodos según las operaciones que desees realizar con la API
