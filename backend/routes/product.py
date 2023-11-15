from fastapi import APIRouter
from config.db import conn
from models.product import product_model
from schema.product import Product_schema_post
from fastapi.responses import JSONResponse
import json


product_router = APIRouter()


@product_router.get("/products")
def get_products():
    result = conn.execute(product_model.select()).fetchall()
    print(result)

    fields = ["product_id", "product_name", "product_description", "product_purchase_price", "product_selling_price"]
    json_data = []

    for item in result:
        json_item = {}
        for i, field in enumerate(fields):
            json_item[field] = item[i]  # Include the first element in the tuple, which is product_id
        json_data.append(json_item)

    return JSONResponse(json_data)



@product_router.post("/products")
def create_product(product:Product_schema_post):
    # return conn.execute(product_model.select()).fetchall()
    new_product = {
        # "product_id":product.id,
        "product_name":product.product_name,
        "product_description":product.product_description,
        "product_purchase_price":product.product_purchase_price,
        "product_selling_price":product.product_selling_price


        }
    
    result = conn.execute(product_model.insert().values(new_product))
    conn.commit()  # Agrega este commit para guardar los cambios en la base de datos
    print(result)


@product_router.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product_schema_post):
    result = conn.execute(product_model.select().where(product_model.c.product_id == product_id)).fetchone()

    if result is None:
        return JSONResponse(content={"error": "Product not found"}, status_code=404)

    updated_values = {
        "product_name": updated_product.product_name,
        "product_description": updated_product.product_description,
        "product_purchase_price": updated_product.product_purchase_price,
        "product_selling_price": updated_product.product_selling_price
    }

    conn.execute(product_model.update().where(product_model.c.product_id == product_id).values(updated_values))
    conn.commit()

    return JSONResponse(content={"message": "Product updated successfully"})


@product_router.delete("/products/{product_id}")
def delete_product(product_id: int):
    result = conn.execute(product_model.select().where(product_model.c.product_id == product_id)).fetchone()

    if result is None:
        return JSONResponse(content={"error": "Product not found"}, status_code=404)

    conn.execute(product_model.delete().where(product_model.c.product_id == product_id))
    conn.commit()

    return JSONResponse(content={"message": "Product deleted successfully"})
