from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='사용자명')
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    registered_date_time = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
