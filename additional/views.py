from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from additional.data import messages
from additional.helpers import set_cookie_helper, get_cookie_helper, set_header_helper, get_Header_helper
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
    title = request.GET.get('cookie')
    value = request.GET.get('val')
    return set_cookie_helper.set_cookieHelper(request, title, value)
def get_cookie(request, title):
    return get_cookie_helper.get_cookieHelper(request, title)

def set_Header(request):
    header_name = request.GET.get('header')
    header_value = request.GET.get('value')
    return set_header_helper.set_HeaderHelper(request, header_name, header_value)

def get_Header(request, header_name):
    return get_Header_helper.get_HeaderHelper(request, header_name)



