import os
import sys

#path = "C:\\Users\\student\\PycharmProjects\\Python_lab"

def list_files(startpath = os.getcwd()):
    try:
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        list_files(sys.argv[1])
    else:
        list_files()