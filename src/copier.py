import os, shutil

def directory_copier(source_directory, dest_directory, first_time_checker=True):
    print("SOURCE AND DEST DIR BEGINNING = ", source_directory, dest_directory)
    if os.path.exists(source_directory) == False:
        print("OS PATH DOESN'T EXIST = ", source_directory)   
        return
    if os.path.isdir(dest_directory) and first_time_checker:
        print("FIRST TIME", first_time_checker)
        shutil.rmtree(dest_directory)
        os.mkdir(dest_directory)
        
    list_dir = os.listdir(source_directory)
    print("LIST DIR = ", list_dir)
    for item in list_dir:
        print("ITEM IN LIST DIR =", item)
        if os.path.isfile(f"{source_directory}/{item}"):
            shutil.copy(f"{source_directory}/{item}", f"{dest_directory}")
            print("WRITING FILE TO DEST", f"{source_directory}/{item}", f"{dest_directory}")
        else: 
            new_source_directory = f"{source_directory}/{item}"
            new_dest_directory = f"{dest_directory}/{item}"
            os.mkdir(new_dest_directory)
            first_time_checker = False
            print("CHANGING SOURCE AND DEST DIR = ", new_source_directory, new_dest_directory)
            directory_copier(new_source_directory, new_dest_directory, first_time_checker)
    print("LOOP OVER")

    return


source_directory = "../static"
dest_directory = "../public"

directory_copier(source_directory, dest_directory)