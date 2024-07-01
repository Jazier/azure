from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# Información del Service Principal
sp_tenant_id = "6d94013f-6c4c-484e-bbd7-2b95b7fe0f87"
sp_client_id = "82ba1b93-1278-41c2-b054-bbd6896538ea"
sp_client_secret_value = "bec8Q~OPIPNoN3wNFbRy9lhPoGLCIklGrS9RTblx"

# URL del Key Vault
vault_url = "https://mykeyvaultjazier.vault.azure.net/"

# Nombre del secreto que deseas leer
kv_secret_name = "secretnametest"

# Autenticación
credential = ClientSecretCredential(tenant_id=sp_tenant_id, client_id=sp_client_id, client_secret=sp_client_secret_value)

# Crear el cliente del Key Vault
secret_client = SecretClient(vault_url=vault_url, credential=credential)

# Obtener el secreto
secret = secret_client.get_secret(kv_secret_name)

# Imprimir el valor del secreto
print(f"El valor del secreto '{kv_secret_name}' es: {secret.value}")