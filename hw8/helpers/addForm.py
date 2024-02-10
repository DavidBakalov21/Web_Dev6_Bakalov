from django.shortcuts import render
def callForm(request):
    return render(request, 'form.html')
