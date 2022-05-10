from rest_framework.response import Response as drf_response


class Response:
    """
    http请求响应类
    """

    # 请求状态码
    CODE_SUCCESS = 10000  # 成功
    CODE_MESSAGE = 20000  # 信息
    CODE_CONFIRM = 30000  # 确认
    CODE_LOADING = 40000  # 进度
    CODE_WARNING = 60000  # 警告
    CODE_PERMISSION_DENIED = 70000  # 无权限
    CODE_FAILURE = 99999  # 失败

    @staticmethod
    def success(data=None, message='', description='服务器处理请求成功'):
        """
        成功

        :return:
        """

        data = {'code': Response.CODE_SUCCESS, 'message': message, 'description': description, 'result': data}

        return drf_response(data)

    @staticmethod
    def message(data=None, message='', description='服务器处理请求成功'):
        """
        信息

        :return:
        """

        data = {'code': Response.CODE_MESSAGE, 'message': message, 'description': description, 'result': data}

        return drf_response(data)

    @staticmethod
    def confirm(data=None, message='', description='服务器处理请求成功'):
        """
        确认

        :return:
        """

        data = {'code': Response.CODE_CONFIRM, 'message': message, 'description': description, 'result': data}

        return drf_response(data)

    @staticmethod
    def loading(data=None, message='', description='服务器处理请求成功'):
        """
        进度

        :return:
        """

        data = {'code': Response.CODE_LOADING, 'message': message, 'description': description, 'result': data}

        return drf_response(data)

    @staticmethod
    def warning(data=None, message='', description='服务器处理请求失败'):
        """
        警告

        :return:
        """

        data = {'code': Response.CODE_WARNING, 'message': message, 'description': description, 'result': data}

        return drf_response(data)

    @staticmethod
    def permission_denied(data=None, message='权限不足，无法访问', description='服务器处理请求失败'):
        """
        无权限

        :return:
        """

        data = {'code': Response.CODE_PERMISSION_DENIED, 'message': message, 'description': description, 'result': data}

        return drf_response(data)

    @staticmethod
    def failure(data=None, message='', description='服务器处理请求失败'):
        """
        失败

        :return:
        """

        data = {'code': Response.CODE_FAILURE, 'message': message, 'description': description, 'result': data}

        return drf_response(data)
