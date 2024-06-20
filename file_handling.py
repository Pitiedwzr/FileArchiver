import os
import yaml
import shutil
from collections import defaultdict

# Use classes and objects to add other attributes to the file to be processed later.
class PendingFile:
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path)
        self.ext = os.path.splitext(self.name)[1].lower()

def goThroughFiles(dir_path):
    files = []
    for root, dirs, files_list in os.walk(dir_path):
        for file in files_list:
            full_path = os.path.join(root, file)
            files.append(PendingFile(full_path)) # Add the current file as a pending file to the list
    return files

def categorizeByExt(files, extension_mapping):
    categorized_files = defaultdict(list) # Use defaultdict to create a dictionary
    ext_to_category = {}

    for category, extensions in extension_mapping.items():
        for ext in extensions:
            ext_to_category[ext] = category # The key is extension and value is the category its belongs to

    for file in files:
        category = ext_to_category.get(file.ext, "Others") # Find the category that apply to the file's ext, if not found then categorize it as others
        categorized_files[category].append(file) # The key is category and the value is the file

    return categorized_files

# Load extension mapping from yaml file
def loadMapping(yaml_path):
    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)
    return config.get('extension_mapping', {})

def copyFilesToCategories(categorized_files, processed_path):
    for category, files in categorized_files.items():
        category_path = os.path.join(processed_path, category)
        os.makedirs(category_path, exist_ok=True)
        
        for file in files:
            destination = os.path.join(category_path, file.name)
            shutil.copy2(file.path, destination)
            print(f"Copied {file.path} to {destination}") # Debug

# Debug, connect to the ui later
map_path = 'ext_map.yaml'
extension_mapping = loadMapping(map_path)

pending_path = "./for_assessment/develop_log/W5T2/path_getting/pending"
processed_path = "./for_assessment/develop_log/W5T2/path_getting/processed"
pending_files = goThroughFiles(pending_path)
categorized_files = categorizeByExt(pending_files, extension_mapping)

# copyFilesToCategories(categorized_files, processed_path)
