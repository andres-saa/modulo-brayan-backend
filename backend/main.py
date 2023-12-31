from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product_router
from routes import files_router
from routes.provider import provider_router
from routes.product_photo import photo_router
from routes.category  import category_router
app = FastAPI()

# Configuración para permitir todos los orígenes (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(files_router.router)
app.include_router(provider_router)
app.include_router(photo_router)
app.include_router(category_router)

