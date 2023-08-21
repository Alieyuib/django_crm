from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

class Items(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100) 
    code = models.CharField(max_length=100)
    price = models.FloatField()
    owner = models.IntegerField()

    def __str__(self):
        return (f"{self.name} {self.code} {self.owner}")

class Vehicle(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    vin = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return (f"{self.model} {self.vin} {self.type} {self.phone}")

class Car(models.Model):
    model = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    vin = models.CharField(max_length=100, blank=True, unique=True)
    color = models.CharField(max_length=100, blank=True)
    # address = models.CharField(max_length=200, blank=True)
    # phone = models.CharField(max_length=15, blank=True)
    status = models.BooleanField()
    owner = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True)