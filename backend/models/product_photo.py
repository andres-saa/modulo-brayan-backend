from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta
from config.db import meta,engine

Product_photo_model = Table(
    "product_photos",
    meta,
    Column("photo_id", Integer, primary_key=True),
    Column("image_url", String(255)),
    Column("product_id", ForeignKey("products.product_id")),  # Relación con la tabla de productos
)

meta.create_all(engine)