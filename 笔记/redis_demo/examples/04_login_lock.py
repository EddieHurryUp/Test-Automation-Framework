from redis import Redis
from redis.exceptions import RedisError

from common import get_client

MAX_FAILS = 5
LOCK_SECONDS = 60
def register_login_failure(client: Redis, username: str) -> tuple[int, int]:
    fail_key = f"demo:login:fail:{username}"
    lock_key = f"demo:login:lock:{username}"

    lock_ttl = client.ttl(lock_key)
    if lock_ttl > 0:
        return MAX_FAILS, lock_ttl

    fails = client.incr(fail_key)
    if fails == 1:
        client.expire(fail_key, LOCK_SECONDS)

    if fails >= MAX_FAILS:
        client.setex(lock_key, LOCK_SECONDS, "1")
        client.delete(fail_key)
        return MAX_FAILS, LOCK_SECONDS

    remaining = max(LOCK_SECONDS, client.ttl(fail_key))
    return fails, remaining


def main() -> None:
    client = get_client()
    username = "tom"
    fail_key = f"demo:login:fail:{username}"
    lock_key = f"demo:login:lock:{username}"

    try:
        client.ping()
    except RedisError as err:
        print(f"Redis 未连接: {err}")
        return

    client.delete(fail_key, lock_key)

    print(f"模拟用户 {username} 连续登录失败，阈值={MAX_FAILS}，锁定={LOCK_SECONDS}秒")
    for i in range(1, 8):
        count, ttl = register_login_failure(client, username)
        if count >= MAX_FAILS:
            print(f"第{i}次失败 -> 账号已锁定，剩余 {ttl} 秒")
        else:
            print(f"第{i}次失败 -> 当前失败次数 {count}，窗口剩余 {ttl} 秒")


if __name__ == "__main__":
    main()
