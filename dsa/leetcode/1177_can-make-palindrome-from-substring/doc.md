# Can Make Palindrome from Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1177 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [can-make-palindrome-from-substring](https://leetcode.com/problems/can-make-palindrome-from-substring/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/can-make-palindrome-from-substring/).

### Goal
For each substring query, decide whether the substring can be rearranged into a palindrome after changing at most `k` characters.

### Function Contract
**Inputs**

- `s`: lowercase string.
- `queries`: list of `[left, right, k]` queries with inclusive indices.

**Return value**

Boolean answers for the queries in order.

### Examples
**Example 1**

- Input: `s = "abcda"`, `queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]`
- Output: `[true,false,false,true,true]`

**Example 2**

- Input: `s = "aaaa"`, `queries = [[0,3,0],[1,2,0],[0,1,1]]`
- Output: `[true,true,true]`

**Example 3**

- Input: `s = "abc"`, `queries = [[0,2,1],[0,2,0]]`
- Output: `[true,false]`

---

## Solution
### Approach
Prefix parity masks and palindrome parity counting.

### Complexity Analysis
- **Time Complexity**: `O(len(s) + q)`
- **Space Complexity**: `O(len(s))`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s, queries):
    masks = [0]
    for ch in s:
        masks.append(masks[-1] ^ (1 << (ord(ch) - ord("a"))))

    answers = []
    for left, right, k in queries:
        odd_count = (masks[right + 1] ^ masks[left]).bit_count()
        answers.append(odd_count // 2 <= k)
    return answers
```
</details>
