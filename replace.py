import glob
import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]
find = os.environ["INPUT_FIND"]
replace = os.environ["INPUT_REPLACE"]
output_file = os.environ["GITHUB_OUTPUT"]

z = f"{files_path}/{files_filter}"
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
    filedata = filedata.replace(find, replace)

    # Write the file out again
    with open(k, "w") as file:
        file.write(filedata)

    with open(k, "r") as file:
        print(file.read())
