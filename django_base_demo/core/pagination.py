import logging

from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict

logger = logging.getLogger('django')


class BasePageNumberPagination(PageNumberPagination):
    """
    全局分页器
    """

    # 默认每页显示10条数据
    page_size = 10

    # 当前页码对应的参数名
    page_query_param = 'page'

    # 每页显示数据条数对应的参数名
    page_size_query_param = 'page_size'

    # 每页显示最大数据条数，即page_size的值最大是100
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        """
        封装分页对象

        :param queryset:
        :param request:
        :param view:
        :return:
        """

        # 获取每页显示数据条数
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        # 构造分页器
        paginator = self.django_paginator_class(queryset, page_size)

        # 获取当前页码
        page_number = request.query_params.get(self.page_query_param, 1)
        # 判断当前页码是否合法
        if not isinstance(page_number, int) and not page_number.isdigit():
            # 如果当前页码不是数字，则当前页码等于1
            page_number = 1
        elif int(page_number) <= 0:
            # 如果当前页码小于等于0，则当前页码等于1
            page_number = 1
        elif int(page_number) > paginator.num_pages:
            # 如果当前页码大于最后一页的页码，则当前页码等于最后一页的页码
            page_number = paginator.num_pages

        # 获取当前页面的数据
        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        # 获取当前页数据
        page_data = list(self.page)

        # 序列化，如果视图集配置了serializer_class，且配置了auto_serializer=True时，此处将直接对当前分页数据进行序列化
        if page_data and view.serializer_class and hasattr(view, 'auto_serializer') and view.auto_serializer:
            page_data = view.serializer_class(page_data, many=True).data

        # 封装分页结果对象
        return OrderedDict([
            ('total', self.page.paginator.count),
            ('page', self.page.number),
            ('page_size', page_size),
            ('num_pages', self.page.paginator.num_pages),
            ('records', page_data),
        ])
