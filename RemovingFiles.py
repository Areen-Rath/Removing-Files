import os, shutil, time

days = time.time()

path = input("Enter the path for clean up: ")

if(os.path.exists(path)):
    for file in os.listdir(path):
        file_or_dir_path = os.path.join(path, file)
        root_ext = file_or_dir_path.split('.')
        ctime = os.stat(file_or_dir_path).st_ctime
        
        if ctime > days:
            if root_ext[1]:
                os.remove(file_or_dir_path)
            else:
                shutil.rmtree(file_or_dir_path)