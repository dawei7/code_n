# Find Words Containing Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2942 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-words-containing-character](https://leetcode.com/problems/find-words-containing-character/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-words-containing-character/).

### Goal
Given a collection of strings and a target character, identify the indices of all strings in the collection that contain the specified character at least once. The result should be a list of these indices in the order they appear in the input array.

### Function Contract
**Inputs**

- `words`: A list of strings (`List[str]`).
- `x`: A single character (`str`).

**Return value**

- A list of integers (`List[int]`) representing the indices of the strings that contain the character `x`.

### Examples
**Example 1**

- Input: `words = ["leet","code"], x = "e"`
- Output: `[0, 1]`

**Example 2**

- Input: `words = ["abc","bcd","aaaa","cbc"], x = "a"`
- Output: `[0, 2]`

**Example 3**

- Input: `words = ["abc","bcd","aaaa","cbc"], x = "z"`
- Output: `[]`

---

## Solution
### Approach
The problem utilizes a linear scan (iteration) over the input array. For each string, we perform a membership check (substring search) to determine if the target character exists within the string.

### Complexity Analysis
- **Time Complexity**: `O(n * m)`, where `n` is the number of words in the list and `m` is the average length of each word. We must inspect each character of every word in the worst case.
- **Space Complexity**: `O(k)`, where `k` is the number of indices returned. In the worst case, this is `O(n)` if all words contain the character.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(words: List[str], x: str) -> List[int]:
    """
    Returns a list of indices of words that contain the character x.
    """
    result = []
    for index, word in enumerate(words):
        if x in word:
            result.append(index)
    return result
```
</details>
