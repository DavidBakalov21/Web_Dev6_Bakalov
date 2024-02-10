from django.shortcuts import render
def updateForm(request,id):
    return render(request, 'updateWhole.html',{'id': id})
