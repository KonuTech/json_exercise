import os
import pprint

file_metadata = {}

for root, directories, files in os.walk("."):
    for file in files:
        full_path = os.path.abspath(os.path.join(root, file))
        size = os.path.getsize(full_path)
        file_metadata[full_path] = size


item = 0
for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if item > 10:
        break
    print(f"Size: {size}b of Path: {path}")
    item += 1
