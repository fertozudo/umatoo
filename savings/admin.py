from core.admin import admin_site
from savings.models import Target,  BankTransaction, KimoniTransaction
from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from savings.models import ProfileUser


# USER MODEL ADMIN
# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileUserInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileUserInline, )
    actions = ['action_simulation']

    def action_simulation(self, request, queryset):
        from savings.utils import simulation
        for user in queryset:
            simulation(user, salary=1000)

    action_simulation.short_description = "Simulation"


# Re-register UserAdmin
admin_site.register(ProfileUser)
admin_site.unregister(User)
admin_site.register(User, UserAdmin)


# BASE MODEL ADMIN
class SavingsBaseModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(admin.ModelAdmin, self).get_queryset(request)
        else:
            return super(admin.ModelAdmin, self).get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the owner field.
        """
        if not change:
            obj.owner = request.user
        obj.save()


# SAVINGS MODEL ADMINS
class TargetAdmin(SavingsBaseModelAdmin):
    list_display = ('name', 'target_amount', 'achieved_amount')

admin_site.register(Target, TargetAdmin)


class BankTransactionAdmin(SavingsBaseModelAdmin):
    list_display = ('date', 'category', 'description', 'amount', 'balance')

admin_site.register(BankTransaction, BankTransactionAdmin)


class KimoniTransactionAdmin(SavingsBaseModelAdmin):
    list_display = ('date', 'category', 'target', 'amount', 'balance')

admin_site.register(KimoniTransaction, KimoniTransactionAdmin)

