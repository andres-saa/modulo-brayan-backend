from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta,engine


product_model = Table("products", meta,
                Column("product_id", Integer, primary_key=True),
                Column("product_name", String(255)),
                Column("product_description", String(255)),  # Cambiando a "product_description"
                Column("product_selling_price", Float, nullable=True),
                Column("product_purchase_price", Float, nullable=True),
                )


meta.create_all(engine)