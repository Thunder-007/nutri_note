from django.contrib import admin
from .models import DiveUser, ReachedLimit

# Register your models here.

admin.site.register(DiveUser)
admin.site.register(ReachedLimit)
