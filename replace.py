import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]
output_file = os.environ["GITHUB_OUTPUT"]

print(files_path)
    
with open(output_file, "a") as file:
    file.write(f"time={files_filter}")
