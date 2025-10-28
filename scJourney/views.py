from django.shortcuts import render

def index(request):
    return render(request, 'scjourney/index.html')

def aboutMe(request):
    return render(request, 'scjourney/aboutMe.html')
