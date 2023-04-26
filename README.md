# api-postman-wrapper
> It is recommended to use the base-API-script repo over this lite option.

An SDK lite version of the endpoints listed in the PT Postman Collection for use in Python scripting. This set of functions was generated from the Postman Collection JSON export.

This collection of files and functions acts as a wrapper for the Python requests module. It creates a function containing the description and URL for each request in Postman. When developing a Python script that needs to send API requests to a Plextrac instance, this collection allows you to write the script more directly without having so jump back and forth between Postman to copy the URL needed for a request.

## Instructions
1. Add the `api` folder to any Python script project
2. Add the import statement `import api` on any Python files where you want to make an API call
3. Write your API calls directly in the file

If your IDE has correctly found the api folder you can start typing `api.` and then auto complete should display your options.
![image](https://user-images.githubusercontent.com/88407273/220484222-af42c024-8333-4267-b139-e82ca09c20f1.png)

The structure to find endpoints is the same as the Postman folder structure. So to call the `Get Findings` endpoint, in the Postman folders `v1/Findings` you can write `api._v1.findings.get_finding()`. You can then hover over the function name and your IDE should display the parameters the function needs to successfully make the call through the Python requests module. It will also show the Postman description.
![image](https://user-images.githubusercontent.com/88407273/220484551-bc96351a-eee3-41ef-ab99-8c77e4079404.png)

**Note:** All folder and request names have been stripped of special characters and lowercased. You should be able to find a certain request by following the Postman folder structure.

**Note:** This function call is just a wrapper for the Python requests module. This means that writing this line is the same as manually calling the corresponding requests function and will return a Response object from the requests module.

### Function Parameters
The parameters the function needs will always include the base_url and the headers. Additional parameters will be needed if there are any variables in the URL or if the request needs any query parameters.

The `base_url` is the URL to your instance of Plextrac. e.x. `https://example.plextrac.com`

The `headers` is the JSON needed containing authentication information. e.x.
```
{
    "Authorization": "eyJhbGci..."
}
```
