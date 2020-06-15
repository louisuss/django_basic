from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    # 1:n 관계
    writer = models.ForeignKey(
        "user.User", verbose_name='작성자', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    # m:n 관계
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
