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

def add_product (product_list: list, **dictItem: dict) -> dict:
    index = 1

    if len(product_list) == 0:
        dictItem.update({ "_id": index })
        product_list.append(dictItem)
        return dictItem

    for item in product_list:
        if item["_id"] >= index:
            index = item["_id"] + 1


    dictItem.update({ "_id": index })
    product_list.append(dictItem)
            
    return dictItem