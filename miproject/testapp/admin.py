from django.contrib import admin
from testapp.models import ContactInfo01, Student01, Teacher01, Parent, Child, SubChild
# Register your models here.

'''
class ContactInfo01Admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address']

class Student01Admin(admin.ModelAdmin):
    list_display = ['rollno', 'marks']

class Teacher01Admin(admin.ModelAdmin):
    list_display = ['subject', 'salary']
'''

admin.site.register(ContactInfo01)
admin.site.register(Student01)
admin.site.register(Teacher01)

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SubChild)