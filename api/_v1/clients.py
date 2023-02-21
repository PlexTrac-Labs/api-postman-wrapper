from api import request_handler as request

def list_clients(base_url, headers):
    """
    This request retrieves **all** clients for a tenant that you are **authorized** to view.

The `instanceUrl` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| id | full client ID | client_1254 |
| doc_id | client ID | 1254 |
| data | available information on client, such as name | 1254, Karbo Industries, null |
    """
    name = "List Clients"
    root = "/api/v1"
    path = f'/client/list'
    return request.get(base_url, root, path, name, headers)

def get_client(base_url, headers, clientId):
    """
    This request retrieves information on a client for a tenant that you are **authorized** to view.

The `instanceUrl` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| name | client name | Karbo Industries |
| client_id | client ID | 1254 |
| tenant_id | tenant ID | 40632 |
| doc_type | type of data | client |
| users | list of users who have access to client (email, ID, and role) | [janepentester@plextrac.com](mailto:janepentester@plextrac.com), null, ADMIN |
    """
    name = "Get Client"
    root = "/api/v1"
    path = f'/client/{clientId}'
    return request.get(base_url, root, path, name, headers)

def create_client(base_url, headers, payload):
    """
    This request **creates** a new client within a tenant.

The `instanceUrl` is needed to execute the call, along with a client name, any associated tags, a client description, point of contact name, point of contact email address, and any desired custom fields.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | further validation | Client updated successfully. |
    """
    name = "Create Client"
    root = "/api/v1"
    path = f'/client/create'
    return request.post(base_url, root, path, name, headers, payload)

def update_client(base_url, headers, clientId, payload):
    """
    This request updates an existing client within a tenant.

The `instanceUrl` and `clientId` is needed to execute the call, along with the information to update:

*   client name
*   tags
*   client description
*   point of contact name
*   point of contact email address
*   custom fields
    

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | explanation of request | Client updated successfully. |
    """
    name = "Update Client"
    root = "/api/v1"
    path = f'/client/{clientId}'
    return request.put(base_url, root, path, name, headers, payload)

def delete_client(base_url, headers, clientId):
    """
    This request **removes** a client from a tenant.

The `instanceUrl` and `clientId` is needed to execute the call.

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of delete request | success |
| message | explanation of request | client deleted successfully |
    """
    name = "Delete Client"
    root = "/api/v1"
    path = f'/client/{clientId}'
    return request.delete(base_url, root, path, name, headers)

def add_client_logo(base_url, headers, clientId, payload):
    """
    This request **creates** a logo for a client. The file must be JPEG or PNG.

The `instanceUrl` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | further validation | Client Logo Updated |
    """
    name = "Add Client Logo"
    root = "/api/v1"
    path = f'/client/{clientId}/logo'
    return request.post(base_url, root, path, name, headers, payload)

def delete_client_logo(base_url, headers, clientId, payload):
    """
    This request **removes** a logo for a client.

The `instanceUrl` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | further validation | Client Logo Updated |
    """
    name = "Delete Client Logo"
    root = "/api/v1"
    path = f'/client/{clientId}/logo'
    return request.delete(base_url, root, path, name, headers, payload)

def get_client_findings(base_url, headers, clientId, payload, sev, limit, skip):
    """
    No description in Postman

    Query Parameters:
    sev: 'Critical', 'High', 'Medium', 'Low', or 'Informational' - example (Critical)
    limit: Integer: Num findings to return. Default 10, max 500 - example (10)
    skip: Integer: Index of finding to start from. Default 0 - example (0)
    """
    name = "Get Client Findings"
    root = "/api/v1"
    path = f'/client/{clientId}/topFlaws?sev={sev}?limit={limit}?skip={skip}'
    return request.get(base_url, root, path, name, headers, payload)

def get_multiple_clients_findings(base_url, headers, payload, limit, skip):
    """
    No description in Postman

    Query Parameters:
    limit: No description in Postman - example (50)
    skip: No description in Postman - example (50)
    """
    name = "Get Multiple Clients Findings"
    root = "/api/v1"
    path = f'/clients/topFlaws?limit={limit}?skip={skip}'
    return request.post(base_url, root, path, name, headers, payload)

def list_tenant_client_users(base_url, headers, tenantId, clientId):
    """
    This request **retrieves a list of all users** for a specific client.
    """
    name = "List Tenant Client Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/users'
    return request.get(base_url, root, path, name, headers)

def assign_user_to_client(base_url, headers, tenantId, clientId, payload):
    """
    DEPRECATED - See v2 Assign Users to Client

Known Bug

Will not honor the `role` or `classificationId` entered. Will instead set the client permission level the same as the users default level.

Assign a user to a client within your tenancy
    """
    name = "Assign User to Client"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/user/assign'
    return request.post(base_url, root, path, name, headers, payload)

def remove_user_from_client(base_url, headers, tenantId, clientId, payload):
    """
    Revoke a user's authorization from a client
    """
    name = "Remove User from Client"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/user/remove'
    return request.post(base_url, root, path, name, headers, payload)

def available_tenant_users(base_url, headers, tenantId, clientId):
    """
    No description in Postman
    """
    name = "Available Tenant Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/users/available'
    return request.get(base_url, root, path, name, headers)
