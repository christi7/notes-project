from django.contrib import admin
from .models import Profile, Report
from django.contrib.auth.admin import UserAdmin



admin.site.register(Profile, UserAdmin)
