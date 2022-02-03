import hashlib
from pathlib import Path


def generate_directory_hashmap(directory_path):
    dictionary_to_return = {}
    p = Path(directory_path)
    file_list = p.rglob("*")
    for entry in file_list:
        if entry.is_file():
            sha256sum = hashlib.sha256(entry.read_bytes()).hexdigest()
            dictionary_to_return[sha256sum] = entry.absolute()

    return dictionary_to_return


def is_copy_successful(source_path, destination_path):
    """
    Given two paths, compare the source path with the destination path.
    If there are any files in the destination path that cannot be found in the source path, print out the path for those files
    """
    camera_folder_dict = generate_directory_hashmap(source_path)
    pc_folder_dict = generate_directory_hashmap(destination_path)
    for file_hash in pc_folder_dict.keys():
        if file_hash not in camera_folder_dict.keys():
            print(pc_folder_dict[file_hash])


source_folder = "Path/To/Source/Folder/Goes/Here"
destination_folder = "Path/To/Destination/Folder/Goes/Here"

is_copy_successful(source_folder, destination_folder)