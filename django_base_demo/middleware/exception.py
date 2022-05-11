import logging

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.views import exception_handler as drf_exception_handler

from django_base_demo.core.response import Response

logger = logging.getLogger('django')


class ExceptionMiddleware(MiddlewareMixin):
    """
    全局异常处理中间件
    """

    def process_exception(self, request, exception):
        """
        异常处理

        :param request:
        :param exception:
        :return:
        """

        # 记录异常日志
        logger.exception(exception)

        # 封装返回值
        data = {
            'code': Response.CODE_FAILURE,
            'message': '服务器内部错误',
            'description': '服务器处理请求失败',
            'result': None
        }

        # 响应异常信息，这里返回200状态码，而不是500状态码（status.HTTP_500_INTERNAL_SERVER_ERROR）
        return JsonResponse(data=data, status=status.HTTP_200_OK)


def exception_handler(exc, context):
    """
    DRF框架全局异常处理，用于拦截 APIView 及其子类抛出的 APIException 类型的异常

    :param exc: 异常
    :param context: 抛出异常的上下文
    :return:
    """

    # 记录异常日志
    logger.exception(exc)

    # 调用drf框架原生的异常处理方法
    response = drf_exception_handler(exc, context)

    if not response:
        response = Response.failure(message='服务器内部错误', description='服务器处理请求失败')

    return response
