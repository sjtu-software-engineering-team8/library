from django.shortcuts import render
from . import models

# Create your views here.
def credit(request):
    credits = models.Credit.objects.all()  # 获取我们的数据库信息到credit里
    return render(request,'credit/display2.html',locals())
