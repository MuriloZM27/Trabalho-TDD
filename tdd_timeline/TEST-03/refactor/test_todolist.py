import unittest
from todolist import ToDoList, Status

class TestToDoList(unittest.TestCase):
    def test_03_marcar_como_concluida(self):
        lista = ToDoList()
        t = lista.add_task("comprar pão", "padaria")
        lista.mark_done(t.id)
        self.assertEqual(lista.get(t.id).status, Status.DONE)

if __name__ == "__main__":
    unittest.main()
