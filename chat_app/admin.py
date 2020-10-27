from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


from import_export.admin import ImportExportModelAdmin
# Register your models here.

# main account


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

# for import export


class Unreg_studentsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'institute')


admin.site.register(Account, AccountAdmin)
admin.site.register(Institute)
admin.site.register(Unreg_students, Unreg_studentsAdmin)
