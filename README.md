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
```

### Inputs

| Input                  | Description                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |

### Outputs

| Output          | Description                                 |
| --------------- | ------------------------------------------- |
| `modifiedFiles` | The number of files that have been modified |
