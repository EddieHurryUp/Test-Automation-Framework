import time

from redis import Redis
from redis.exceptions import RedisError

from common import get_client

WINDOW_SECONDS = 10
MAX_REQUESTS = 5
def allow_request(client: Redis, user_id: str) -> tuple[bool, int, int]:
    key = f"demo:rate:user:{user_id}"
    current = client.incr(key)
    if current == 1:
        client.expire(key, WINDOW_SECONDS)
    ttl = client.ttl(key)
    allowed = current <= MAX_REQUESTS
    return allowed, current, max(ttl, 0)


def main() -> None:
    client = get_client()
    user_id = "u1001"
    key = f"demo:rate:user:{user_id}"

    try:
        client.ping()
    except RedisError as err:
        print(f"Redis 未连接: {err}")
        return

    client.delete(key)
    print(f"固定窗口限流: {WINDOW_SECONDS}秒内最多 {MAX_REQUESTS} 次请求")

    for i in range(1, 9):
        allowed, current, ttl = allow_request(client, user_id)
        state = "允许" if allowed else "拒绝"
        print(f"请求{i}: {state} (窗口计数={current}, 剩余TTL={ttl}s)")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
