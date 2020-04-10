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


class Desk(models.Model):
    desk_number = models.CharField(primary_key=True, max_length=5)
    floor = models.CharField(max_length=1)
    plug_state = models.BooleanField()
    student_number = models.IntegerField(null=True)


class Rent(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    desk_number = models.ForeignKey(Desk, on_delete=models.CASCADE)
    operate_time = models.DateTimeField(auto_now_add=True)
