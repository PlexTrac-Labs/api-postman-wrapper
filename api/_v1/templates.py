from api import request_handler as request

def list_report_templates(base_url, headers, tenantId):
    """
    This request **lists all report templates** for a tenant.
    """
    name = "List Report Templates"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-templates'
    return request.get(base_url, root, path, name, headers)

def get_report_template(base_url, headers, tenantId, reportTemplateId):
    """
    This request **retrieves a specific report template** within a tenant.
    """
    name = "Get Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template/{reportTemplateId}'
    return request.get(base_url, root, path, name, headers)

def create_report_template(base_url, headers, tenantId, payload):
    """
    This request **creates** **a report template** within a tenant.
    """
    name = "Create Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template'
    return request.put(base_url, root, path, name, headers, payload)

def update_report_template(base_url, headers, tenantId, reportTemplateId, payload):
    """
    This request **updates** **a report template** within a tenant.
    """
    name = "Update Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template/{reportTemplateId}'
    return request.put(base_url, root, path, name, headers, payload)

def delete_report_template(base_url, headers, tenantId, reportTemplateId):
    """
    No description in Postman
    """
    name = "Delete Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template/{reportTemplateId}'
    return request.delete(base_url, root, path, name, headers)

def list_findings_templates(base_url, headers):
    """
    This request **lists all findings templates** for a tenant.
    """
    name = "List Findings Templates"
    root = "/api/v1"
    path = f'/field-templates'
    return request.get(base_url, root, path, name, headers)

def get_findings_template(base_url, headers, findingTemplateId):
    """
    This request retrieves **a findings template**
    """
    name = "Get Findings Template"
    root = "/api/v1"
    path = f'/field-template/{findingTemplateId}'
    return request.get(base_url, root, path, name, headers)

def create_finding_template(base_url, headers, tenantId, payload):
    """
    This request **creates** **a findings template** within a tenant.
    """
    name = "Create Finding Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/field-template'
    return request.put(base_url, root, path, name, headers, payload)

def update_finding_template(base_url, headers, tenantId, findingTemplateId, payload):
    """
    Update a finding template in your tenancy
    """
    name = "Update Finding Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/field-template/{findingTemplateId}'
    return request.put(base_url, root, path, name, headers, payload)

def delete_finding_template(base_url, headers, tenantId, findingTemplateId):
    """
    No description in Postman
    """
    name = "Delete Finding Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/field-template/{findingTemplateId}'
    return request.delete(base_url, root, path, name, headers)
