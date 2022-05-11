from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    """
    ViewSet基础类，所有视图类都要继承该类
    """

    # 是否在分页器中根据设置的serializer_class自动序列化，默认False
    auto_serializer = False

    def list(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
