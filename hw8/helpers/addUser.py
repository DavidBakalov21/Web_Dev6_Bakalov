from django.http import HttpResponse
def addUser(insert_data, collection):
    collection.insert_one({"realname":insert_data[0], "age":insert_data[1], "email":insert_data[2], "nickname":insert_data[3],"isAdmin":insert_data[4], "id":insert_data[5]})
    return HttpResponse("User was successfully added")


