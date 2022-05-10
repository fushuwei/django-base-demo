import logging

from rest_framework.decorators import action

from django_base_demo.apps.user.models import User
from django_base_demo.apps.user.serializers import UserSerializer
from django_base_demo.core.response import Response
from django_base_demo.core.viewsets import BaseViewSet

logger = logging.getLogger('django')


class UserViewSet(BaseViewSet):
    """
    用户视图集
    """

    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        """
        查询用户列表

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # 获取搜索条件
        search = request.query_params.get('search')

        # 构建查询ORM
        query = User.objects.filter(is_deleted=False).order_by('create_time')

        # 过滤搜索条件
        if search:
            query = query.filter(name__icontains=search)

        # 封装分页，从查询结果集中取出当前页数据
        data = self.paginate_queryset(query)

        # 序列化，对当前页的数据进行序列化
        serializer = UserSerializer(data.get('records'), many=True)

        # 将序列化结果封装至返回值中
        data['records'] = serializer.data

        return Response.success(data, message='请求成功')

    @action(detail=False, methods=['get'])
    def list2(self, request):
        """
        查询用户列表，与 list() 的区别在于该方法是在分页器中自动序列化数据，而非手动编码进行序列化

        重点代码如下：

            # 设置在分页器中进行序列化
            self.auto_serializer = True
            # 封装分页，从查询结果集中取出当前页数据
            data = self.paginate_queryset(query)

        :param request:
        :return:
        """

        # 获取搜索条件
        search = request.query_params.get('search')

        # 构建查询ORM
        query = User.objects.filter(is_deleted=False).order_by('create_time')

        # 过滤搜索条件
        if search:
            query = query.filter(name__icontains=search)

        # 设置在分页器中进行序列化
        self.auto_serializer = True
        # 封装分页，从查询结果集中取出当前页数据
        data = self.paginate_queryset(query)

        return Response.success(data, message='请求成功')

    def create(self, request, *args, **kwargs):
        """
        创建用户

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

    def retrieve(self, request, *args, **kwargs):
        """
        查询单个用户信息

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

    def update(self, request, *args, **kwargs):
        """
        修改用户

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

    def destroy(self, request, *args, **kwargs):
        """
        删除指定用户

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
