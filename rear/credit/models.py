from django.db import models
from login.models import User
# Create your models here.

class Credit(models.Model):
    id = models.AutoField(primary_key=True)
    user_number_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(db_column='score',default =20 ) #初始化默认为20

    class Meta:
        verbose_name = '积分'
        db_table = 'credit'