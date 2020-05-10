from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import models
from credit.models import Credit
from .forms import UserForm
from .forms import RegisterForm
from .forms import ConfirmForm
import hashlib
from .models import User,EmailVerifyRecord
from utils.email_send import send_type_email


def index(request):
    pass
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            number = request.POST.get('number')
            password = request.POST.get('password')
            try:
                user = models.User.objects.get(number=number)
                if user.password == hash_code(password):
                    if user.has_confirmed != False:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        return redirect('/index/')
                    else:
                        message="账号未激活！"
                else:
                    message="密码不正确！"
            except:
                message="学号/工号不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    # if request.session.get('is_login', None):
    #     #登录状态不允许注册。你可以修改这条原则！
    #     return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            number = register_form.cleaned_data['number']
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            identity = register_form.cleaned_data['identity']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_number_user = models.User.objects.filter(number=number)
                if same_number_user:  # 学号/工号唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.number=number
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.identity = identity
                new_user.save()
                user11 = models.User.objects.get(number=number)
                print(user11)
                new_credit = Credit.objects.create(user_number_id=user11)
                message = '请前往注册邮箱，进行邮件确认！'
                send_type_email(email, "register")
                return redirect("/confirm/")  # 自动跳转到确认页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def user_confirm(request):
    if request.method == "POST":
        confirm_form = ConfirmForm(request.POST)
        message = "请检查填写的内容！"
        if confirm_form.is_valid():
            email=confirm_form.cleaned_data['email']
            code = confirm_form.cleaned_data['code']
            all_records = EmailVerifyRecord.objects.filter(email=email)
            if all_records:
                for record in all_records:
                    if code == record.code:
                        user = User.objects.get(email=email)
                        user.has_confirmed = True
                        user.save()
                        return redirect('/login/')
                    else:
                        render(request, 'login/confirm.html', locals())
            else:
                render(request, 'login/confirm.html', locals())
    confirm_form = ConfirmForm()

    return render(request, 'login/confirm.html', locals())


def base(request):
    pass
    return render(request, 'login/base.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')

def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

#new

def confirm(request):
    user = {}
    object1 = {}
    if request.method == 'POST':
        user['name'] = request.POST.get('name')
        try:
            check = models.User.objects.get(name=user['name'])
            object1['status'] = 0
            object1['no'] = check.number
            return JsonResponse(object1)
        except:
            object1['status'] = 1
            object1['no'] = -250
            return JsonResponse(object1)
