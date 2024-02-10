from django.http import HttpResponse
def get_HeaderHelper(request, header_name):
    allheaders=request.META
    my_header_value=allheaders.get('HTTP_' +header_name.upper(), "Header not set")
    return HttpResponse(f"Value of '{header_name}': {my_header_value}")