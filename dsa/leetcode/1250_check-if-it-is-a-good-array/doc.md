# Check If It Is a Good Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1250 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-it-is-a-good-array](https://leetcode.com/problems/check-if-it-is-a-good-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-it-is-a-good-array/).

### Goal
Decide whether some integer linear combination of the array values can equal `1`.

### Function Contract
**Inputs**

- `nums`: positive integer array.

**Return value**

`true` if there exist integers multiplying the array values whose sum is `1`, otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [12,5,7,23]`
- Output: `true`

**Example 2**

- Input: `nums = [29,6,10]`
- Output: `true`

**Example 3**

- Input: `nums = [3,6]`
- Output: `false`

---

## Solution
### Approach
Greatest common divisor and Bezout's identity.

### Complexity Analysis
- **Time Complexity**: `O(n log M)` where `M` is the largest value.
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from math import gcd


def solve(nums):
    current = 0
    for value in nums:
        current = gcd(current, value)
        if current == 1:
            return True
    return False
```
</details>
