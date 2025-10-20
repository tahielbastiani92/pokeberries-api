import redis
import json
from src.config import REDIS_HOST, REDIS_PORT, REDIS_TIME_EXPIRED, REDIS_USERNAME, REDIS_PASSWORD


r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, username=REDIS_USERNAME, password=REDIS_PASSWORD)


def get_cache(key: str):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None


def set_cache(key: str, value, expire_seconds=REDIS_TIME_EXPIRED):
    """ Cache data expire each 6 hours """
    r.set(key, json.dumps(value), ex=expire_seconds)
