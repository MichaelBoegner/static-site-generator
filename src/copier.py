import os, shutil
from helpers import generate_page

def directory_copier(source_directory, dest_directory, first_time_checker=True):
    if os.path.exists(source_directory) == False:  
        return
    if os.path.isdir(dest_directory) and first_time_checker:
        shutil.rmtree(dest_directory)
        os.mkdir(dest_directory)
        
    list_dir = os.listdir(source_directory)
    for file in list_dir:
        if os.path.isfile(f"{source_directory}/{file}"):
            shutil.copy(f"{source_directory}/{file}", f"{dest_directory}")
        else: 
            new_source_directory = f"{source_directory}/{file}"
            new_dest_directory = f"{dest_directory}/{file}"
            os.mkdir(new_dest_directory)
            first_time_checker = False
            directory_copier(new_source_directory, new_dest_directory, first_time_checker)
    return

def generate_pages_recursive(source_directory, template_path, dest_directory):
    print("\n\nDEST DIR EXISTS? == ", os.path.isdir(dest_directory)," and is ", dest_directory, " and source dir is ", source_directory)
    if os.path.isdir(dest_directory) != True:
        print("\nMAKING DIR == ", dest_directory)
        os.mkdir(dest_directory)

    list_dir = os.listdir(source_directory)
    for file in list_dir:
        print("\nFILE BEING CHECKED == ", file)
        if os.path.isfile(f"{source_directory}/{file}"):
            print("\nGENERATE PAGE WITH == ", source_directory,"/",file," and ", template_path, " and ", dest_directory,"/index.html")
            generate_page(f"{source_directory}/{file}", template_path, f"{dest_directory}/index.html")
        else:
            new_source_directory = f"{source_directory}/{file}"
            new_dest_directory = f"{dest_directory}/{file}"
            os.mkdir(new_dest_directory)
            print("\n RECURSING == ", new_dest_directory," and ", new_dest_directory," and ", template_path)
            generate_pages_recursive(new_source_directory, template_path, new_dest_directory)
    return