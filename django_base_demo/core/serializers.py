from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    """
    Serializer基础类，统一格式化同名同类型的字段，所有Serializer继承该类
    """

    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False, read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False, read_only=True)
