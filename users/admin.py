from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):

    search_fields = ('email', 'username', 'first_name')
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-date_joined', )
    list_display = ('username', 'email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Profile', {'fields': ('first_name', 'last_name', 'profile_picture', 'biography', 'gender', 'birthday')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'email', 'password1', 'password2',)}
         ),
        ('Profile', {'fields': ('first_name', 'last_name', 'profile_picture', 'biography', 'gender', 'birthday')}
         ),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')})
    )
