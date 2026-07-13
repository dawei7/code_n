# Check If Array Pairs Are Divisible by k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1497 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-array-pairs-are-divisible-by-k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/).

### Goal
Decide whether the array can be partitioned into pairs whose sums are all divisible by `k`.

### Function Contract
**Inputs**

- `arr`: a list of integers.
- `k`: the divisor.

**Return value**

`true` if such a pairing exists, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5,10,6,7,8,9], k = 5`
- Output: `true`

**Example 2**

- Input: `arr = [1,2,3,4,5,6], k = 7`
- Output: `true`

**Example 3**

- Input: `arr = [1,2,3,4,5,6], k = 10`
- Output: `false`

---

## Solution
### Approach
Remainder counting. Remainder `0` values must pair among themselves, and every remainder `r` must have the same count as remainder `k - r`; when `k` is even, remainder `k/2` must also have even count.

### Complexity Analysis
- **Time Complexity**: `O(n + k)`
- **Space Complexity**: `O(k)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(arr, k):
    k = abs(int(k)) or 1
    counts = Counter(num % k for num in arr)
    if counts.get(0, 0) % 2:
        return False
    for rem in range(1, k):
        if counts.get(rem, 0) != counts.get((-rem) % k, 0):
            return False
    return True
```
</details>
