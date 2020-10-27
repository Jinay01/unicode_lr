from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'name', 'is_faculty', 'is_student', 'is_institute'
    )

    search_fields = (
        'email',
        'name',
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Institute)
# admin.site.register(Student)
