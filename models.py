from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    describtion:str
    price:int
    quantity:int

    # def __init__(self,id:int,name:str,describtion:str,price:int,quantity:int):
    #     self.id=id
    #     self.name=name
    #     self.describtion=describtion
    #     self.price=price
    #     self.quantity=quantity
