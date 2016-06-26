import model.item as model

def build_inventory(bson_items):
    item_list = list()

    for item in bson_items:
        json_item = model.JsonItem(item)
        item_list.append(json_item.get_dictionary())

    return item_list

