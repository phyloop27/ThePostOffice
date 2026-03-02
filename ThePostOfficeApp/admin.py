from django.contrib import admin

from ThePostOfficeApp.models import *

# Register your models here.
admin.site.register(Courier)
admin.site.register(Address)
admin.site.register(Letters)
admin.site.register(Parcels)
admin.site.register(Prices)
admin.site.register(Names)
admin.site.register(Quantity)
admin.site.register(PostOfficeSales)

