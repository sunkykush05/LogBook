from django.contrib import admin
from .models import InventoryModel, AttorneyModel

# Register your models here.
admin.site.register(InventoryModel)
admin.site.register(AttorneyModel)