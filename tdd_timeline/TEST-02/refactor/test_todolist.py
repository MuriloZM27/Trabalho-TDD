import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_02_rejeitar_criacao_nome_vazio(self):
        lista = ToDoList()
        with self.assertRaises(ValueError):
            lista.add_task("", "desc")
        with self.assertRaises(ValueError):
            lista.add_task("   ", "desc")

if __name__ == "__main__":
    unittest.main()
