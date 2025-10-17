import unittest
from todolist import ToDoList, Status

class TestToDoList(unittest.TestCase):
    def test_05_marcar_como_em_andamento(self):
        lista = ToDoList()
        t = lista.add_task("estudar", "")
        lista.mark_in_progress(t.id)
        self.assertEqual(lista.get(t.id).status, Status.IN_PROGRESS)

if __name__ == "__main__":
    unittest.main()
