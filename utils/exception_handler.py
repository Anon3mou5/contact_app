from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    print(response.data)
    if(response.data.get('email')):
        pass
    elif('page' in (response.data.get('detail')) if(response.data.get('detail')) else 'none'):
        response.data = {
            "message": "The request page no is out of bound",
            "error": "Invalid Page No Error",
        }
    elif response is not None and response.status_code == 404:
        response.data = {
            "message": "The requested object is not found.",
            "error": "HTTP_404_NOT_FOUND",
        }

    return response
