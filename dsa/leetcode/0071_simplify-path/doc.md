# Simplify Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 71 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/simplify-path/) |

## Problem Description
### Goal
You are given an absolute path for a Unix-style file system, beginning at root `/`. Slash characters separate components; repeated slashes act as one. A component `.` means the current directory, while `..` moves to the parent unless the path is already at root.

Return the simplified canonical path with exactly one slash between retained directory names and no trailing slash unless the answer is root itself. Components such as `...` or `.hidden` are ordinary names, not navigation commands. The result must contain neither `.` nor `..` components.

### Function Contract
**Inputs**

- `path`: an absolute path beginning with `/`

**Return value**

The canonical absolute path with one separator between components, no trailing separator unless the result is root, and no `.` or `..` components.

### Examples
**Example 1**

- Input: `path = "/home/"`
- Output: `"/home"`

**Example 2**

- Input: `path = "/home//foo/"`
- Output: `"/home/foo"`

**Example 3**

- Input: `path = "/home/user/Documents/../Pictures"`
- Output: `"/home/user/Pictures"`
