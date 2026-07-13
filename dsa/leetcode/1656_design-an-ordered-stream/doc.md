# Design an Ordered Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1656 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-an-ordered-stream](https://leetcode.com/problems/design-an-ordered-stream/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-an-ordered-stream/).

### Goal
Design a stream that receives `(id, value)` pairs and returns the longest
contiguous chunk starting at the current pointer whenever a value is inserted.

### Function Contract
**Inputs**

- `n`: the number of stream positions.
- `insert(idKey, value)`: stores `value` at 1-based position `idKey`.

**Return value**

Each insert returns the next available contiguous chunk, or an empty list if the
current pointer position is still missing.

### Examples
**Example 1**

- Input: `OrderedStream(5), insert(3, "ccccc"), insert(1, "aaaaa"), insert(2, "bbbbb"), insert(5, "eeeee"), insert(4, "ddddd")`
- Output: `[[], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]`

**Example 2**

- Input: `OrderedStream(3), insert(1, "x"), insert(3, "z"), insert(2, "y")`
- Output: `[["x"], [], ["y", "z"]]`

**Example 3**

- Input: `OrderedStream(1), insert(1, "only")`
- Output: `[["only"]]`

---

## Solution
### Approach
Store values in an array indexed by id and keep a pointer to the first not-yet
returned position. After each insertion, advance the pointer while values are
present, collecting the chunk along the way.

### Complexity Analysis
- **Time Complexity**: `O(total returned values)` across all calls; each stored value is returned once.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
