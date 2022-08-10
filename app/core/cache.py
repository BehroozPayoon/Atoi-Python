from functools import wraps

from app import crud
from app.core.response import send_success_response


def check_cache(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        cached_result = crud.atoi.get_item(kwargs['redis_conn'], kwargs['data'].input_str)
        if cached_result:
            return send_success_response({'result': cached_result})
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
