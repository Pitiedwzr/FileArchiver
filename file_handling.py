import os
import yaml
import shutil
from collections import defaultdict


# Use classes and objects to add other attributes to the file
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
            # Add the current file as a pending file to the list
            files.append(PendingFile(full_path))
    return files


def categorizeByExt(files, extension_mapping):
    categorized_files = defaultdict(list)
    ext_to_category = {}

    for category, extensions in extension_mapping.items():
        for ext in extensions:
            # The key is extension, value is the category its belongs to
            ext_to_category[ext] = category

    for file in files:
        # Find the category that apply to the file's extention
        # if not found then categorize it as others
        category = ext_to_category.get(file.ext, "Others")
        # The key is category and the value is the file
        categorized_files[category].append(file)

    return categorized_files


def readRulesFiles(directory):
    yaml_files = [f for f in os.listdir(directory) if f.endswith('.yaml')]
    file_names = [os.path.splitext(f)[0] for f in yaml_files]
    return file_names


# Load extension mapping from yaml file
def loadMapping(yaml_file):
    yaml_path = "rules/" + yaml_file + ".yaml"
    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)
    return config.get('extension_mapping', {})


def copyFilesToCategories(categorized_files, processed_path):
    for category, files in categorized_files.items():
        category_path = os.path.join(processed_path, category)
        os.makedirs(category_path, exist_ok=True)

        for file in files:
            destination = os.path.join(category_path, file.name)
            # Leave copy until snapshot is complete
            shutil.copy2(file.path, destination)
