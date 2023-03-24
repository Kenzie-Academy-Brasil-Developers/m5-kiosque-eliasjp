from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    print(get_product_by_id())
    print(get_products_by_type())
    print(add_product())
    print(calculate_tab())
    print(menu_report())
    ...