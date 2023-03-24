from menu import products

def get_product_by_id (id):
    for x in products:
        if (x["_id"] == id):
            return x
        
    return {}

        
def get_products_by_type (type):
    filtered = []

    for x in products:
        if (x["type"] == type):
            filtered.append(x)
        
    return filtered

def add_product (product_list: list, **dict_item: dict) -> dict:
    index = 1

    if len(product_list) == 0:
        dict_item.update({ "_id": index })
        product_list.append(dict_item)
        return dict_item

    for item in product_list:
        if item["_id"] >= index:
            index = item["_id"] + 1


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

    most_item_position = list(types_dictionary.keys())[list(types_dictionary.values()).index(max(list(types_dictionary.values())))]

    avg_price = sum_price / count

    return f"Products Count: {count} - Average Price: ${round(avg_price, 2)} - Most Common Type: {most_item_position}"

def get_product_by_id (id: int) -> dict:
    if type(id) != int:
        raise(TypeError("product id must be an int"))

    for item in products:
        if item["_id"] == id:
            return item