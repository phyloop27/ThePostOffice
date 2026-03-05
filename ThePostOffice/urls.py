from django.contrib import admin
from django.urls import path, include
from ThePostOfficeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'), # Remove this On completion!! Change to Login page!!!!

    path('formName/', views.formName, name='formName'),

    path("formLetter/<int:name_id>/", views.formLetter, name="formLetter"),

    path('formParcel/<int:name_id>/', views.formParcel, name='formParcel'),

    path('formSuccess', views.formSuccess, name='formSuccess'),

    path('customerDetails/', views.customerDetails, name='customerDetails'),

    path('postedItems/', views.postedItems, name='postedItems'),


    path("delete/<int:identifier>/", views.delete, name="delete"),


    path("update/<int:identifier>/", views.update, name="update"),
]
