# Maximum Length of a Concatenated String with Unique Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1239 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-length-of-a-concatenated-string-with-unique-characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/).

### Goal
Pick any subsequence of strings, concatenate them in order, and maximize the length of a result that contains no repeated character.

### Function Contract
**Inputs**

- `arr`: list of lowercase strings.

**Return value**

The maximum possible length of a concatenation whose characters are all unique.

### Examples
**Example 1**

- Input: `arr = ["un","iq","ue"]`
- Output: `4`

**Example 2**

- Input: `arr = ["cha","r","act","ers"]`
- Output: `6`

**Example 3**

- Input: `arr = ["abcdefghijklmnopqrstuvwxyz"]`
- Output: `26`

---

## Solution
### Approach
Bitmask backtracking / dynamic set expansion.

### Complexity Analysis
- **Time Complexity**: `O(2^n)` in the number of usable strings.
- **Space Complexity**: `O(2^n)` for the set of reachable masks.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr):
    masks = [0]
    best = 0
    for word in arr:
        mask = 0
        for ch in word:
            bit = 1 << (ord(ch) - ord("a"))
            if mask & bit:
                mask = 0
                break
            mask |= bit
        if mask == 0:
            continue
        for existing in masks[:]:
            if existing & mask == 0:
                combined = existing | mask
                masks.append(combined)
                best = max(best, combined.bit_count())
    return best
```
</details>
