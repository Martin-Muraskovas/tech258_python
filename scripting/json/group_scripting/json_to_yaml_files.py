# Check if JSON is valid JSON

import json
import os
import sys
import yaml


def check_json():
    if len(sys.argv) > 1:  # more than 1 argument?
        if os.path.exists((sys.argv[1])):  # is the file name passed as an argument
            file = open(sys.argv[1], "r")  # opens the json file referenced by the user in the CLI parameters
            json.load(file)  # throws an error if the format inside the file is not correctly JSON
            file.close()  # closes the file
            print("JSON is Valid!")
            return True  # returns true to confirm that the file is a JSON format file with correctly formatted data
        else:
            print(sys.argv[1] + " not found")  # prints that the file is not found (user error)
    else:
        print("Usage: python check_json.py <file>")  # shows the user how to use the script in CLI


if check_json():  # if the json file is a valid format
    path = sys.argv[1]  # saves the second parameter
    with open(path) as json_file:  # convert the json to yaml
        json_string = json.load(json_file)  # loads json from file to variable in python
    yaml_conversion = yaml.dump(json_string)  # converts the loaded json data to yaml format
    path_cwd = os.getcwd()  # gets current working directory and saves it to a string
    filename = "yaml_output.yml"  # defines the output file name with the yaml extension
    filepath = os.path.join(path_cwd, filename)  # creates the full filepath for the converted yaml file

    with open(filepath, "w") as file1:  # opens the intended file that the yaml will be saved to
        file1.write(yaml_conversion)  # stores the yaml conversion in the file we defined earlier
