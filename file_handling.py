import os
import yaml
import time
import shutil
from collections import defaultdict


# Use classes and objects to add attributes to the file
class PendingFile:
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path)
        self.ext = os.path.splitext(self.name)[1].lower()


# Go through a directory and create PendingFile objects for each file, return a list of PendingFile objects      
def goThroughFiles(dir_path):
    files = []
    for root, dirs, files_list in os.walk(dir_path):
        for file in files_list:
            full_path = os.path.join(root, file)
            # Add the current file as a pending file to the list
            files.append(PendingFile(full_path))
    return files


# Categorize files based on their extensions using the provided mapping
# Return a dictionary with categories as keys and lists of files as values
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


# Find the map file (yaml) in the path
# Return a list of rule file names without extensions
def readRulesFiles(directory):
    yaml_files = [f for f in os.listdir(directory) if f.endswith('.yaml')]
    file_names = [os.path.splitext(f)[0] for f in yaml_files]
    return file_names


# Load extension mapping from the name of map file (without the extension)
# return a dictionary containing the extension mapping
def loadMapping(yaml_file):
    yaml_path = "rules/" + yaml_file + ".yaml"
    with open(yaml_path, 'r') as yamlfile:
        config = yaml.safe_load(yamlfile)
    return config.get('extension_mapping', {})


# Generate a snapshot (yaml) file of the file processing operation
def generateSnapshot(files, category_path):
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    snapshot_dir = "snapshots"
    snapshot_file = f"{snapshot_dir}/{current_time}.yaml"

    os.makedirs(snapshot_dir, exist_ok=True)
    for file in files:
        final_path = os.path.join(category_path, file.name)
        snapshot = {
            "date": current_time,
            file.name: {
                "pending_path": file.path,
                "processed_path": final_path
                }
            }

        # Load existing data or create an empty dict
        if os.path.exists(snapshot_file):
            with open(snapshot_file, "r") as yamlfile:
                existing_data = yaml.safe_load(yamlfile) or {}
        else:
            existing_data = {}

        # Update existing data with new snapshot
        existing_data.update(snapshot)

        # Write updated data to file
        with open(snapshot_file, "w") as yamlfile:
            yaml.safe_dump(existing_data, yamlfile)


# Load the snapshot, recover files from the processed path to their original locations
def loadSnapshot(snapshot):
    with open(snapshot, "r") as yamlfile:
        snapshot_data = yaml.safe_load(yamlfile)

    for file_name, paths in snapshot_data.items():
        if file_name == "date":
            continue  # Skip the date entry

        pending_path = paths.get("pending_path")
        processed_path = paths.get("processed_path")

        if pending_path and processed_path and os.path.exists(processed_path):
            # Ensure the directory of pending_path exists
            os.makedirs(os.path.dirname(pending_path), exist_ok=True)
  
            # Move the file back to its original location
            shutil.move(processed_path, pending_path)


# Move files to their category folders and optionally save a snapshot
def moveFilesToCategories(categorized_files, processed_path, save_snapshot):
    for category, files in categorized_files.items():
        category_path = os.path.join(processed_path, category)
        os.makedirs(category_path, exist_ok=True)

        for file in files:
            destination = os.path.join(category_path, file.name)
            shutil.move(file.path, destination)
            
        if save_snapshot:
            generateSnapshot(files, category_path)