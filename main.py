from fastapi import FastAPI
from models import Product
from fastapi.middleware.cors import CORSMiddleware
from database import session , engine
import database_model
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI()
# cors setup
database_model.base.metadata.create_all(bind= engine)
app.add_middleware(
    CORSMiddleware,
     allow_origins=["http://localhost:3000"],  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
   
)


@app.get("/")
def greet():
    return "main product page"


#dependency injection

def get_db():
    db= session() #start session

    try:
        yield db    #generator(yeild)-- when used -pauses execution - returns control to the caller -resumes later from same point
    finally:        #resume point -- always runs despite anything above --guarantees connection closes 
        db.close()


#old -- without dependency injection

# @app.get("/products")
# def all_products():
#     #start connection / session with db (limited 'connections' are there so you must manually close each connection after you finish calling func/using db)
#     db = session()
#     products = db.query(Product).all()
#     db.close
#     return products
   

#new --with depinj..
@app.get("/products")
def all_products( db: Session = Depends(get_db)):
    products = db.query(database_model.Product).all()
    return products

@app.get("/products/{id}")
def get_by_id(id :int , db:Session= Depends(get_db)):
    db_product =db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    
    return "product not found"


@app.post("/products")
def add_product( product :Product , db:Session= Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int ,product :Product, db:Session= Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
       db_product.name = product.name
       db_product.description=product.description
       db_product.price=product.price
       db_product.quantity=product.quantity
       db.commit()
       return "product updated"
    else:
        return "product not found"

@app.delete("/products/{id}")
def delete_product(id :int ,db:Session= Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted"
    else:
        return "product not found"

  













#wihout db versions

# @app.get("/product/{p_id}")
# def get_product_byid(p_id : int):
#      for p in products:
#           if p.id==p_id:
#                return p
          
          
# @app.post("/post_product")
# def post_product(new_product : Product):
#      products.append(new_product)
#      return new_product

# @app.put("/product/{p_id}")
# def update(p_id :int , new_product :Product):
#     for i in range(len(products)):
#         if products[i].id == p_id:
#             products[i] = new_product
#             return new_product
        

# @app.delete("/product")
# def delete_prod(p_id: int):
#      for i in range(len(products)):
#           if products[i].id==p_id:
#                products.pop(i)
#                return products 
          
#      return "product not found"     
# 