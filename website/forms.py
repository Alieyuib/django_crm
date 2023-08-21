from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record, Items, Vehicle, Car
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Email address'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First name'}), max_length=100)
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Last name'}), max_length=100)  

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Last name'}), max_length=100) 
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Email Address'}), max_length=100) 
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Phone Number'}), max_length=15) 
    address = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Address'}), max_length=100) 
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'City'}), max_length=100) 
    state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'State'}), max_length=100) 
    zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Zipcode'}), max_length=100) 

    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')

# class EditCustomerForm(forms.ModelForm):
#     first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First Name'}))
#     last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Last name'}), max_length=100) 
#     email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Email Address'}), max_length=100) 
#     phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Phone Number'}), max_length=15) 
#     address = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Address'}), max_length=100) 
#     city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'City'}), max_length=100) 
#     state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'State'}), max_length=100) 
#     zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Zipcode'}), max_length=100) 

#     class Meta:
#         model = Record
#         fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')

class ItemForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}), max_length=100)
    # code = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Code'}), max_length=100) 
    price = forms.FloatField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Price'}))  

    class Meta:
        model = Items
        fields = ('name', 'price')

class VehicleForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Owner First Name'}), max_length=100)
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Owner Last Name'}), max_length=100)
    model = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'BMW,AUDI,HONDA......'}), max_length=100)
    type = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Saloon,Sedan,SUV,Sport....'}), max_length=100)   
    vin = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'NSR-XXXDF'}), max_length=100)   
    color = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Maroon,Blue,Silver....'}), max_length=100) 
    phone = forms.CharField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : '+2348000000000'}))   
    address = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'No 15 Nil Street Unknown Location'}), max_length=100) 

    class Meta:
        model = Vehicle
        fields = ('first_name', 'last_name', 'type', 'model', 'vin', 'color', 'phone', 'address')

class VehicleOwnerForm(forms.ModelForm):
    model = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'BMW,AUDI,HONDA......'}), max_length=100)
    type = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Saloon,Sedan,SUV,Sport....'}), max_length=100)   
    vin = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'NSR-XXXDF'}), max_length=100)   
    color = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Maroon,Blue,Silver....'}), max_length=100) 

    class Meta:
        model = Car
        fields = ('type', 'model', 'vin', 'color')