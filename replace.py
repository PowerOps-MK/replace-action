import os

files_path = os.environ["INPUT_PATH"]
files_filter = os.environ["INPUT_FILTER"]

print(files_path)

echo "time=files_filter" >> $GITHUB_OUTPUT
