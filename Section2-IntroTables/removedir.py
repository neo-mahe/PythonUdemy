import os
import stat
import shutil


def redo_with_write(redo_func, path, err):
    os.chmod(path, stat.S_IWRITE)
    redo_func(path)


dir_path = "D:\\Export_Users\\"

if os.path.exists(dir_path):
    shutil.rmtree(dir_path, onerror=redo_with_write)
    print("Removing the old folders & files structure")

else:
    print("Skipping this step as the old folder & file structure doesn't exists")
