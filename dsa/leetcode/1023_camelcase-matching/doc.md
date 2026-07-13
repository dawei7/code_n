# Camelcase Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1023 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Trie, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [camelcase-matching](https://leetcode.com/problems/camelcase-matching/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/camelcase-matching/).

### Goal
For each query string, decide whether it can match a pattern after inserting any number of lowercase letters into the pattern. Extra uppercase letters are not allowed.

### Function Contract
**Inputs**

- `queries`: List[str]
- `pattern`: str

**Return value**

List[bool] - match result for each query

### Examples
**Example 1**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FB"`
- Output: `[True, False, True, True, False]`

**Example 2**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FoBa"`
- Output: `[True, False, True, False, False]`

**Example 3**

- Input: `queries = ["CompetitiveProgramming", "CounterPick", "ControlPanel"], pattern = "CooP"`
- Output: `[False, False, True]`

---

## Solution
### Approach
Two-pointer subsequence matching with uppercase constraints.

### Complexity Analysis
- **Time Complexity**: `O(total query characters)`
- **Space Complexity**: `O(1)` auxiliary space excluding output

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1023: Camelcase Matching."""


def solve(queries: list[str], pattern: str) -> list[bool]:
    def matches(query: str) -> bool:
        i = 0
        for char in query:
            if i < len(pattern) and char == pattern[i]:
                i += 1
            elif char.isupper():
                return False
        return i == len(pattern)

    return [matches(query) for query in queries]
```
</details>
