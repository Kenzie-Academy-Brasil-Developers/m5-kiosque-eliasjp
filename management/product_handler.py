from menu import products

def get_product_by_id(id):
    for x in products:
        if (x["_id"] == id):
            return x
        
    return {}

        
def get_products_by_type(type):
    filtered = []

    for x in products:
        if (x["type"] == type):
            filtered.append(x)
        
    return filtered