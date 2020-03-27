from django import forms

from captcha.fields import CaptchaField

class UserForm(forms.Form):
    number = forms.CharField(label=" I  D  ", max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    type = (
        ('student', '学生'),
        ('teacher', '教师'),
        ('visitor', '外来者'),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(label="学号/工号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    identity = forms.ChoiceField(label='身份', choices=type)
    captcha = CaptchaField(label='验证码')