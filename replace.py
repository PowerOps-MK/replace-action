import glob
import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]
output_file = os.environ["GITHUB_OUTPUT"]

z = f"{files_path}/{files_filter}"
y = glob.glob(z)
for file in y:
    with open(file, "r") as fil:
        print(fil.read())

modified_count = len(y)
with open(output_file, "a") as fil:
    o = f"count={modified_count}"
    fil.write(o)
