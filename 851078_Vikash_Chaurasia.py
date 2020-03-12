from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
#tenant Id
TENANT_ID = 'c04f95c6-2748-45e0-89b9-3c530a8c064a'
# Your Service Principal App ID
CLIENT = 'f6df6007-3d9a-4ed6-a09f-ae736-ed7462c'
# Your Service Principal Password
KEY = 'client secret'
credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

subscription_id = 'subscription_id'

compute_client = ComputeManagementClient(credentials, subscription_id)

rg = 'python_auto'
name = 'auto_project'
vmss = compute_client.virtual_machine_scale_set_vms.list(rg,name)
for i in vmss:
    print i.name
