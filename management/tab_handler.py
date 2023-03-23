from menu import products

def calculate_tab (itemList: list) -> dict:
    total = 0
    for item in itemList:
        for product in products:
            if product["_id"] == item["_id"]:
                total = total + (product["price"] * item["amount"])

    return {"subtotal": f"${round(total, 2)}"}