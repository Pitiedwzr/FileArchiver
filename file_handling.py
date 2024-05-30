import os
from collections import defaultdict

# Use classes and objects to add other attributes to the file to be processed later.
class PendingFile:
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path)
        self.ext = os.path.splitext(self.name)[1]

def goThroughFiles(dir_path):
    files = []
    for root, dirs, files_list in os.walk(dir_path):
        for file in files_list:
            full_path = os.path.join(root, file)
            files.append(PendingFile(full_path)) # Add the current file as a pending file to the list
    return files

def categorizeByExt(files):
    categorized_files = defaultdict(list)
    for file in files:
        categorized_files[file.ext].append(file)
    return categorized_files

directory = "./for_assessment" # Will replace by the pending path
files = goThroughFiles(directory)
categorized_files = categorizeByExt(files)

for ext, files in categorized_files.items():
    print(f"Extension: {ext}")
    for file in files:
        print(f"  {file.path}")
