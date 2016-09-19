
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User


class MyAdminSite(AdminSite):
    site_header = 'Kimoni administration'
    index_template = 'admin/index.html'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Group)
admin_site.register(User)


