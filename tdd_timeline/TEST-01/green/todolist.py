class ToDoList:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add_task(self, name, description):
        # Implementação mínima para o teste 01
        Task = type("Task", (), {})
        task = Task()
        task.id = self._next_id
        task.name = name
        task.description = description
        task.status = "pendente"
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
