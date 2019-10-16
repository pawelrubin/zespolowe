# swagger_client.DefaultApi

All URIs are relative to *http://api.mathjs.org/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](DefaultApi.md#root_get) | **GET** / | Calculate given expression with GET
[**root_post**](DefaultApi.md#root_post) | **POST** / | Calculate given expression with POST

# **root_get**
> root_get(expr, precision=precision)

Calculate given expression with GET

Calculate expression given in a query parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
expr = 'expr_example' # str | The expression to be evaluated. The expression must be [url encoded](http://www.w3schools.com/tags/ref_urlencode.asp).
precision = 1.2 # float | Number of significant digits in formatted output. Undefined by default. (optional)

try:
    # Calculate given expression with GET
    api_instance.root_get(expr, precision=precision)
except ApiException as e:
    print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expr** | **str**| The expression to be evaluated. The expression must be [url encoded](http://www.w3schools.com/tags/ref_urlencode.asp). | 
 **precision** | **float**| Number of significant digits in formatted output. Undefined by default. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> Response root_post(body=body)

Calculate given expression with POST

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Request() # Request |  (optional)

try:
    # Calculate given expression with POST
    api_response = api_instance.root_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->root_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Request**](Request.md)|  | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

