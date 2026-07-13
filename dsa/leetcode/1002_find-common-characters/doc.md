# Find Common Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1002 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-common-characters](https://leetcode.com/problems/find-common-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-common-characters/).

### Goal
Given a list of lowercase words, return all characters that appear in every word. If a character appears multiple times in every word, include it that many times in the result.

### Function Contract
**Inputs**

- `words`: List[str]

**Return value**

List[str] - common characters with multiplicity

### Examples
**Example 1**

- Input: `words = ["bella", "label", "roller"]`
- Output: `["e", "l", "l"]`

**Example 2**

- Input: `words = ["cool", "lock", "cook"]`
- Output: `["c", "o"]`

**Example 3**

- Input: `words = ["abc", "def"]`
- Output: `[]`

---

## Solution
### Approach
Frequency-count intersection.

### Complexity Analysis
- **Time Complexity**: `O(total characters)`
- **Space Complexity**: `O(1)` for the fixed lowercase alphabet

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1002: Find Common Characters."""

from collections import Counter


def solve(words: list[str]) -> list[str]:
    common = Counter(words[0])
    for word in words[1:]:
        common &= Counter(word)

    answer: list[str] = []
    for char in sorted(common):
        answer.extend([char] * common[char])
    return answer
```
</details>
