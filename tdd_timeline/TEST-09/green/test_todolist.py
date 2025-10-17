import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_09_excluir_tarefa(self):
        lista = ToDoList()
        t = lista.add_task("deletar", "")
        lista.delete_task(t.id)
        with self.assertRaises(KeyError):
            lista.get(t.id)

if __name__ == "__main__":
    unittest.main()
