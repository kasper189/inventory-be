import json
import unittest
import model.item


class TestModel(unittest.TestCase):

    def creation_test(self):
        name = 'item name'
        count = 3

        item = model.item.Item(name, count)
        self.assertEqual(name, item.item.name)
        self.assertEqual(count, 3)

    def getter_test(self):
        name = 'inventory_name'
        count = 2

        item = model.item.Item(name, count)
        json_item = model.item.JsonItem(item.item)

        self.assertEqual(name, json_item.get_name())
        self.assertEqual(count, json_item.get_count())

    def dictionary_test(self):
        name = 'inventory_name'
        count = 2

        item = model.item.Item(name, count)
        json_item = model.item.JsonItem(item.item)

        computed_json = json_item.get_dictionary()

        expected_dict = { 'name': name, 'count': count}
        expected_dict_json = json.dumps(expected_dict)

        self.assertEqual(expected_dict_json, json.dumps(computed_json))