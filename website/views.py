from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.core.paginator import Paginator

def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "You Must be Logged In First...")
        return redirect('login')

    records = Record.objects.all()
    paginator = Paginator(records, 5)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hello <strong>{user.username}</strong>, You have been logged In!")
            return redirect('home')
        else:
            messages.error(request, "Incorrect username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out ....")
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Successfully Registered! Please Login!")
            return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
         messages.success(request, "You Must be Logged In to view that page..")
         return redirect('login')
     
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records Delete Succesfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Delete The Record")
        return redirect('home')
    
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Data added successfully...")
                return redirect('home')  
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must be Logged In...")
        return redirect('login') 


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must be Logged In...")
        return redirect('login') 


