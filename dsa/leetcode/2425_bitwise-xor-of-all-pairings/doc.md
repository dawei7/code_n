# Bitwise XOR of All Pairings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2425 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [bitwise-xor-of-all-pairings](https://leetcode.com/problems/bitwise-xor-of-all-pairings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/bitwise-xor-of-all-pairings/).

### Goal
Given two integer arrays, `nums1` and `nums2`, calculate the bitwise XOR sum of all possible pairs `(x, y)` where `x` is an element from `nums1` and `y` is an element from `nums2`.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- An integer representing the XOR sum of all `nums1[i] ^ nums2[j]` for all valid indices `i` and `j`.

### Examples
**Example 1**

- Input: `nums1 = [2, 1, 3], nums2 = [10, 2, 5, 0]`
- Output: `13`

**Example 2**

- Input: `nums1 = [1, 2], nums2 = [3, 4]`
- Output: `0`

**Example 3**

- Input: `nums1 = [5], nums2 = [1, 2, 3]`
- Output: `5`

---

## Solution
### Approach
The solution relies on the properties of the XOR operation:
1. **Commutativity and Associativity**: The order of XOR operations does not matter.
2. **Self-Inverse**: `x ^ x = 0` and `x ^ 0 = x`.
3. **Distribution**: Each element in `nums1` appears in the total XOR sum exactly `len(nums2)` times. Similarly, each element in `nums2` appears exactly `len(nums1)` times.
If `len(nums2)` is even, every element in `nums1` cancels itself out. If `len(nums2)` is odd, the XOR sum of all elements in `nums1` contributes to the result. The same logic applies to `nums2` based on the parity of `len(nums1)`.

### Complexity Analysis
- **Time Complexity**: `O(N + M)`, where `N` is the length of `nums1` and `M` is the length of `nums2`, as we iterate through each array exactly once.
- **Space Complexity**: `O(1)`, as we only use a few variables to store the running XOR sums.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    """
    Calculates the XOR sum of all pairs (x, y) where x in nums1 and y in nums2.
    If len(nums2) is odd, all elements in nums1 contribute to the result.
    If len(nums1) is odd, all elements in nums2 contribute to the result.
    """
    xor1 = 0
    xor2 = 0

    if len(nums2) % 2 == 1:
        for num in nums1:
            xor1 ^= num

    if len(nums1) % 2 == 1:
        for num in nums2:
            xor2 ^= num

    return xor1 ^ xor2
```
</details>
