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

    def mark_done(self, task_id: int) -> Task:
        task = self._ensure_exists(task_id)
        task.status = Status.DONE
        return task

    def mark_in_progress(self, task_id: int) -> Task:
        task = self._ensure_exists(task_id)
        if task.status == Status.DONE:
            raise ValueError("não é possível marcar 'em andamento' uma tarefa já concluída")
        task.status = Status.IN_PROGRESS
        return task
