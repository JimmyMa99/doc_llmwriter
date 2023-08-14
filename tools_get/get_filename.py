import os

def list_filenames_in_directory(directory_path):
    filenames = []
    relative_filenames = []
    #相对路径

    relative_path = os.path.relpath(directory_path)
    
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            filenames.append(filename)
            relative_filenames.append(os.path.join(relative_path, filename))

    return filenames,relative_filenames

