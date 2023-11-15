from fastapi import APIRouter, UploadFile,FastAPI, File,Form,BackgroundTasks
from fastapi.responses import FileResponse
from os import getcwd
from os.path import splitext
from pathlib import Path
# from model.files_connection import siteDocumentConnection
# from schema.site_document_schema import SiteDocumentSchemaPost,SiteDocumentSchema
from PIL import Image

# conn = siteDocumentConnection()

router = APIRouter()


def resize_image(path:str,upload_dir:str,product_id:str,file_extension:str):
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

    for size in sizes:
        upload_dir.mkdir(parents=True, exist_ok=True)
        size_defined = size["width"], size["height"]
        image =  Image.open(path, mode='r')
        image.thumbnail(size_defined)
        file_path = upload_dir / ( " product image " + product_id + " "+ str(size["width"]) + 'x' + str(size["height"]) + file_extension)
        image.save(file_path)
        print(file_extension)
        



@router.get("/")
def root():
    return "hola"

@router.post('/upload-product-image/{product_id}')
async def upload_user_photo(product_id: str, file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks):
    # Obtener la extensión del archivo
    file_extension = splitext(file.filename)[1]

    # Directorio donde se guardarán las imágenes
    upload_dir = Path(getcwd()) / "files" / "images" / "products" / product_id

    # Crear la carpeta "users" si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / ( " product image " + product_id + file_extension)

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)
        myflle.close()

    background_tasks.add_task(resize_image,file_path,upload_dir,product_id,file_extension)

    return "hecho"






@router.get('/read_product_image/{height}/{product_id}')
def get_photo_profile(product_id: str,height:str):
    base_dir = getcwd() + "/files" + "/images" + "/products" + "/" + product_id

    # Lista de extensiones de archivo a buscar en orden de preferencia
    file_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

    for extension in file_extensions:
        file_path = base_dir + "/" + " product image " + product_id + " " + height+"x"+height + extension
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

