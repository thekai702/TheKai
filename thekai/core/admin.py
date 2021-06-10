from django.contrib import admin
from django.http import request
from django.shortcuts import render

from core.models import Profile

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display =(
#         "name","email",
#     )
