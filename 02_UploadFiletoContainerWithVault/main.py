import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient


load_dotenv()

# Configuración
connection_string = os.environ["CONNECTION_STRING"]
container_name = "containerforlearning"
local_file_path = "C:/Users/Jazier/Desktop/Azure/01_UploadFiletoContainerWithKey/mytext.txt"
blob_name = "mytextcopied.txt"

# Crear el cliente de BlobService
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Crear el cliente del contenedor
container_client = blob_service_client.get_container_client(container_name)

# Crear el cliente del blob
blob_client = container_client.get_blob_client(blob_name)

# Subir el archivo
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Archivo {local_file_path} subido a {blob_name} en el contenedor {container_name}.")