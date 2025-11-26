# modules/knowledge.py
import os, json

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
MEMORY_PATH = os.path.join(DATA_DIR, "memory.json")
TASK_PATH = os.path.join(DATA_DIR, "tasks.txt")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def _load_memory():
    ensure_data_dir()
    if not os.path.exists(MEMORY_PATH):
        return {}
    try:
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def _save_memory(mem):
    ensure_data_dir()
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2)

def learn_fact(key, value):
    mem = _load_memory()
    mem[key] = value
    _save_memory(mem)
    return f"Okay, I will remember that {key} is {value}."

def recall_fact(key):
    mem = _load_memory()
    return mem.get(key, None)

def add_task(task_str):
    ensure_data_dir()
    with open(TASK_PATH, "a", encoding="utf-8") as f:
        f.write(task_str.strip() + "\n")
    return f"Added task: {task_str}"

def list_tasks():
    ensure_data_dir()
    if not os.path.exists(TASK_PATH):
        return []
    with open(TASK_PATH, "r", encoding="utf-8") as f:
        tasks = [t.strip() for t in f.readlines() if t.strip()]
    return tasks

def clear_tasks():
    ensure_data_dir()
    open(TASK_PATH, "w", encoding="utf-8").close()
    return "All tasks cleared."
