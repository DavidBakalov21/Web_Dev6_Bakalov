from django.shortcuts import render
def showById(request,id,collection):
    user = collection.find_one({"id": id})
    return render(request, 'singleUser.html', {'item': user})
