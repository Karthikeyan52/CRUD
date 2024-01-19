from django.shortcuts import redirect, render
from . import model


def home(request):
    return render(request, "home.html")


def create(request):
    data = model.Create.objects.all()
    logic = {'data': data}
    if request.method == "POST":
        x = model.Create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            contact=request.POST.get('contact')
        )
        if x is not None:
            x.save()
        return redirect('home')
    else:
        return render(request, "create.html", logic)
