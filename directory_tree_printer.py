import os

def print_directory_tree(root_path, indent=''):
    if not os.path.isdir(root_path):
        return

    files = [file_name for file_name in os.listdir(root_path) if
             not file_name.startswith('.') and file_name != '__pycache__']

    for file_name in files:
        file_path = os.path.join(root_path, file_name)
        if os.path.isdir(file_path):
            print(f"{indent}├── {file_name}/")
            print_directory_tree(file_path, indent + "│   ")
        else:
            print(f"{indent}├── {file_name}")


# 현재 폴더의 구조를 트리 형태로 출력
current_directory = os.getcwd()
print_directory_tree(current_directory)
