import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_10_excluir_inexistente(self):
        lista = ToDoList()
        with self.assertRaises(KeyError):
            lista.delete_task(42)

if __name__ == "__main__":
    unittest.main()
