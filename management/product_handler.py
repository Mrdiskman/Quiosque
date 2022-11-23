from menu import products

def get_product_by_id(id:int):
    
    if type(id) == int:
        for item in products:
            if id == item["_id"]:
                return item  
        return {}
    raise TypeError("product id must be an int")

def get_products_by_type(prod_type:str):
    
        if type(prod_type) == str:
            list_of_types = []
            for item in products:
                if prod_type == item["type"]:
                    list_of_types.append(item)
            if len(list_of_types):
                    return list_of_types
            return list()
        raise TypeError("product type must be a str")

def menu_report():
    contagem = len(products)
    preco_de_produtos = 0
    most_commun_type = products[0]["type"]

    for item in products:
        preco_de_produtos += item["price"] 
        if len(get_products_by_type(most_commun_type)) < len(get_products_by_type(item["type"])):
            most_commun_type = item["type"]
    media = preco_de_produtos/contagem
    return f"Products Count: {contagem} - Average Price: ${media:.1f} - Most Common Type: {most_commun_type}"

def add_product(list_products, **new_product):
    id = len(products) + 1
    print(id)
    new_product["_id"] = id
    list_products.append(new_product)
    print(list_products)
    return new_product