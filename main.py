from management.product_handler import get_product_by_id, get_products_by_type, add_product

list = []

new_product = {
            "title": "Suco de React",
            "price": 5.0,
            "rating": 4,
            "description": "Suco de React com Limao",
            "type": "drink",
        }

if __name__ == "__main__":
    print(get_product_by_id(21))
    print(get_products_by_type("drink"))
    print(add_product(list, new_product))
    ...