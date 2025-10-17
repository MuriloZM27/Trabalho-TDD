from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

class Status(Enum):
    PENDING = "pendente"
    IN_PROGRESS = "em andamento"
    DONE = "concluída"

@dataclass
class Task:
    id: int
    name: str
    description: str
    status: Status = field(default=Status.PENDING)

class ToDoList:
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def _ensure_exists(self, task_id: int) -> Task:
        if task_id not in self._tasks:
            raise KeyError("tarefa inexistente")
        return self._tasks[task_id]

    def add_task(self, name: str, description: str) -> Task:
        task = Task(id=self._next_id, name=name.strip(), description=description or "")
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        return self._ensure_exists(task_id)

    def edit_task(self, task_id: int, *, name: Optional[str] = None, description: Optional[str] = None) -> Task:
        task = self._ensure_exists(task_id)
        if name is not None:
            if not name.strip():
                raise ValueError("nome da tarefa não pode ser vazio")
            task.name = name.strip()
        if description is not None:
            task.description = description
        return task
