from fastapi import APIRouter
from config.db import conn
from models.provider import provider_model
from schema.provider import provider_schema_post
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
import json  # Asegúrate de tener este import en tu código

provider_router = APIRouter()

@provider_router.get("/providers")
def get_providers():
    result = conn.execute(provider_model.select()).fetchall()

    provider_data_list = []
    for row in result:
        provider_data = {
            "provider_id": row.provider_id,
            "provider_name": row.provider_name,
            "provider_address": row.provider_address,
            "provider_contact": row.provider_contact,
            "provider_nit": row.provider_nit
        }
        provider_data_list.append(provider_data)

    return JSONResponse(content=provider_data_list)

    # return JSONResponse(json_data)

@provider_router.post("/providers")
def create_provider(provider: provider_schema_post):
    new_provider = {
        "provider_name": provider.provider_name,
        "provider_address": provider.provider_address,
        "provider_contact": provider.provider_contact,
        "provider_nit": provider.provider_nit,
    }

    result = conn.execute(provider_model.insert().values(new_provider))
    conn.commit()

    return JSONResponse(content={"message": "Provider created successfully"})

@provider_router.put("/providers/{provider_id}")
def update_provider(provider_id: int, updated_provider: provider_schema_post):
    result = conn.execute(provider_model.select().where(provider_model.c.provider_id == provider_id)).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Provider not found")

    updated_values = {
        "provider_name": updated_provider.provider_name,
        "provider_address": updated_provider.provider_address,
        "provider_contact": updated_provider.provider_contact,
        "provider_nit": updated_provider.provider_nit
    }

    conn.execute(provider_model.update().where(provider_model.c.provider_id == provider_id).values(updated_values))
    conn.commit()

    return JSONResponse(content={"message": "Provider updated successfully"})

@provider_router.delete("/providers/{provider_id}")
def delete_provider(provider_id: int):
    result = conn.execute(provider_model.select().where(provider_model.c.provider_id == provider_id)).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Provider not found")

    conn.execute(provider_model.delete().where(provider_model.c.provider_id == provider_id))
    conn.commit()

    return JSONResponse(content={"message": "Provider deleted successfully"})


@provider_router.get("/providers/{provider_id}")
def get_provider_by_id(provider_id: int):
    # Consultar el proveedor por su ID
    result = conn.execute(provider_model.select().where(provider_model.c.provider_id == provider_id)).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Provider not found")

    # Crear un diccionario con los datos del proveedor
    provider_data = {
        "provider_id": result.provider_id,
        "provider_name": result.provider_name,
        "provider_address": result.provider_address,
        "provider_contact": result.provider_contact,
        "provider_nit": result.provider_nit
    }

    return JSONResponse(content=provider_data)