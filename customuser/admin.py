from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'first_name', 'last_name', 
        'email', 'is_active', 'is_margin', 
        'favorite')

    list_filter = (
        'first_name', 'last_name', 
        'email', 'is_active', 'is_margin', 
        'favorite')

    fieldsets = (None, {'fields': ('email', 'password')}),
        # ('Permissions', {'fields': ('is_staff', 'is_active')}),
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name',
                'email', 'password1', 'password2',
                'is_margin', 'is_active', 'portfolio'
                )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)