from redis.exceptions import RedisError

from common import get_client


def main() -> None:
    client = get_client()
    try:
        pong = client.ping()
        print(f"PING -> {pong}")
        print("Redis 连接成功")
    except RedisError as err:
        print("Redis 连接失败，请先启动 Redis")
        print(f"错误信息: {err}")


if __name__ == "__main__":
    main()
