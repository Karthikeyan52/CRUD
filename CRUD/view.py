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


def read(request):
    data = model.Create.objects.all()
    context = {'data': data}
    return render(request, "read.html", context)


def update(request, pk):
    data = model.Create.objects.get(pk=pk)
    context = {'data': data}
    if request.method == "POST":
        data.name = request.POST.get("name")
        data.email = request.POST.get("email")
        data.contact = request.POST.get("contact")
        data.save()
        return redirect('read')
    return render(request, "update.html", context)


def delete(request, pk):
    data = model.Create.objects.filter(pk=pk).first()
    data.delete()
    return redirect('read')

