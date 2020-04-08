from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import models
from .forms import UserForm
from .forms import RegisterForm
import hashlib



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
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
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
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

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