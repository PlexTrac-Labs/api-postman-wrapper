from api import request_handler as request

def get_report_list(base_url, headers, payload):
    """
    This request **retrieves a list of reports** for a tenant.

{  
pagination: { // required object with keys "offset" & "limit"  
offset: 0, // required number, default 0  
limit: 25, // required number valid \[5, 25, 50, 100\]  
},  
sort: \[ // optional array of objects with keys "by" & "order"  
{  
by: "asset", // required string  
order: "DESC", // required one of "ASC" | "DESC"  
},  
\],  
filters: \[ // optional array of object with keys "by" & "value"  
{  
by: "asset", // required string  
value: "ba", // required string allows "empty string" if filtering by "tags" must be array of strings  
},  
\],  
}
    """
    name = "Get Report List"
    root = "/api/v2"
    path = f'/reports'
    return request.post(base_url, root, path, name, headers, payload)
