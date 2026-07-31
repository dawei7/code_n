## Examples

**Example 1**

- Input: `path = "/home/"`
- Output: `"/home"`
- Explanation: Canonical form removes the trailing slash.

**Example 2**

- Input: `path = "/home//foo/"`
- Output: `"/home/foo"`
- Explanation: Consecutive separators collapse to one slash, and the trailing slash is removed.

**Example 3**

- Input: `path = "/home/user/Documents/../Pictures"`
- Output: `"/home/user/Pictures"`
- Explanation: Component `..` moves from `Documents` back to its parent before entering `Pictures`.

**Example 4**

- Input: `path = "/../"`
- Output: `"/"`
- Explanation: Navigation cannot move above the root directory.

**Example 5**

- Input: `path = "/.../a/../b/c/../d/./"`
- Output: `"/.../b/d"`
- Explanation: Component `...` is an ordinary directory name, not parent-directory navigation.
