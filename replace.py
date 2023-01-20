import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]

os.environ["GITHUB_OUTPUT"] = "test=output"

print(files_path + files_filter)
