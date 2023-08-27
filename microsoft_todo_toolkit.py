from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseToolkit
from microsoft_todo_tool import MicrosoftTodoTool

class MicrosoftTodoToolkit(BaseToolkit, ABC):
    name: str = "Microsoft Todo Toolkit"
    description: str = "Kit de herramientas para interactuar con la API de Microsoft Graph para Microsoft To-Do"

    def get_tools(self) -> List[BaseTool]:
        return [MicrosoftTodoTool()]

    def get_env_keys(self) -> List[str]:
        return ["CLIENT_ID", "CLIENT_SECRET", "REDIRECT_URI", "ACCESS_TOKEN"]
