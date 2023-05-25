from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,SocialLogin

# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'user_country', 'no_files')
	search_feilds = ('email', 'username',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets =()

admin.site.register(Account, AccountAdmin)	
admin.site.register(SocialLogin)