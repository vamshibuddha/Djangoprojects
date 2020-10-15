from django.contrib import admin
from testapp.models import moviemodel
# Register your models here.
class Movieadmin(admin.ModelAdmin):
    list_display = ['rdate', 'name', 'hero', 'heroine', 'rating']
admin.site.register(moviemodel, Movieadmin)