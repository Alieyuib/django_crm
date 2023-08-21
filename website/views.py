from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm, ItemForm, VehicleForm, VehicleOwnerForm
from django.contrib.auth.models import User
from .models import Record, Items, Vehicle, Car
import random

def home(request):
    records = Record.objects.all()
    #  check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('vehicles')
        else:
            messages.success(request, 'There was an error logging in....')
            return redirect('vehicles')
        
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout....')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully register...')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        return render(request, 'customer.html', { 'customer': customer })

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if  request.method == 'POST':
            if form.is_valid:
                form.save()
                messages.success(request, 'Success...')
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to add record...')
        return redirect('home')

def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_data = Record.objects.get(id=pk)
        if delete_data:
            delete_data.delete()
            messages.success(request, 'Customer deleted....')
            return redirect('home')
        
def update_customer(request, pk):
    if request.user.is_authenticated:
        customer_data = Record.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=customer_data)
        if request.method == 'POST':
            form.save()
            messages.success(request, 'Record updated!!')
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to update record...')
        return redirect('home')

def add_item(request):
    if request.user.is_authenticated:
        form = ItemForm(request.POST or None)
        # customers = Record.objects.get()
        if request.method == 'POST':
            if form.is_valid:
                item = form.save(commit=False)
                item.code = "ITM" + "_" + str(random.randint(1111, 9999))
                item.owner = request.user.id
                item.save()
                messages.success(request, 'Item Added!!')
                return redirect('items')
        return render(request, 'add_item.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to add item...')
        return redirect('items')
    
def items(request):
    items = Items.objects.filter(owner=request.user.id)
    return render(request, 'items.html', {'items': items})

def item(request, pk):
    item = Items.objects.filter(id=pk).first()
    owner = User.objects.filter(id=item.owner).first()
    return render(request, 'item.html', {'item': item, 'owner': owner})

def delete_item(request, pk):
    if request.user.is_authenticated:
        item = Items.objects.filter(id=pk).first()
        if item.owner == request.user.id:
            item.delete()
            messages.success(request, 'Item Deleted!!')
            return redirect('items')
    else:
        return redirect('login')

def edit_item(request, pk):
    if request.user.is_authenticated:
        item_data = Items.objects.get(id=pk)
        form = ItemForm(request.POST or None, instance=item_data)
        if request.method == 'POST':
            form.save()
            messages.success(request, 'Item updated!!')
            return redirect('item', item_data.id)
        return render(request, 'update_item.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to update record...')
        return redirect('home')
    
def profile(request, pk):
    if request.user.is_authenticated:
        user_data = User.objects.filter(id=pk).first()
        return render(request, 'user_data.html', {'user_data': user_data})
    else:
        messages.success(request, 'You must be logged in to update record...')
        return redirect('home')

def new_vehicle(request):
    if request.user.is_authenticated:
        form = VehicleForm(request.POST or None)
        if request.method == 'POST':
            vehicle = form.save(commit=False)
            vehicle_vin = request.POST.get('vin')
            check_vin = Vehicle.objects.get(vin=vehicle_vin)
            if check_vin:
                messages.success(request, 'A Vehicle with thesame VIN is registered!!')
                return render(request, 'new_vehicle.html', {'form': form})
            else:
                vehicle.status = True
                vehicle.save()
                messages.success(request, 'Vehicle Added!!!')
                return redirect('new_vehicle')
        return render(request, 'new_vehicle.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to update record...')
        return redirect('home')

def vehicles(request):
    if request.method == "POST":
        q = request.POST.get("q")
        vehicles = Vehicle.objects.filter(vin=q)
    else:
        vehicles = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})

def vehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    cars = Car.objects.filter(owner=pk)
    return render(request, 'vehicle.html', {'vehicle': vehicle, 'cars': cars})

def vehicle_update(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if request.method == 'POST':
        # s = form.save(commit=False)
        # # s.form = request.POST.get('model')
        # s.save()
        form.save()
        messages.success(request, 'Vehicle Updated!!!')
        return redirect('vehicles')
    return render(request, 'update_vehicle.html', {'form': form, 'vehicle': vehicle})

def vehicle_delete(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    if vehicle:
        vehicle.delete()
        messages.success(request, 'Vehicle Deleted!!!')
        return redirect('vehicles')

def check_out(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        vehicle_id = request.POST.get('vehicle_id')
        vehicle = Car.objects.filter(id=car_id).update(status=False)
        if vehicle:
            messages.success(request, 'Vehicle Checked Out!!!')
            return redirect('vehicle', vehicle_id)

def check_in(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        vehicle_id = request.POST.get('vehicle_id')
        vehicle = Car.objects.filter(id=car_id).update(status=True)
        if vehicle:
            messages.success(request, 'Vehicle Checked In!!!')
            return redirect('vehicle', vehicle_id)

def search(request):
    if request.method == "POST":
        q = request.POST.get("q")
        vehicles = Vehicle.objects.get(model__exact=q)
        return render(request, 'vehicles.html', {'vehicles': vehicles})

def owner_vehicle(request, pk):
    form = VehicleOwnerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            car = form.save(commit=False)
            car.status = True
            car.owner = Vehicle.objects.get(id=pk)
            car.save() 
            messages.success(request, 'Vehicle Added')
            return redirect('vehicle', pk)
    return render(request, 'owner_vehicle.html', {'form': form, 'id': pk})