import os
import shutil
import string

# 1. Write a Python program to list only directories, files and all directories, files in a specified path.
print("1. List only directories, files, and all directories/files in a specified path")
path = input("Enter a path: ")
if os.path.exists(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    print("Directories:", dirs)
    print("Files:", files)
    print("All:", all_items)
else:
    print("Path not found")

# 2. Write a Python program to check for access to a specified path.
# Test the existence, readability, writability and executability of the specified path.
print("\n2. Check for access to a specified path")
if os.path.exists(path):
    print("Exists:", os.access(path, os.F_OK))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
else:
    print("Path not found")

# 3. Write a Python program to test whether a given path exists or not.
# If the path exists, find the filename and directory portion of the given path.
print("\n3. Test whether a given path exists or not, and find filename and directory")
if os.path.exists(path):
    print("Exists")
    print("Directory part:", os.path.dirname(path))
    print("File part:", os.path.basename(path))
else:
    print("Does not exist")

# 4. Write a Python program to count the number of lines in a text file.
print("\n4. Count the number of lines in a text file")
file_path = input("Enter text file path: ")
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        print("Number of lines:", len(f.readlines()))
else:
    print("File not found")

# 5. Write a Python program to write a list to a file.
print("\n5. Write a list to a file")
lst = ["apple", "banana", "cherry"]
with open("list.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")

# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
print("\n6. Generate 26 text files named A.txt, B.txt, ..., Z.txt")
for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()

# 7. Write a Python program to copy the contents of a file to another file.
print("\n7. Copy the contents of a file to another file")
src = input("Enter source file: ")
dst = input("Enter destination file: ")
if os.path.exists(src):
    shutil.copyfile(src, dst)
    print("Copied")
else:
    print("Source not found")

# 8. Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.
print("\n8. Delete file by specified path (check access and existence)")
delete_path = input("Enter path to delete file: ")
if os.path.exists(delete_path):
    if os.access(delete_path, os.W_OK):
        os.remove(delete_path)
        print("Deleted")
    else:
        print("No permission")
else:
    print("File not found")
