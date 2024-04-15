# Check if JSON is valid JSON

import json
import os
import sys

if len(sys.argv) > 1:  # more than 1 argument?
    if os.path.exists((sys.argv[1])):  # is the file name passed as an argument
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is Valid!")
    else:
        print(sys.argv[1] + "not found")
else:
    print("Usage: python check_json.py <file>")


