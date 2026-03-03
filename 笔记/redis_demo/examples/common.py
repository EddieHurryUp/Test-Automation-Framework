from configparser import ConfigParser
from pathlib import Path

from redis import Redis


def get_client() -> Redis:
    config_path = Path(__file__).resolve().parent.parent / "redis.ini"
    parser = ConfigParser()
    parser.read(config_path, encoding="utf-8")

    if not parser.has_section("redis"):
        raise ValueError(f"Missing [redis] section in {config_path}")

    password = parser.get("redis", "password", fallback="").strip() or None
    return Redis(
        host=parser.get("redis", "host", fallback="127.0.0.1"),
        port=parser.getint("redis", "port", fallback=6379),
        db=parser.getint("redis", "db", fallback=0),
        password=password,
        decode_responses=parser.getboolean("redis", "decode_responses", fallback=True),
        socket_timeout=parser.getfloat("redis", "socket_timeout", fallback=3),
    )

