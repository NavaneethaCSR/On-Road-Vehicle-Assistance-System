from django.contrib import admin
from.models import Call,Users,Mechanics,Workshops,Reviews,Request


class MechanicsAdmin(admin.ModelAdmin):
     list_display = ('username','pass1')

admin.site.register(Mechanics,MechanicsAdmin)




class WorkshopsAdmin(admin.ModelAdmin):
     list_display = ('shop_name','mechanic_name','address','number','service','vehicle_types')

admin.site.register(Workshops,WorkshopsAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list = ('Enter_Name','Write_review')

admin.site.register(Reviews, ReviewsAdmin)


admin.site.register(Request)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'pass1')


admin.site.register(Users, UsersAdmin)

class CallAdmin(admin.ModelAdmin):
    list = ('Mobile_no','SMS')

admin.site.register(Call, CallAdmin)