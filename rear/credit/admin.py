from django.contrib import admin
from credit.models import *
# Register your models here.

class CreditAdmin(admin.ModelAdmin):
    #后台展示的字段 分别是用户id，
    list_display =['user_number_id', 'score']
    #每条显示页数
    list_per_page = 10

admin.site.register(Credit,CreditAdmin)

