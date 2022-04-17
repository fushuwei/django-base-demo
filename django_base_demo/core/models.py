import uuid

from django.db import models


class UUID(object):
    """
    UUID工具类，用于生成32位长度的UUID字符串
    """

    @staticmethod
    def uuid():
        """
        生成32位长度, 不带"-"的唯一字符串

        :return:
        """

        return uuid.uuid1().hex


class BaseModel(models.Model):
    """
    Model基础类，所有Model都要继承该类
    """

    IS_DELETED = (
        (True, '是'),
        (False, '否')
    )

    id = models.CharField(max_length=50, primary_key=True, default=UUID.uuid, null=False)  # 唯一主键
    create_by = models.CharField(max_length=255, blank=True, null=True)  # 创建人
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间
    update_by = models.CharField(max_length=255, blank=True, null=True)  # 最后修改人
    update_time = models.DateTimeField(auto_now=True, null=True)  # 最后修改时间
    is_deleted = models.BooleanField(default=False, choices=IS_DELETED)  # 是否删除标记

    class Meta:
        abstract = True  # 抽象类，数据库迁移时不会创建实体表