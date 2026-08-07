## Description

You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters. For example, "`/leetcode"` and "`/leetcode/problems"` are valid paths while an empty string `""` and `"/"` are not.

Implement the `FileSystem` class:

- `bool createPath(string path, int value)` Creates a new `path` and associates a `value` to it if possible and returns `true`. Returns `false` if the path **already exists** or its parent path **doesn't exist**.

- `int get(string path)` Returns the value associated with `path` or returns `-1` if the path doesn't exist.
### Function Contract

**Source-native class**

- `FileSystem()`: Initialize an empty file system.
- `createPath(path, value)`: Create `path`, associate it with `value`, and return `true` only when `path` is new and its immediate parent exists. Otherwise return `false` without changing the system. The implicit root permits a one-component path to be created directly.
- `get(path)`: Return the value associated with `path`, or `-1` if that path does not exist.

**App-local input**

- `operations`: A sequence of `createPath` and `get` calls, each represented by its method name and argument list. The adapter constructs one empty `FileSystem`, performs the calls in order, and returns their results in the same order. The source-native constructor entry and its `null` result are omitted from this adapted sequence.

Let

$S = \sum_{o \in \text{operations}} \lvert \operatorname{path}(o) \rvert$

be the total number of path characters processed across all calls.

**Return value**

- A list containing each operation's boolean or integer result in execution order.

### Examples

#### Example 1

- **Input:** ``
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
- **Output:** ``
[null,true,1]
- **Explanation:**
FileSystem fileSystem = new FileSystem();
fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
#### Example 2

- **Input:** ``
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
- **Output:** ``
[null,true,true,2,false,-1]
- **Explanation:**
FileSystem fileSystem = new FileSystem();
fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
### Constraints

- $2 \le \text{path.length} \le 100$

- $1 \le value \le 10^{9}$

- Each `path` is **valid** and consists of lowercase English letters and `'/'`.

- At most $10^{4}$ calls **in total** will be made to `createPath` and `get`.