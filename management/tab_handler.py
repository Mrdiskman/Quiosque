from menu import products

def calculate_tab(table: list):
    id_list = []
    ammount_list = []

    for item in table:
        id_list.append(item["_id"])
        ammount_list.append(item["amount"])
    
    value_list = []

    for id in id_list:
        for item in products:
            if item["_id"] == id:
                value_list.append(item["price"])

    sub_total = round(sum([a*b for a,b in zip(ammount_list, value_list)]), 2)
    return {"subtotal": f"${sub_total}"}