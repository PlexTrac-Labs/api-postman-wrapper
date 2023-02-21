from api import request_handler as request

def update_settings(base_url, headers, tenantId, payload):
    """
    No description in Postman
    """
    name = "Update settings"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/settings'
    return request.put(base_url, root, path, name, headers, payload)
