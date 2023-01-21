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
```

### Inputs

| Input                  | Description                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `path` | The path of the files to replace |
| `filter` | Filter the files in the path |
| `find` | The String to search in files |
| `replace` | The String to replace in files |

### Outputs

| Output          | Description                                 |
| --------------- | ------------------------------------------- |
| `modified_count` | The number of files that have been modified |
