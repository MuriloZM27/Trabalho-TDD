import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_06_nao_pode_marcar_em_andamento_se_concluida(self):
        lista = ToDoList()
        t = lista.add_task("correr", "")
        lista.mark_done(t.id)
        with self.assertRaises(ValueError):
            lista.mark_in_progress(t.id)

if __name__ == "__main__":
    unittest.main()
