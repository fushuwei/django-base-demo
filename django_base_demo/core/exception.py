import logging

from rest_framework.views import exception_handler as drf_exception_handler

from django_base_demo.core.response import Response

logger = logging.getLogger('django')


def exception_handler(exc, context):
    """
    自定义全局异常处理方法

    :param exc: 异常
    :param context: 抛出异常的上下文
    :return:
    """

    # 调用drf框架原生的异常处理方法
    response = drf_exception_handler(exc, context)

    logger.exception(exc)

    if not response:
        response = Response.failure(message='服务器内部错误', description='服务器处理请求失败')

    return response
