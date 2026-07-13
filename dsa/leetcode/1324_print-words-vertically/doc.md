# Print Words Vertically

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1324 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [print-words-vertically](https://leetcode.com/problems/print-words-vertically/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/print-words-vertically/).

### Goal
Given a sentence, write its words top-to-bottom in columns and return the resulting vertical rows. Trailing spaces must be removed from each returned row.

### Function Contract
**Inputs**

- `s`: sentence containing words separated by single spaces.

**Return value**

The vertical reading of the sentence as a list of strings.

### Examples
**Example 1**

- Input: `s = "HOW ARE YOU"`
- Output: `["HAY","ORO","WEU"]`

**Example 2**

- Input: `s = "TO BE OR NOT"`
- Output: `["TBON","OERO","   T"]`

**Example 3**

- Input: `s = "CONTEST IS COMING"`
- Output: `["CIC","OSO","N M","T I","E N","S G","T"]`

---

## Solution
### Approach
String matrix simulation.

### Complexity Analysis
- **Time Complexity**: `O(total characters including padding)`
- **Space Complexity**: `O(total characters in output)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1324: Print Words Vertically."""


def solve(s: str) -> list[str]:
    words = s.split()
    width = max(len(word) for word in words)
    rows: list[str] = []
    for col in range(width):
        chars = [word[col] if col < len(word) else " " for word in words]
        rows.append("".join(chars).rstrip())
    return rows
```
</details>
