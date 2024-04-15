# Create a directory

import os

# Directory
directory = "test_dir"

# Parent directory

parent_directory = "C:/Users/Marti/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Create Directory
os.mkdir(path)
