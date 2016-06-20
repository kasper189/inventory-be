import unittest
import model.item


class TestModel(unittest.TestCase):

    def creation_test(self):
        name = 'item name'
        count = 3

        item = model.item.Item(name, count)
        self.assertEqual(name, item.item.name)
        self.assertEqual(count, 3)
