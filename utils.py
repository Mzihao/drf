import functools
from importlib import import_module
from rest_framework.response import Response


def response_json(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        json = {
            "code": 200,
            "msg": 'success',
            "data": f(*args, **kwargs),
        }
        return Response(json)

    return decorator


def convert_upper_case_to_snake_case(string):
    new_string = ""
    index = 0

    for char in string:
        if index == 0:
            new_string += char.lower()
        elif char.isupper():
            new_string += f"_{char.lower()}"
        else:
            new_string += char

        index += 1

    return new_string


def lazy_import(service_name):
    """
    物流服务懒加载
    :param service_name: 服务名称
    :return: 服务类对象
    """
    try:
        namespace_ = convert_upper_case_to_snake_case(service_name)
        namespace_module = import_module(f"app.services.{namespace_}")
        class_object = getattr(namespace_module, service_name)
    except ImportError:
        raise ValueError(
            'service_name "{}" 不存在'.format(service_name)
        )
    return class_object
