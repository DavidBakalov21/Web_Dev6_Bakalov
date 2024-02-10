from django.http import HttpResponse
def set_cookieHelper(request, title, value):
    response = HttpResponse(title)
    response.set_cookie(title, value, httponly=True)
    return response