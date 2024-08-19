from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'age', 'is_staff')
    fieldsets = UserAdmin.fieldsets +((None, {'fields': ('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets +((None, {'fields': ('age',)}),)

    """
     The None value indicates that this new section does not have a title,
     and {"fields": ("age",)} specifies that the age field should be included in this section.
    """


admin.site.register(CustomUser, CustomUserAdmin)

