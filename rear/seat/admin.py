from django.contrib import admin
from seat.models import *
# Register your models here.

class FloorBuildingAdmin(admin.ModelAdmin):
    #后台展示的字段 分别是楼层号，最大容量
    list_display =['floor','number_max','number_now']
    #每页显示条数
    list_per_page = 5

class DeskAdmin(admin.ModelAdmin):
    #后台展示的字段 分别是桌子号码，是否有插座，是否被预定
    list_display =['desk_id','floor','plug_state','rent_state']
    list_per_page = 20

class RentAdmin(admin.ModelAdmin):
    #后台展示的字段 分别是用户id，桌子id,预定日期，开始时刻，结束时刻，操作时刻，正在使用情况，履行约定情况
    list_display =['user_number', 'desk_number', 'date', 'start_time', 'end_time', 'operate_time', 'status']
    list_per_page = 10


admin.site.register(FloorBuilding, FloorBuildingAdmin)
admin.site.register(Desk, DeskAdmin)
admin.site.register(Rent, RentAdmin)
