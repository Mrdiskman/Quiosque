from management.product_handler import get_product_by_id, get_products_by_type, menu_report, add_product
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    get_product_by_id(20)
    produto = { 
        "description": "Healthy breakfast with cottage cheese and strawberry",
        "price": 14.05,
        "rating": 1,
        "title": "Breakfast with cottage",
        "type": "fruit",
        }
    print(add_product([], **produto))
    get_products_by_type("vegetable")
    menu_report()
    list_objects = [{
        "_id":20,
        "ammount":5
    },
    {
        "_id":22,
        "ammount":8
    }]
    # print(calculate_tab(list_objects))
    ...
