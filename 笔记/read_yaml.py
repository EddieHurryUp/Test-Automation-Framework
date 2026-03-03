import yaml
from pathlib import Path

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

data = read_yaml(Path(__file__).with_name('login.yaml'))
print(data)
