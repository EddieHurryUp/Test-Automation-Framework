from redis.exceptions import RedisError

from common import get_client


def main() -> None:
    client = get_client()
    key = "demo:page:view_count"
    try:
        client.ping()
    except RedisError as err:
        print(f"Redis 未连接: {err}")
        return

    client.delete(key)
    print("初始值:", client.get(key))

    print("模拟 5 次访问...")
    for _ in range(5):
        current = client.incr(key)
        print("当前计数:", current)

    final_count = client.get(key)
    print("最终计数:", final_count)


if __name__ == "__main__":
    main()
