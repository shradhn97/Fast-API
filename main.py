
from fastapi import FastAPI
from models import *

app=FastAPI()

@app.get("/")
def myfun():
    return "welcome to my web page ✅"


products=[
    Product(id=1,name="laptop",describtion="gaming laptop",price=90000,quantity=15),
    Product(id=2,name="mobile",describtion="gaming mobile",price=8000,quantity=14),
    Product(id=3,name="ac",describtion="super AC",price=10000,quantity=13),
    Product(id=4,name="cooler",describtion="super cooling",price=11000,quantity=12),
    Product(id=5,name="washing machine",describtion="automatic",price=8900,quantity=11)

]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
        
    return {"error":"product not found"}

@app.post("/products/")
def add_product(product:Product):
    products.append(product)
    return product

@app.put("/products/")
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]==product
            return "product found successfully ✅"
        
    return "no product found"

@app.delete("/products/")
def delete_product(id:int):
    for i in range (len(products)):
        if products[i].id==id:
            del products[i]
            return "products deleted "
    return "no products found "