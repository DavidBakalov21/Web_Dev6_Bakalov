import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hw8.helpers import displayAll
from hw8.helpers import mongoConnection, addForm, addUser, showOne, delete, updateForm, UpdateUser, PatchUser, PatchForm, Information
client=mongoConnection.get_mongo_collection()
def display(request):
    return displayAll.displayAll(request,client)

def AddForm(request):
    return addForm.callForm(request)

def showById(request,id):
    return showOne.showById(request,id,client)

def UpdateForm(request,id):
    return updateForm.updateForm(request,id)

def Patch_Form(request,id):
    return PatchForm.PatchForm(request,id)
def Info(request):
    return Information.Info(request)
@csrf_exempt
def postNew(request):
    if request.method == 'POST':
        realname = request.POST.get('realname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')
        isAdmin=request.POST.get('isAdmin')
        if isAdmin!='True':
            isAdmin='False'
        id=realname+age+email+nickname+isAdmin
        return addUser.addUser([realname,age,email,nickname,isAdmin,id],client)
    else:
        return HttpResponse("Please don't access this endpoint manually")
@csrf_exempt
def Delete(request):
    if request.method=="DELETE":
        data = json.loads(request.body)
        item_id = data.get('id')
        return delete.delete(item_id,client)
    else:
        return HttpResponse("Please don't access this endpoint manually")
#CSRF was working very bad, it basically didn't allow me to do anything so I decided to work with POST method
@csrf_exempt
def Update_User(request):
    if request.method == "POST":
        realname = request.POST.get('realname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')
        isAdmin = request.POST.get('isAdmin')
        id=request.POST.get('firstId')
        if isAdmin!='True':
            isAdmin='False'
        data={"realname": realname, "age": age, "email": email, "nickname": nickname,
         "isAdmin": isAdmin, "id":  id}
        return UpdateUser.UpdateUser(data, client)
    else:
        return HttpResponse("Please don't access this endpoint manually")

#CSRF was working very bad, it basically didn't allow me to do anything so I decided to work with POST method
@csrf_exempt
def Patch_User(request):
    if request.method == "POST":
        nickname = request.POST.get('nickname')
        id = request.POST.get('firstId')
        data={"nickname": nickname, "id":  id}
        return PatchUser.PatchUser(data, client)
    else:
        return HttpResponse("Please don't access this endpoint manually")




