# Shuffle String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1528 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shuffle-string](https://leetcode.com/problems/shuffle-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shuffle-string/).

### Goal
Rearrange the characters of `s` so that the character originally at index `i`
moves to index `indices[i]`.

### Function Contract
**Inputs**

- `s`: the original string.
- `indices`: a permutation of positions in `s`.

**Return value**

The restored string after placing each character at its target index.

### Examples
**Example 1**

- Input: `s = "codeleet", indices = [4, 5, 6, 7, 0, 2, 1, 3]`
- Output: `"leetcode"`

**Example 2**

- Input: `s = "abc", indices = [0, 1, 2]`
- Output: `"abc"`

**Example 3**

- Input: `s = "aiohn", indices = [3, 1, 4, 2, 0]`
- Output: `"nihao"`

---

## Solution
### Approach
Allocate a character array of the same length as `s`, then for each original
index place `s[i]` into `result[indices[i]]`. Join the result array at the end.

### Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s, indices):
    if not s:
        return ""
    result = [""] * len(s)
    extras = []
    for i, ch in enumerate(s):
        target = indices[i] if i < len(indices) else i
        if 0 <= target < len(s) and result[target] == "":
            result[target] = ch
        else:
            extras.append(ch)
    extra_index = 0
    for i in range(len(result)):
        if result[i] == "":
            if extra_index < len(extras):
                result[i] = extras[extra_index]
                extra_index += 1
            else:
                result[i] = s[i]
    return "".join(result)
```
</details>
