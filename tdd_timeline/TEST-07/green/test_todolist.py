import unittest
from todolist import ToDoList

class TestToDoList(unittest.TestCase):
    def test_07_editar_nome_e_descricao(self):
        lista = ToDoList()
        t = lista.add_task("antigo", "velha desc")
        lista.edit_task(t.id, name="novo", description="nova desc")
        self.assertEqual(lista.get(t.id).name, "novo")
        self.assertEqual(lista.get(t.id).description, "nova desc")

if __name__ == "__main__":
    unittest.main()
