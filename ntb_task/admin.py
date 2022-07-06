from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Resource


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'email',
        'role',
    )
    readonly_fields = ('last_login',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ip',
        'port',
        'type_resource',
        'owner',
    )
    readonly_fields = ('date_edit',)


admin.site.register(User, UserAdmin)
