from django.contrib import admin
from .models import newuser

# Register your models here.
class newuserAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','username','city','mobile']

admin.site.register(newuser,newuserAdmin)

