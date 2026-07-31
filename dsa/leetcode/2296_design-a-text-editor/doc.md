# Design a Text Editor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2296 |
| Difficulty | Hard |
| Topics | Array, Linked List, String, Design, Stack, Doubly-Linked List, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-text-editor/) |

## Problem Description
### Goal
Design a text editor whose cursor always occupies a position between
characters, from position zero through the current text length. The editor
starts empty and supports these stateful operations:

- `addText(text)` inserts all of `text` at the cursor and leaves the cursor
  immediately after the inserted text.
- `deleteText(k)` acts like backspace: it removes up to `k` characters
  directly to the left of the cursor and returns how many were removed.
- `cursorLeft(k)` moves left by up to `k` positions without passing the start.
- `cursorRight(k)` moves right by up to `k` positions without passing the end.

Each cursor movement returns the suffix of at most ten characters immediately
to the left of the cursor after moving. If no character lies there, it returns
the empty string.

### Function Contract
**Inputs**

- `operations`: A trace beginning with `"TextEditor"` and followed by supported method names.
- `arguments`: The aligned constructor and method arguments for that trace.

Each inserted `text` and each `k` has size or value from 1 through 40; inserted
text contains lowercase English letters. Across one editor instance, at most
$2\cdot10^4$ method calls are made.

**Return value**

An aligned trace containing `null` for construction and `addText`, the actual
deletion count for `deleteText`, and the requested left-context string for
each cursor movement.

### Examples
**Example 1**

- Input: `operations = ["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]`, `arguments = [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]`
- Output: `[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]`
