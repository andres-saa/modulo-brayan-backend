from fastapi import APIRouter
from config.db import conn
from models.category import category_model
from schema.category import category_schema_post
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
import json  # Asegúrate de tener este import en tu código
from models.category import category_model


category_router = APIRouter()

@category_router.get("/categories")
def get_providers():
    result = conn.execute(category_model.select()).fetchall()

    category_data_list = []
    for row in result:
        provider_data = {
            "category_id": row.category_id,
            "category_name": row.category_name,
        }
        category_data_list.append(provider_data)

    return JSONResponse(content=category_data_list)

    # return JSONResponse(json_data)

@category_router.post("/categories")
def create_provider(categorie: category_schema_post):
    new_categorie = {
            # "category_id": categorie.category_id,
            "category_name": categorie.category_name,
        }

    result = conn.execute(category_model.insert().values(new_categorie))
    conn.commit()

    return JSONResponse(content={"message": "Provider created successfully"})

# @category_router.put("/providers/{provider_id}")
# def update_provider(provider_id: int, updated_provider: provider_schema_post):
#     result = conn.execute(category_model.select().where(category_model.c.provider_id == provider_id)).fetchone()

#     if result is None:
#         raise HTTPException(status_code=404, detail="Provider not found")

#     updated_values = {
#         "provider_name": updated_provider.provider_name,
#         "provider_address": updated_provider.provider_address,
#         "provider_contact": updated_provider.provider_contact,
#         "provider_nit": updated_provider.provider_nit
#     }

#     conn.execute(category_model.update().where(category_model.c.provider_id == provider_id).values(updated_values))
#     conn.commit()

#     return JSONResponse(content={"message": "Provider updated successfully"})

@category_router.delete("/categories/{category_id}")
def delete_provider(category_id: int):
    # result = conn.execute(category_model.select().where(category_model.c.category_id == category_id)).fetchone()

    # if result is None:
    #     raise HTTPException(status_code=404, detail="Provider not found")

    conn.execute(category_model.delete().where(category_model.c.category_id == category_id))
    conn.commit()

    return JSONResponse(content={"message": "Provider deleted successfully"})


@category_router.get("/category/{category_id}")
def get_category_by_id(category_id: int):
    # Consultar el proveedor por su ID
    result = conn.execute(category_model.select().where(category_model.c.category_id == category_id)).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Provider not found")

    # Crear un diccionario con los datos del proveedor
    catgory_data = {
        "category_id": result.category_id,
        "category_name": result.category_id,
    }

    return JSONResponse(content=catgory_data)