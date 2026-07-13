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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Tokenize by separators, then interpret navigation components**

Split on `/`. Repeated separators create empty components, which do nothing. A component exactly equal to `.` also preserves the current location. A component exactly equal to `..` pops the most recent stored directory when one exists; at root, it has no effect. Push every other nonempty component unchanged.

The comparisons must be exact. Names such as `...`, `.hidden`, and `..data` are ordinary directory names, not navigation instructions.

**The stack already is the canonical component sequence**

Join the remaining stack with single separators and prepend `/`. An empty stack naturally produces the root path `/`.

**Root is an unpoppable lower boundary**

After each component, the stack is the canonical sequence of directories reached by the processed prefix. It contains neither separators nor `.`/`..` navigation markers. Ignoring `..` when the stack is empty models the rule that an absolute path cannot move above root.

**Trace repeated separators and parent navigation**

For `/home/user/Documents/../Pictures`, push `home`, `user`, and `Documents`; `..` removes `Documents`; then push `Pictures`. Joining yields `/home/user/Pictures`.

**The stack mirrors every directory transition**

Empty and `.` components leave the current location unchanged. An ordinary name descends one level and is pushed; `..` ascends one level by popping when possible, while an empty stack correctly keeps the path at root.

After each component, the stack therefore lists exactly the directory names from root to the current destination. Joining that list with single separators removes all redundant syntax and yields the unique canonical absolute path.

#### Complexity detail

Splitting, classifying, and joining process $O(n)$ total characters. The component stack and returned path use $O(n)$ space.

#### Alternatives and edge cases

- **Repeated string replacement:** becomes brittle for interacting `//`, `.`, and `..` patterns and can copy the path many times.
- **Regular expressions alone:** can collapse separators but do not naturally model parent-directory state.
- **Manual character tokenizer:** avoids the split list and can reduce temporary allocations, but uses the same stack logic with more parsing code.
- `/../` simplifies to `/`, while `/.../` remains `/...`. A trailing separator never appears in the result unless the result is root.
- The input is absolute. Relative paths would need different behavior for leading unresolved `..` components.

</details>
