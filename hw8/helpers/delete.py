from django.http import HttpResponse
def delete(id,collection):
    collection.delete_one({"id": id})
    return HttpResponse("Message is successfully deleted if it was present")