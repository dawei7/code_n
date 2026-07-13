# Make Two Arrays Equal by Reversing Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1460 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [make-two-arrays-equal-by-reversing-subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/).

### Goal
Decide whether `arr` can be transformed into `target` by reversing any number of subarrays.

### Function Contract
**Inputs**

- `target`: the desired array.
- `arr`: the array that may be changed by subarray reversals.

**Return value**

`true` if the transformation is possible, otherwise `false`.

### Examples
**Example 1**

- Input: `target = [1,2,3,4], arr = [2,4,1,3]`
- Output: `true`

**Example 2**

- Input: `target = [7], arr = [7]`
- Output: `true`

**Example 3**

- Input: `target = [3,7,9], arr = [3,7,11]`
- Output: `false`

---

## Solution
### Approach
Multiset equality. Since arbitrary subarray reversals can permute elements, the arrays are interchangeable exactly when they contain the same values with the same frequencies.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(target, arr):
    return Counter(target) == Counter(arr)
```
</details>
