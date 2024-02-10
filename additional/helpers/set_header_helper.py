from django.http import HttpResponse
def set_HeaderHelper(request, header_name, header_value):
    response = HttpResponse(header_name,content_type="text/plain")
    response[header_name] = header_value
    return response
