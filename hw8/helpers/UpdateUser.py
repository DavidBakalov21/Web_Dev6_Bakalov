from django.http import HttpResponse
def UpdateUser(data, collection):
    search={'id':data['id']}
    data['id']=data['realname']+data['age']+data['email']+data['nickname']+data['isAdmin']
    updated = {"$set": data}
    collection.update_one(search, updated)
    return HttpResponse("User was successfully updated")
