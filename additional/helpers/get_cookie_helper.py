from django.http import HttpResponse
def get_cookieHelper(request, title):
    my_cookie_value=request.COOKIES.get(title, "Cookie not set")
    return HttpResponse(f"value of my_cookie:{my_cookie_value}")