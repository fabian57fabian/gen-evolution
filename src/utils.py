import json
import shutil


def read_file(fn: str) -> str:
    with open(fn, "r") as f:
        content = f.read()
    return content


def write_file(fn: str, content: str) -> None:
    with open(fn, "w") as f:
        f.write(content)


def append_file(fn: str, lines: list):
    with open(fn, "a") as f:
        for line in lines:
            f.write(line)


def load_config(path) -> dict:
    with open(path, "r") as f:
        config = json.load(f)
    assert "llm" in config
    if "temperature" in config:
        assert isinstance(config["temperature"], float)
    return config


def save_config(path: str, params: dict) -> None:
    with open(path, "w") as f:
        f.write(json.dumps(params, indent=2))


def copy_files(src: str, dest: str) -> None:
    shutil.copy2(src, dest)