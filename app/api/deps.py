import redis

from app.core.config import get_settings


def get_redis_connection():
    redis_con = redis.Redis(host=get_settings().redis_host,
                            password=get_settings().redis_password)
    try:
        yield redis_con
    finally:
        redis_con.close()
