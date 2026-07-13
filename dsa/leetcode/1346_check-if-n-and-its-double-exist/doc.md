# Check If N and Its Double Exist

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1346 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-n-and-its-double-exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-n-and-its-double-exist/).

### Goal
Determine whether the array contains two different indices `i` and `j` such that `arr[i]` is exactly twice `arr[j]`.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

`true` if such a pair exists, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [10,2,5,3]`
- Output: `true`

**Example 2**

- Input: `arr = [3,1,7,11]`
- Output: `false`

**Example 3**

- Input: `arr = [0,0]`
- Output: `true`

---

## Solution
### Approach
Hash-set lookup.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(arr):
    seen = set()
    for value in arr:
        if 2 * value in seen or (value % 2 == 0 and value // 2 in seen):
            return True
        seen.add(value)
    return False
```
</details>
