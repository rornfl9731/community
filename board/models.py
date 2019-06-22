from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=64,verbose_name='title',default='')
    contents = models.TextField(verbose_name='content',default='')
    # contents = RichTextField(max_length=128, verbose_name='content', default='')
    writer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="user",default='')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='시간')





    class Meta:
        db_table = "board"
        verbose_name = "게시글"
        verbose_name_plural="게시글"

        def __str__(self):
            return self.title


class Comment(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='comment')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='comment_user')
    text = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "댓글"
        verbose_name_plural="댓글들"



    def __str__(self):
        return self.text

