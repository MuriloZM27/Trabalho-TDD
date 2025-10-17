import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_04_nao_marcar_concluida_duas_vezes(self):
        lista = ToDoList()
        t = lista.add_task("lavar louça", "")
        lista.mark_done(t.id)
        with self.assertRaises(ValueError):
            lista.mark_done(t.id)

if __name__ == "__main__":
    unittest.main()
