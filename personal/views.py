from django.shortcuts import render

# Create your views here.
def home_screen(request,*args,**kwargs):
    return render(request,"personal/home.html",{

    })