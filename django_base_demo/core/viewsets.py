from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):
    """
    ViewSet基础类，所有视图类都要继承该类
    """

    # 自定义属性，用于判断是否在分页器中根据设置的serializer_class自动序列化，默认False
    auto_serializer = False
