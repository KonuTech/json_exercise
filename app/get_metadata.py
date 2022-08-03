import os
import pprint

def main():
    """
    :return:
    """

    files_metadata = {}

    for root, directories, files in os.walk("."):
        for file in files:
            full_path = os.path.abspath(os.path.join(root, file))
            size = os.path.getsize(full_path)
            files_metadata[full_path] = size


    item = 0
    for path, size in sorted(files_metadata.items(), key=lambda x:x[1], reverse=True):
        if item > 10:
            break
        print(f"Size: {size}b of Path: {path}")
        item += 1


if __name__ == "__main__":
    main()
