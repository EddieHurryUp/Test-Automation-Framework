# redis_demo

面向初学者的 Redis Python 示例。目标是 10 分钟内完成：

1. 启动本地 Redis
2. Python 成功连接 Redis
3. 学会常见操作（String / Hash / List / TTL）
4. 运行一个简单计数器场景
5. 理解登录失败锁定和固定窗口限流

## 目录结构

```text
redis_demo/
├── docker-compose.yml
├── redis.ini
├── requirements.txt
├── run_all.py
└── examples/
    ├── common.py
    ├── 01_connect.py
    ├── 02_basic_ops.py
    ├── 03_counter.py
    ├── 04_login_lock.py
    └── 05_rate_limit.py
```

## 0) 安装依赖

```bash
cd /Users/qijiaxi/IdeaProjects/Test-Automation-Framework/笔记/redis_demo
python -m pip install -r requirements.txt
```

## 1) 启动 Redis

如果你本机已有 Redis，可跳过本步骤。  
推荐用 Docker 一键启动：

```bash
docker compose up -d
```

检查是否启动成功：

```bash
docker compose ps
```

默认连接地址：`127.0.0.1:6379`

连接配置统一放在 `redis.ini`，示例：

```ini
[redis]
host = 127.0.0.1
port = 6379
db = 0
password =
decode_responses = true
socket_timeout = 3
```

如果你的 Redis 在别的机器或有密码，改这里即可。

## 2) 运行入门脚本

```bash
python examples/01_connect.py
python examples/02_basic_ops.py
python examples/03_counter.py
python examples/04_login_lock.py
python examples/05_rate_limit.py
```

或者一次跑完：

```bash
python run_all.py
```

## 每个脚本学什么

- `01_connect.py`：连接 Redis、`PING` 健康检查、连接异常处理
- `02_basic_ops.py`：String / Hash / List / TTL 常见操作
- `03_counter.py`：`INCR` 计数器场景（如浏览量）
- `04_login_lock.py`：登录失败累计 + 锁定时间（防爆破）
- `05_rate_limit.py`：固定窗口限流（10 秒最多 5 次）

## 常见报错

1. `ConnectionError: Error 61 connecting to 127.0.0.1:6379`  
Redis 没启动，先执行 `docker compose up -d`。

2. `ModuleNotFoundError: No module named 'redis'`  
没装依赖，执行 `python -m pip install -r requirements.txt`。

3. 用了多个 Python 环境  
建议统一用：`python -m pip ...` 和 `python xxx.py`，避免 `pip`、`python` 指向不同环境。
