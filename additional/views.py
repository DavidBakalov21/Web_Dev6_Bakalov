from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from additional.data import messages

# Create your views here.

def sendAll(request):
    return render(request, 'messagePage.html',{'items': messages.messages['messages']})

def sendImg(request):
    return render(request, 'imageStatic.html')

def sendOne(request, id):
    one_item_array=[]
    for i in messages.messages['messages']:
        if i['Userid']==id:
            one_item_array.append(i)
    if len(one_item_array)==0:
        return HttpResponse("Seems like there are no messages with such id")
    return render(request, 'messagePage.html',{'items': one_item_array})

@csrf_exempt
def postNew(request):
    data = json.loads(request.body)
    messages.messages["messages"].append(data)
    return JsonResponse(data)

@csrf_exempt
def Delete(request, id):
    newMessage=[]
    for i in messages.messages["messages"]:
        if i['Userid']!=id:
            newMessage.append(i)
    messages.messages["messages"]=newMessage
    return HttpResponse("Message is successfully deleted if it was present")

#hw7
def set_cookie(request):
    response=HttpResponse("Cookie")
    #response.set_cookie("my_cookie", "Hello from server")
    response.set_cookie("my_cookie", "Hello from server", httponly=True)
    return response
def get_cookie(request):
    my_cookie_value=request.COOKIES.get("my_cookie", "Cookie not set")
    return HttpResponse(f"value of my_cookie:{my_cookie_value}")


