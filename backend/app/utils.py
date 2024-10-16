import os
from natsort import natsorted

def process_file(file_path):

    if os.path.exists(file_path):
        print(f"Processing the file path: {file_path}")
    else:
        print(f"File path does not exists.")

def print_file_names(file_path):

    directory_path = file_path
    
    sorted_items = natsorted(os.listdir(directory_path))

    for item in sorted_items:

        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            print(item)
        else:
            print("Error check that file path you have entered")