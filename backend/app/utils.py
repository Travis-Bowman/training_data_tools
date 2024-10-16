import os

def process_file(file_path):

    if os.path.exists(file_path):
        print(f"Processing the file path: {file_path}")
    else:
        print(f"File path does not exists.")
