from rest_framework import serializers

from django_base_demo.apps.user.models import User
from django_base_demo.core.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    """
    用户序列化类
    """

    gender_name = serializers.ChoiceField(choices=User.GENDER, source='get_gender_display')

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if not instance.remark:
            data['remark'] = '请补充备注信息'

        return data

    class Meta:
        model = User
        fields = '__all__'
