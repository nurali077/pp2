import os
import shutil

def list_files_and_dirs(path):
    if not os.path.exists(path):
        print(f"Ошибка: путь '{path}' не существует!")
        return
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All:", os.listdir(path))