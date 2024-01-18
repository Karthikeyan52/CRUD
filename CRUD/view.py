from django.shortcuts import redirect, render


def home(request):
    return render(request, "home.html")
def create(request):
    return render(request,"create.html")