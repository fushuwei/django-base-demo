from django.db import models

from django_base_demo.core.models import BaseModel


class User(BaseModel):
    """
    用户表
    """

    GENDER = (
        ('MALE', '男'),
        ('FEMALE', '女')
    )

    name = models.CharField(max_length=255, null=True, verbose_name='姓名')
    gender = models.CharField(max_length=255, choices=GENDER, null=True, verbose_name='性别')
    age = models.IntegerField(null=True, verbose_name='年龄')
    remark = models.TextField(null=True, verbose_name='备注，描述信息')

    class Meta:
        db_table = 't_user'
