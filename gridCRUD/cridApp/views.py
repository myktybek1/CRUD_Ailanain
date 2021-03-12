from  .forms import EmployerForm
from django.shortcuts import render, redirect
from .models import Employer

def addnew(request):
    if request.method =="POST":
        form = EmployerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployerForm()
    return render(request, 'cridApp/index.html', {'form': form})

def index(request):
    employees= Employer.objects.all()
    return render (request, 'cridApp/show.html', {'employees': employees})

def edit(request, id):
    employees= Employer.objects.get(id=id)
    return render(request, 'cridApp/edit.html', {'employees': employees})

def update(request, id):
    employees = Employer.objects.get(id=id)
    form = EmployerForm(request.POST, instance=employees)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'cridApp/edit.html', {'employees': employees})

def destroy(request, id):
    employee = Employer.objects.get(id=id)
    employee.delete()
    return redirect("/")




# Create your views here.
