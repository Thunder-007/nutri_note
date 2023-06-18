from django.contrib import admin
from .models import DiveUser, ReachedLimit, Food

# Register your models here.

admin.site.register(DiveUser)
admin.site.register(ReachedLimit)
admin.site.register(Food)
