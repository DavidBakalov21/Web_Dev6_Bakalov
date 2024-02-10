from django.shortcuts import render
def displayAll(request, collection):
    documents = collection.find()
    documents_list = [doc for doc in documents]
    return render(request, 'displayAll.html', {'items': documents_list})
