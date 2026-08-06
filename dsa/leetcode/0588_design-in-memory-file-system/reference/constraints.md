## Constraints

- `1 <= path.length, filePath.length <= 100`
- `path` and `filePath` are absolute paths beginning with `/`; only the root path `/` may end with `/`.
- Directory and file names contain only lowercase letters, and equal names do not coexist within one directory.
- Every operation receives valid parameters; no call tries to read content from or list a file or directory that does not exist.
- The parent directory for every file passed to `addContentToFile` already exists.
- `1 <= content.length <= 50`
- At most `300` total calls are made to `ls`, `mkdir`, `addContentToFile`, and `readContentFromFile`.
