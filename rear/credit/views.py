from django.shortcuts import render
from . import models

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from login.models import User
from . import models
import random
import hashlib


# Create your views here.
def credit(request):
    credits = models.Credit.objects.all()  # 获取我们的数据库信息到credit里
    return render(request,'credit/display2.html',locals())


def insert(request):
    user11 = User.objects.filter()
    try:
        for user in user11:
            new_credit = models.Credit.objects.create(user_number_id=user,score=random.randint(15, 30))
        return render(request, 'login/index.html')
    except:
        return render(request,'login/register.html')

def getcredit(request):
    user = request.GET.get('No')
    msg = User.objects.values().filter(number=user)
    msg = list(msg)
    id = msg[0]['id']
    score = models.Credit.objects.values().filter(user_number_id=id)
    score = list(score)
    objreturn ={}
    objreturn['status'] = 0
    objreturn['credit'] = score[0]['score']
    return JsonResponse(objreturn)


def getall(request):
    msg = models.Credit.objects.values().filter().order_by('-score')
    msg = list(msg)
    for num in range(0, len(msg)-1):
        id = msg[num]['user_number_id_id']
        usermsg = list(User.objects.values().filter(id=id))
        msg[num]['name']=usermsg[0]['name']
        msg[num]['number']=usermsg[0]['number']
        msg[num]['identity']=usermsg[0]['identity']
    objreturn ={}
    objreturn['status'] = 0
    objreturn['msg'] = msg
    return JsonResponse(objreturn)