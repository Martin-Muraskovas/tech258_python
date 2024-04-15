# Create a file

import os

# Directory
directory = "test_dir"

# Parent directory

parent_directory = "C:/Users/Marti/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Filename
filename = "testfile.txt"

# Filepath
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of the file go here"
    file1.write(toFile)
