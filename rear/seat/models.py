from django.db import models
from login.models import User
#导入login中的User类

# Create your models here.

#楼层信息表
class FloorBuilding(models.Model):
    floor = models.IntegerField(primary_key=True) #楼层
    number_max = models.IntegerField(db_column='max') #桌子数量（最大容量）
    number_now = models.IntegerField(db_column='now') #目前已占用数量

    class Meta:
        db_table = 'floor'
        verbose_name_plural = '楼层'

#座位表
class Desk(models.Model):
    rent_state_choice = (
        (0,'未被占用'),
        (1,'被占用')
    )
    plug_state_choice = (
        (0,'有插座'),
        (1,'无插座')
    )
    desk_id = models.IntegerField(primary_key=True,db_column='desk')
    floor = models.IntegerField(db_column='floor')
    plug_state = models.IntegerField(db_column='plug', choices=plug_state_choice)
    rent_state = models.IntegerField(db_column='status', choices=rent_state_choice)
    #student_number = models.IntegerField(null=True)
    #uer_number = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'desk'
        verbose_name_plural = '座位'

#占座情况表
class Rent(models.Model):
    status_choice = (
        (0,'尚未使用'),
        (1,'正被使用'),
        (2,'使用结束'),
    )       #是否应该增加选项？ 尚未使用、正在使用中

    id = models.AutoField(primary_key=True)
    user_number = models.ForeignKey(User, on_delete=models.CASCADE)
    desk_number = models.ForeignKey(Desk, on_delete=models.CASCADE)  #外键

    date = models.DateField()
    time_choices = (
        (1,'8:00'),
        (2, '9:00'),
        (3, '10:00'),
        (4, '11:00'),
        (5, '12:00'),
        (6, '13:00'),
        (7, '14:00'),
        (8, '15:00'),
        (9, '16:00'),
        (10, '17:00'),
        (11, '18:00'),
        (12, '19:00'),
        (13, '20:00'),
    )
    start_time = models.IntegerField(db_column='start_time',choices=time_choices)
    end_time = models.IntegerField(db_column='end_time',choices=time_choices)
    operate_time = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(db_column='status',choices=status_choice)

    class Meta:
        unique_together = (
            ('user_number','desk_number','date','start_time','end_time'),
        )    # 五个属性联合构成主码，防止有人重复预定
        db_table ='rent'
        verbose_name_plural = '预约座位信息'