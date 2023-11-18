from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta,engine




provider_model = Table("providers", meta,
                Column("provider_id", Integer, primary_key=True),
                Column("provider_name", String(255)),
                Column("provider_address", String(255)),  # Cambiando a "product_description"
                Column("provider_contact", String(255)),
                Column("provider_nit", String(255)),
                )


meta.create_all(engine)
