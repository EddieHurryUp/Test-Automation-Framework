from redis.exceptions import RedisError

from common import get_client


def main() -> None:
    client = get_client()
    try:
        client.ping()
    except RedisError as err:
        print(f"Redis 未连接: {err}")
        return

    print("== String 示例 ==")
    client.set("demo:name", "xiaobai")
    print("demo:name =", client.get("demo:name"))

    print("\n== Hash 示例 ==")
    client.hset("demo:user:1", mapping={"name": "Tom", "age": "18"})
    print("demo:user:1 =", client.hgetall("demo:user:1"))

    print("\n== List 示例 ==")
    client.delete("demo:queue")
    client.rpush("demo:queue", "task-1", "task-2", "task-3")
    print("demo:queue =", client.lrange("demo:queue", 0, -1))

    print("\n== TTL 示例 ==")
    client.setex("demo:temp", 10, "10秒后过期")
    ttl = client.ttl("demo:temp")
    print("demo:temp ttl =", ttl, "秒")

    print("\n完成：你已经跑通常见 Redis 操作")


if __name__ == "__main__":
    main()
