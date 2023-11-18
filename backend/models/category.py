from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta,engine




category_model = Table("categories", meta,
                Column("category_id", Integer, primary_key=True),
                Column("category_name", String(255)),
                
                )


meta.create_all(engine)
