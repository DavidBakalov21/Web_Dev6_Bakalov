from django.shortcuts import render
def PatchForm(request,id):
    return render(request, 'patchForm.html',{'id': id})
