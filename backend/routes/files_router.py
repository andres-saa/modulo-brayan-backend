from fastapi import APIRouter, UploadFile,FastAPI, File,Form,BackgroundTasks
from fastapi.responses import FileResponse
from os import getcwd
from os.path import splitext
from pathlib import Path
# from model.files_connection import siteDocumentConnection
# from schema.site_document_schema import SiteDocumentSchemaPost,SiteDocumentSchema
from PIL import Image
from sqlalchemy import select, func
from config.db import conn
from models.product_photo import Product_photo_model
import sqlalchemy
from config.db import engine
# conn = siteDocumentConnection()

router = APIRouter()


def resize_image(sizes,upload_dir:str,image_path, extension,file_path):
    

    for size in sizes:
        upload_dir.mkdir(parents=True, exist_ok=True)
        size_defined = size["width"], size["height"]
        image =  Image.open(file_path, mode='r')
        image.thumbnail(size_defined)
        new_file_path = upload_dir / ((str(size["height"]) + 'p' )+ "-"+image_path + extension)
        image.save(new_file_path)
    # print ("hola" )
    # print(upload_dir)
        # print(new_file_path)



@router.get("/")
def root():
    return "hola"

@router.post('/upload-product-image/{product_id}')
async def upload_user_photo(product_id: str, file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks):
    # Obtener la extensión del archivo
    
    # conn.execute(Product_photo_model.select().where(Product_photo_model.c.product_id == 1)).fetchone()

    # Obtener el resultado
    sizes = [
        {
            "width":96,
            "height":96
        },
        {
            "width":300,
            "height":300
        },
        {
            "width":600,
            "height":600
        },  
    ]
    
    try:
        product_id_photo = int(product_id)
    except ValueError:
        print("product_id no es un número entero válido.")
        # Puedes manejar el error de alguna manera apropiada para tu aplicación

    num_fotos = 0
    next_photo = 0
    
    # Solo ejecutar la consulta si product_id es un número entero válido
    if isinstance(product_id_photo, int):
        result = conn.execute(Product_photo_model.select().where(Product_photo_model.c.product_id == product_id)).fetchall()
        # Hacer algo con el resultado, por ejemplo, imprimirlo
        num_fotos = len(result)
        next_photo = num_fotos + 1
        # print(num_fotos)


    query_last_id = select((sqlalchemy.sql.functions.max(Product_photo_model.c.photo_id)))
    last_id = conn.execute(query_last_id).scalar()
    next_photo = last_id

    file_extension = splitext(file.filename)[1]

    # Directorio donde se guardarán las imágenes
    upload_dir = Path(getcwd()) / "files" / "images" / "products" / product_id

    # Crear la carpeta "users" si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Combinar el nombre del archivo con el directorio
    image_path = ( "product_image-" + product_id + "-"+ str(next_photo) + file_extension)
    file_path = upload_dir / image_path

    image_path_no_extension = ( "product_image-" + product_id + "-"+ str(next_photo))
    # image_url =( "product_image-" + product_id + "-"+ str(next_photo) + file_extension)
    new_photo = {
    "image_url": image_path,
    "product_id": product_id
    }

    print(new_photo)

    result_query_photo = conn.execute(Product_photo_model.insert().values(new_photo))
    conn.commit()

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)
        myflle.close()
    # print(file_path)

    background_tasks.add_task(resize_image,sizes,upload_dir,image_path_no_extension,file_extension,file_path)

    

    return "hecho"






@router.get('/read_product_image/{product_id}/{height}/{image_url}')
def get_photo_profile(product_id: str,height:str,image_url):
    base_dir = getcwd() + "/files" + "/images" + "/products" + "/" + product_id

    # Lista de extensiones de archivo a buscar en orden de preferencia
    

   
    file_path = base_dir + "/"  + height+"p" +"-" + image_url
    print(file_path)
    file = Path(file_path)

    if file.exists():
        return FileResponse(file)

    # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
    return "Archivo no encontrado", 404














# @router.post('/upload-site-documet/')
# async def upload_user_photo(site_name: str = Form(...), type_document: str = Form(...), file: UploadFile = File(...)):
#     # Obtener la extensión del archivo
#     file_extension = splitext(file.filename)[1]

#     # Directorio donde se guardarán las imágenes
#     upload_dir = Path(getcwd()) / "files" / "documents" / "sites" / site_name

#     # Crear la carpeta "users" si no existe
#     upload_dir.mkdir(parents=True, exist_ok=True)

#     # Combinar el nombre del archivo con el directorio
#     file_path = upload_dir / (site_name + " " + type_document + file_extension)

#     with open(file_path, "wb") as myflle:
#         content = await file.read()
#         myflle.write(content)

#     return "hecho"

# @router.get("/get-site-document/{site_name}/{type_document}")
# def get_site_document(site_name: str, type_document: str):
#     base_dir = getcwd() + "/files" + "/documents" + "/sites" + "/" + site_name + "/"

#     # Lista de extensiones de archivo a buscar en orden de preferencia
#     file_extensions = ['.pdf', '.jpg', '.jpeg', '.gif', '.bmp']

#     for extension in file_extensions:
#         file_path = base_dir + "/" + site_name + " " + type_document + extension
#         print (file_path)
#         file = Path(file_path)

#         if file.exists():


#             return FileResponse(file)
                   
    

#     print(base_dir)
#     # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
#     return "Archivo no encontrado", 404


# @router.get("/get-site-documents-info/{site_id}")
# def get_site_documents_info(site_id: str):
#     data = conn.read_all(site_id)
#     return data
                   

# @router.post("/insert/site-document")
# def insert(site_data:SiteDocumentSchemaPost):
#     data = site_data.dict()
    
#     print(data)
#     return conn.write(data)


# @router.put("/update/site-document/{document_id}")
# def update(site_data:SiteDocumentSchemaPost,document_id:str):
#     data = site_data.dict()
#     data['document_id'] = document_id

#     print(data)
#     return conn.update(data)





# @router.post('/upload-site-cover/')
# async def upload_user_photo(site_name: str = Form(...), file: UploadFile = File(...)):
#     # Obtener la extensión del archivo
#     file_extension = splitext(file.filename)[1]

#     # Directorio donde se guardarán las imágenes
#     upload_dir = Path(getcwd()) / "files" / "images" / "sites" / site_name

#     # Crear la carpeta "users" si no existe
#     upload_dir.mkdir(parents=True, exist_ok=True)

#     # Combinar el nombre del archivo con el directorio
#     file_path = upload_dir / ( "site cover"  + file_extension)

#     with open(file_path, "wb") as myflle:
#         content = await file.read()
#         myflle.write(content)




#     return "hecho"


# @router.get('/read-site-cover/{site_name}')
# def get_photo_profile(site_name: str):
#     base_dir = getcwd() + "/files" + "/images" + "/sites" + "/" + site_name + "/"

#     # Lista de extensiones de archivo a buscar en orden de preferencia
#     file_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

#     for extension in file_extensions:
#         file_path = base_dir +  "site cover" + extension
#         print (file_path)
#         file = Path(file_path)

#         if file.exists():
#             return FileResponse(file)

#     print(base_dir)
#     # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
#     return "Archivo no encontrado", 404

