import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_08_impedir_edicao_inexistente(self):
        lista = ToDoList()
        with self.assertRaises(KeyError):
            lista.edit_task(999, name="x")
        t = lista.add_task("a", "b")
        with self.assertRaises(ValueError):
            lista.edit_task(t.id, name="   ")

if __name__ == "__main__":
    unittest.main()
