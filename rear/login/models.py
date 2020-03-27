from django.db import models

# Create your models here.

class User(models.Model):
    '''用户表'''

    type = (
        ('student', '学生'),
        ('teacher', '教师'),
        ('visitor', '外来者'),
    )

    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    identity = models.CharField(max_length=32, choices=type, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
