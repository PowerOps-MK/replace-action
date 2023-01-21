import glob
import json
import os

files_path = os.environ["INPUT_PATH"]
files_json = os.environ["INPUT_JSON"]
find = os.environ["INPUT_FIND"]
output_file = os.environ["GITHUB_OUTPUT"]

z = f"{files_path}/*.*"
y = glob.glob(z)

modified_count = len(y)
with open(output_file, "a") as file:
    o = f"count={modified_count}"
    file.write(o)

for k in y:
    # Read in the file
    with open(k, "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(find, "XYZ")

    # Write the file out again
    with open(k, "w") as file:
        file.write(filedata)

aList = json.loads(files_json)
print(aList)
