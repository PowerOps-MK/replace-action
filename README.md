# Replace - Docker Action

GitHub Action to replace string in files

## Usage

### Example workflow
This example replaces `hello` with `world` in all of your project files.

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Find and Replace
        uses: powerops-mk/replace-action@main
        with:
          path: ./app
          filter: *.yml
          find: XYZ_NAME
```

### Inputs

| Input                  | Description                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `path` | The path of the files to replace |
| `json` | JSON file to match file with replace String |
| `find` | The String to search in files |

### Outputs

| Output          | Description                                 |
| --------------- | ------------------------------------------- |
| `modified_count` | The number of files that have been modified |
