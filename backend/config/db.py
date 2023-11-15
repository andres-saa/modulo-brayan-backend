from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtén las credenciales de la base de datos desde las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Construye la URL de la base de datos
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Crea el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

meta = MetaData()
conn = engine.connect()
# Puedes realizar operaciones de SQLAlchemy usando este engine
# Por ejemplo, puedes crear una tabla
# from sqlalchemy import Table, Column, Integer, String, MetaData

# metadata = MetaData()

# users = Table('users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('age', Integer),
# )

# # Crea la tabla en la base de datos (si no existe)
# metadata.create_all(engine)
