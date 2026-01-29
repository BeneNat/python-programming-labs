from PIL import Image
import os

folder = "C:\\Users\\student\\PycharmProjects\\Python_lab"

for file in os.listdir(folder):
    if file.endswith('.jpg'):
        jpg_path = os.path.join(folder, file)
        png_path = os.path.join(folder, os.path.splitext(file)[0] + ".png")
        with Image.open(jpg_path) as img:
            img.save(png_path, "PNG")
        print(f"File: {file} -> {png_path}")
