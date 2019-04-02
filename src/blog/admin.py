from django.contrib import admin

# Register your models here.
from .models import BlogPost


admin.site.register(BlogPost)