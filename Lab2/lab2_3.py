from PIL import Image
import os

def change_extension(file_path, new_extension):
    path_root, _ = os.path.splitext(file_path)
    new_file_path = path_root + new_extension

    try:
        #os.rename(file_path, new_file_path)
        with Image.open(file_path) as img:
            img.save(new_file_path)
    except FileNotFoundError:
        print(f"Error: cannot find '{file_path}' file.")
    except FileExistsError:
        print(f"Error: the '{new_file_path}' target file already exists.")
    else:
        print(f"Changed extension of '{file_path}' to '{new_file_path}'.")

if __name__ == '__main__':
    for file in os.listdir('.'):
        if file.endswith('.jpg'):
            change_extension(file, ".png")
