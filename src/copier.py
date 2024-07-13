import os, shutil

def directory_copier(source_directory, dest_directory, first_time_checker=True):
    if os.path.exists(source_directory) == False:  
        return
    if os.path.isdir(dest_directory) and first_time_checker:
        shutil.rmtree(dest_directory)
        os.mkdir(dest_directory)
        
    list_dir = os.listdir(source_directory)
    for item in list_dir:
        if os.path.isfile(f"{source_directory}/{item}"):
            shutil.copy(f"{source_directory}/{item}", f"{dest_directory}")
        else: 
            new_source_directory = f"{source_directory}/{item}"
            new_dest_directory = f"{dest_directory}/{item}"
            os.mkdir(new_dest_directory)
            first_time_checker = False
            directory_copier(new_source_directory, new_dest_directory, first_time_checker)
    return

