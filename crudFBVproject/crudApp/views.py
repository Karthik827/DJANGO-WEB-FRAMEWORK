from django.shortcuts import render,redirect
from crudApp.models import Employee
from crudApp.forms import EmployeeForm

# Create your views here.
def retrive_view(request):
    employees = Employee.objects.all()
    return render(request,'testapp/home.html',{'employees':employees})


def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')


def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'testapp/update.html',{'employee':employee})
