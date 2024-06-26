from menu import products
from management.sortBy import sortById

def get_product_by_id (id):
    if type(id) != int:
        raise(TypeError("product id must be an int"))

    for x in products:
        if (x["_id"] == id):
            return x
        
    return {}
        
def get_products_by_type (type_str: str):
    if type(type_str) != str:
        raise(TypeError("product type must be a str"))

    filtered = []

    for x in products:
        if (x["type"] == type_str):
            filtered.append(x)
        
    return filtered

def add_product (product_list: list, **dict_item: dict) -> dict:
    index = 1
    product_list.sort(key=sortById)

    if len(product_list) == 0:
        dict_item.update({ "_id": index })
    else:
        index = product_list[-1]["_id"] + 1

    dict_item.update({ "_id": index })
    product_list.append(dict_item)
    return dict_item

def menu_report ():
    count = len(products)
    sum_price = 0
    types_dictionary = {}

    for item in products:
        sum_price = sum_price + item["price"]
        type_item = types_dictionary.get(item["type"], False)

        if not type_item:
            types_dictionary.update({ item["type"]: 1 })
        else :
            types_dictionary.update({ item["type"]: type_item + 1 })

    most_item_position = max(types_dictionary, key=types_dictionary.get)

    avg_price = sum_price / count

    return f"Products Count: {count} - Average Price: ${round(avg_price, 2)} - Most Common Type: {most_item_position}"

def add_product_extra (menu: list, *required: tuple, **new_product: dict) -> dict:
    dict_keys = list(new_product.keys())
    tuple_keys = list(required)

    for tuple_key in tuple_keys:
        if tuple_key not in dict_keys:
            raise(KeyError(f"field {tuple_key} is required"))
        
    for dict_key in dict_keys:
        if dict_key not in tuple_keys:
            new_product.pop(dict_key)

    index = 1
    menu.sort(key=sortById)

    if len(menu) == 0:
        new_product.update({ "_id": index })
    else:
        index = menu[-1]["_id"] + 1

    new_product.update({ "_id": index })
    menu.append(new_product)
    return new_product