from django.shortcuts import render
from hw6.data import info
from django.http import HttpResponse


def sendInfo(request):
    return render(request, 'main.html',{'items': info.info['info']})

def nothing(request):
    return HttpResponse("Nothing found")