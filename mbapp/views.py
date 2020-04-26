from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, AddEmpForm, UpdateEmpForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Employee
from django.contrib import messages

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('/')
    else:
        if request.POST.get('email')!="" and User.objects.filter(email=request.POST.get('email')).exists():
            return render(request, 'home.html', {'email_exist': 'true'})
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def show_emplist(request):
    form = AddEmpForm()
    query_list = Employee.objects.filter(manager=request.user.id)
    return render(request, 'home.html',{'emplist': query_list, 'form':form})

def add_emp(request):
    form = AddEmpForm(request.POST)
    if form.is_valid():
        manager = request.user.id
        params = {'fname': form.cleaned_data.get('first_name'), 
                    'lname':form.cleaned_data.get('last_name'), 
                    'address':form.cleaned_data.get('address'), 
                    'company':form.cleaned_data.get('company'), 
                    'manager': manager
                  } 
        Employee.objects.create(**params)
        messages.success(request, 'Employee was added')
        return redirect('/addemp')
    else:
        form = AddEmpForm()
        pass
    return render(request, 'home.html')

def delete_emp(request, emp_id = None):
    emp = Employee.objects.get(id=emp_id)
    emp.delete()
    messages.success(request, 'Employee was Deleted')
    return redirect('/addemp')

def update_render(request, emp_id):
    emp = Employee.objects.get(id=emp_id)
    return render(request, 'update_render.html', {'emp_details':emp})

def update_emp(request,emp_id):
    emp = Employee.objects.get(id=emp_id)
    form = UpdateEmpForm(request.POST, instance = emp)  
    if form.is_valid():
        form.save()
        messages.success(request, 'Employee was Updated')
        return redirect('/addemp')  
    return render(request, 'update_render.html', {'emp_details': emp})






