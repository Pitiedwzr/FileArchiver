import os

def goThroughFiles(dir_path):
    file_paths = []
    file_names = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
            file_names.append(file)
    return file_paths, file_names