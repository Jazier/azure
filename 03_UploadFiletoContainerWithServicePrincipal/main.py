from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Información del Service Principal
sp_tenant_id = "6d94013f-6c4c-484e-bbd7-2b95b7fe0f87"
sp_client_id = "82ba1b93-1278-41c2-b054-bbd6896538ea"
sp_client_secret_value = "bec8Q~OPIPNoN3wNFbRy9lhPoGLCIklGrS9RTblx"

# Información de la cuenta de almacenamiento
storage_account_url = "https://storageaccountjazier.blob.core.windows.net/"
container_name = "containerforlearning"
blob_name = "example03.txt"  # Nombre del archivo en el contenedor
local_file_path = "C:/Users/Administrator/Desktop/azure/03_UploadFiletoContainerWithServicePrincipal/mytext.txt"  # Ruta al archivo local

# Autenticación
credential = ClientSecretCredential(tenant_id=sp_tenant_id, client_id=sp_client_id, client_secret=sp_client_secret_value)

# Crear el cliente de BlobService
blob_service_client = BlobServiceClient(storage_account_url, credential=credential)

# Crear el cliente del contenedor
container_client = blob_service_client.get_container_client(container_name)

# Crear el cliente del blob
blob_client = container_client.get_blob_client(blob_name)

# Subir el archivo
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Archivo subido a {blob_name} en el contenedor {container_name}.")