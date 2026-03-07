from django.contrib import admin
from django.urls import path, include
from ThePostOfficeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.landing, name='landing'),

    path('staffLogin/', views.staffLogin, name='staffLogin'),

    path("staffLogout/", views.staffLogout, name="logout"),

    path('home/', views.home, name='home'),

    path('formName/', views.formName, name='formName'),

    path("formLetter/<int:name_id>/", views.formLetter, name="formLetter"),

    path('formParcel/<int:name_id>/', views.formParcel, name='formParcel'),

    path('formSuccess', views.formSuccess, name='formSuccess'),

    path('customerDetails/', views.customerDetails, name='customerDetails'),

    path('postedItems/', views.postedItems, name='postedItems'),

    path('fullRecord/<int:identifier>/', views.fullRecord, name='fullRecord'),


    path("delete/<int:identifier>/", views.delete, name="delete"),


    path("update/<int:identifier>/", views.update, name="update"),
]
