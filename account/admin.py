from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, StudentProfile


class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the list view of the admin panel
    list_display = ('email', 'role', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email', 'role', 'phone_number')
    ordering = ('email',)

    # Define the layout of fields in the admin form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Roles and Permissions', {'fields': ('role', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_active')},
         ),
    )

class StudentProfileAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view of the admin panel
    list_display = ('user', 'sex', 'age', 'city')
    list_filter = ('sex', 'age', 'city')
    search_fields = ('user__username', 'user__email', 'city')
    ordering = ('user',)


# Register the models and their admin classes
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
