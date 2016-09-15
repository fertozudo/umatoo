from django.contrib import admin

from django.contrib.auth.models import User

from savings.models import Target, ProfileUser


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileUserInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


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


class TargetAdmin(SavingsBaseModelAdmin):
    list_display = ('name', 'amount', 'days')

admin.site.register(Target, TargetAdmin)