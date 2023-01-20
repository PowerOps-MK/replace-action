import glob
import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]
output_file = os.environ["GITHUB_OUTPUT"]

with open(output_file, "a") as file:
    file.write(f"time={files_filter}")

y = glob.glob(files_filter)
print(y)
