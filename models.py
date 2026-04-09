
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    # def __init__(self, id, name, description, price, quantity):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity








#copy pasted from the main file to keep it clean- it doesnt belong here lol

    # products = [ Product(id=1 , name= "watch", description = "titan watch " , price = 20000 , quantity =2),
#             Product(id=2 , name= "watch", description = "sony watch " , price = 20000 , quantity =4),
#             Product(id=3 , name= "watch", description = "quartz watch " , price = 50000 , quantity =5),
#             Product(id=4 , name= "watch", description = "fastrack watch " , price = 20800 , quantity =1),
#             ]
 
