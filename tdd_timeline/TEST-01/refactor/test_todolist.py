import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_01_criar_tarefa_valida(self):
        lista = ToDoList()
        tarefa = lista.add_task("Estudar TDD", "Ler apostila e praticar")
        self.assertEqual(tarefa.name, "Estudar TDD")
        self.assertEqual(tarefa.description, "Ler apostila e praticar")

if __name__ == "__main__":
    unittest.main()
