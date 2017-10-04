from django.contrib import admin
from .models import User, Community


# Register your models here.
admin.site.register(User)
admin.site.register(Community)