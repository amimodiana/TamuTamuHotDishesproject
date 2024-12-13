from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')
def menu(request):
    return render(request,'menu.html')
def team(request):
    return render(request,'team.html')
