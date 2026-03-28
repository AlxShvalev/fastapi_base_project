import redis.asyncio
from fastapi_users.authentication import RedisStrategy

from core.config import settings

redis = redis.asyncio.from_url(
    settings.redis.redis_url,
    decode_responses=True,
)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(
        redis,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
