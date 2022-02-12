# Rest API Example HTTP Serverless Azure Function

Setup and example taken from blog post of Bahrgav Baching 
[How To Write Serverless Python REST API With Azure Functions](https://medium.com/bb-tutorials-and-thoughts/how-to-write-serverless-python-rest-api-with-azure-functions-504c0113c1c8)

If you configure App Registration automatically as described in [Configure your App Service or Azure Functions app to use Azure AD login](https://docs.microsoft.com/en-gb/azure/app-service/configure-authentication-provider-aad) use URL below to login via browser and receive cookie in browser to use function app:
```
https://login.microsoftonline.com/<tenanti-id>/oauth2/v2.0/authorize?response_type=code&client_id=<client-id>&redirect_uri=https://<function_name>.azurewebsites.net/.auth/login/aad/callback&scope=openid
```
**Remark**

Redirect URL is automatically generated as well as client secret. The name of the App Registration is the same as the name of the function application. Client secret is also automatically created and saved as configuraiton variable MICROSOFT_PROVIDER_AUTHENTICATION_SECRET.

Working example:

https://login.microsoftonline.com/41c58ae6-2fc8-43d0-ba98-f14d3a4aeba5/oauth2/v2.0/authorize?response_type=code&client_id=da30267d-17f4-4cc9-abac-59fe40f8f594&redirect_uri=https://fcrpythonrestapi.azurewebsites.net/.auth/login/aad/callback&scope=openid