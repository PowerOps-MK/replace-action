import glob
import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]
output_file = os.environ["GITHUB_OUTPUT"]

z = f"{files_path}/{files_filter}"
y = glob.glob(z)
for file in glob.glob(z):
   print(file)


modified_count = len(y)
with open(output_file, "a") as file:
    file.write(f"count={modified_count}")
