from django.contrib import admin

from ThePostOfficeApp.models import *

# Register your models here.
admin.site.register(Name)
admin.site.register(Address)
admin.site.register(Letter)
admin.site.register(Parcel)



