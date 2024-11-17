import json
import os

# this is to get the full path of the file, this is because when running the code outside its directory
# issues happen with the interpreter, this makes sure those issues do not happen
# os.sep is the file path separator for which ever OS you are using 
full_file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "tasks.json"

# this function reads the json file and returns its content as python data types
def load_tasks_json():
    # open the json file for reading 
    with open(full_file_path,'r') as f:
        # read the json content and load them as python data types
        list_of_tasks = json.loads(f.read())
    # return the parsed content
    return list_of_tasks

# this function writes a python data structure to a json file
def save_tasks_json(list_of_tasks):
    # open the json file for reading 
    with open(full_file_path,'w') as f:
        # write the content to the json file
        json.dump(list_of_tasks, f, indent=4)

