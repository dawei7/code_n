## Description

Design an in-memory file system by implementing `FileSystem` with these operations:

- `FileSystem()` initializes an empty system.
- `ls(path)` returns only the file's name when `path` identifies a file. When `path` identifies a directory, it returns the names of that directory's immediate files and subdirectories in lexicographic order.
- `mkdir(path)` creates the requested directory. The target directory does not already exist, and every missing intermediate directory must also be created.
- `addContentToFile(filePath, content)` creates a missing file with `content`, or appends `content` to the existing file without discarding its earlier contents.
- `readContentFromFile(filePath)` returns the entire content currently stored at `filePath`.
