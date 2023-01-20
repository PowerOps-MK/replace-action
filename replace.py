import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]

print(files_path)

print(f"::set-output name=time::{files_filter}")
