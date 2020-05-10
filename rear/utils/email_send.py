from random import Random,choices
from django.core.mail import send_mail

from login.models import EmailVerifyRecord
from mysite.settings import EMAIL_FROM


# 随机字符串
def random_str(randomlength=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) -1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_type_email(email,send_type = 'register'):
    email_record  = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()      #保存code 和  email 用于 激活 认证

    email_title =""
    email_body = ""

    if send_type == 'register':
        email_title = "图书馆注册激活"
        email_body = "激活验证码:{}" .format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email],fail_silently=False)
        if send_status:
            pass