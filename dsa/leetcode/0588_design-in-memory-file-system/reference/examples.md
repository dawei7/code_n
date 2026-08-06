## Examples

**Example 1**

- **Input:** `operations = ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"], arguments = [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]`

- **Output:** `[null,[],null,null,["a"],"hello"]`

- **Explanation:** The source image presents the call sequence as this operation table:

| Operation | Output | Explanation |
|---|---|---|
| `FileSystem fileSystem = new FileSystem()` | `null` | Construct an empty file system. |
| `fileSystem.ls("/")` | `[]` | The root directory initially contains no names. |
| `fileSystem.mkdir("/a/b/c")` | `null` | Create directory `a` under `/`, then `b` under `a`, and finally `c` under `b`. |
| `fileSystem.addContentToFile("/a/b/c/d", "hello")` | `null` | Create file `d` inside `/a/b/c` with content `"hello"`. |
| `fileSystem.ls("/")` | `["a"]` | Directory `a` is now the root's only immediate entry. |
| `fileSystem.readContentFromFile("/a/b/c/d")` | `"hello"` | Return the stored file content. |
