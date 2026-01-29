import os

def traverse_directory(path):
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                traverse_directory(full_path)
            else:
                print(full_path)
    except PermissionError:
        pass

start_path = "C:\\Users\\student\\PycharmProjects\\Python_lab"
traverse_directory(start_path)