from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount,materials,Answers,Questions,Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserAccount
    list_display = ('email','firstname','lastname','userType','phonenumber','subject')
    list_filter = ('email','firstname','lastname','userType','phonenumber','subject')
    fieldsets = (
        (None, {'fields': ('email', 'password','firstname','lastname','userType','phonenumber','subject')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','firstname','lastname','userType','phonenumber', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserAccount, CustomUserAdmin)
admin.site.register(materials)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Profile)