import time
import functools


def clock(func):
    """
    计时装置器，用于分析方法的执行耗时，从而优化代码

    :param func:
    :return:
    """

    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            arg_list.append(', '.join(['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


if __name__ == '__main__':
    """
    测试装置器，注意@clock后面没有括号
    """


    @clock
    def test(a, b):
        time.sleep(1)


    test(100, 'abc')
