from django.http import HttpResponse
def PatchUser(data, collection):
    search={'id':data['id']}
    user = collection.find_one(search)
    data['id']=user['realname']+user['age']+user['email']+data['nickname']+user['isAdmin']
    updated = {"$set": data}
    collection.update_one(search, updated)
    return HttpResponse("User was successfully updated")
