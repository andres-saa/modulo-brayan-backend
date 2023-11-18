from fastapi import APIRouter, HTTPException
from config.db import conn
from models.product_photo import Product_photo_model
from schema.product_photo import Produc_photo_schema_post
from fastapi.responses import JSONResponse

photo_router = APIRouter()

@photo_router.get("/photos")
def get_photos():
    result = conn.execute(Product_photo_model.select()).fetchall()

    fields = ["photo_id", "image_url", "product_id"]
    json_data = []

    for item in result:
        json_item = {}
        for i, field in enumerate(fields):
            json_item[field] = item[i]
        json_data.append(json_item)

    return json_data


@photo_router.get("/photos/{product_id}")
def get_photo_by_product_id(product_id: int):
    result = conn.execute(Product_photo_model.select().where(Product_photo_model.c.product_id == product_id)).fetchall()

    if not result:
        return JSONResponse(content={"message": "No photos found for the specified product ID"})

    fields = ["photo_id", "image_url", "product_id"]
    json_data = []

    for item in result:
        json_item = {}
        for i, field in enumerate(fields):
            json_item[field] = item[i]
        json_data.append(json_item)

    return {"message": "Some other route", "photos_data": json_data}

@photo_router.post("/photos")
def create_photo(photo: Produc_photo_schema_post):
    new_photo = {
        "image_url": photo.image_url,
        "product_id": photo.product_id
    }

    result = conn.execute(Product_photo_model.insert().values(new_photo))
    conn.commit()

    return JSONResponse(content={"message": "Photo created successfully"})

@photo_router.delete("/photos/{photo_id}")
def delete_photo(photo_id: int):
    result = conn.execute(Product_photo_model.select().where(Product_photo_model.c.photo_id == photo_id)).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Photo not found")

    conn.execute(Product_photo_model.delete().where(Product_photo_model.c.photo_id == photo_id))
    conn.commit()

    return JSONResponse(content={"message": "Photo deleted successfully"})
