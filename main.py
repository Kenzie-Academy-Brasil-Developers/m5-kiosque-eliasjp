# from management.product_handler import get_product_by_id, get_products_by_type, add_product
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    # print(get_product_by_id(21))
    # print(get_products_by_type("drink"))
    # print(add_product(list, new_product))
    print(calculate_tab([
                    {"_id": 10, "amount": 3},
                    {"_id": 20, "amount": 2},
                    {"_id": 21, "amount": 5},
                ]))
    ...