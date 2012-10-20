# _*_ coding:utf-8 _*_

from django.db import models
from django.contrib.auth.models import User

class Msg(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User)
    ip = models.IPAddressField()
    datetime = models.DateTimeField(auto_now_add=True)
    clickcount = models.IntegerField(default=0)
#    comment = models.TextField()

    def __str__(self):
        return '用户%s发表标题为%s 的留言' % (self.title)

    def __unicode__(self):
        return '用户%s发表标题为%s 的留言' % (self.title)

    class Admin:
        list_display = ('title','user','ip','dateti me')
        list_filter = ('user',)
        ording = ('-id',)
        search_field = ('title',)

    class Meta:
        verbose_name_plural = '留言信息'


