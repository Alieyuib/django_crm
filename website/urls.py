from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_user'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_item/', views.add_item, name='add_item'),
    path('items/', views.items, name='items'),
    path('item/<int:pk>/', views.item, name='item'),
    path('item/delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('item/edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('new-vehicle/', views.new_vehicle, name='new_vehicle'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicle/<int:pk>/', views.vehicle, name='vehicle'),
    path('vehicle-update/<int:pk>/', views.vehicle_update, name='vehicle_update'),
    path('vehicle-delete/<int:pk>/', views.vehicle_delete, name='vehicle_delete'),
    path('vehicle-checkout/', views.check_out, name='check_out'),
    path('vehicle-checkin/', views.check_in, name='check_in'),
    path('search/', views.search, name='search'),
    path('owner_vehicle/<int:pk>/', views.owner_vehicle, name='owner_vehicle'),
]
