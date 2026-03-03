import subprocess
import sys
from pathlib import Path
from importlib.util import find_spec


def check_dependency() -> None:
    if find_spec("redis") is None:
        print("缺少依赖: redis")
        print("请先执行: python -m pip install -r requirements.txt")
        sys.exit(1)


def run_script(script_path: Path) -> int:
    print(f"\n===== Running {script_path.name} =====")
    result = subprocess.run([sys.executable, str(script_path)], check=False)
    return result.returncode


def main() -> None:
    check_dependency()
    base = Path(__file__).parent / "examples"
    scripts = [
        base / "01_connect.py",
        base / "02_basic_ops.py",
        base / "03_counter.py",
        base / "04_login_lock.py",
        base / "05_rate_limit.py",
    ]

    failed = []
    for script in scripts:
        code = run_script(script)
        if code != 0:
            failed.append((script.name, code))

    if failed:
        print("\n以下脚本执行失败：")
        for name, code in failed:
            print(f"- {name} (exit code={code})")
        sys.exit(1)

    print("\n全部脚本执行完成")


if __name__ == "__main__":
    main()
