# Find The Original Array of Prefix Xor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2433 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-original-array-of-prefix-xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/).

### Goal
Given an array `pref` representing the prefix XORs of an unknown original array `arr`, reconstruct the original array. The relationship is defined such that `pref[i]` is the result of XORing all elements from `arr[0]` to `arr[i]`.

### Function Contract
**Inputs**

- `pref`: A list of integers where `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.

**Return value**

- A list of integers representing the original array `arr`.

### Examples
**Example 1**

- Input: `pref = [5, 2, 0, 3, 1]`
- Output: `[5, 7, 2, 3, 2]`

**Example 2**

- Input: `pref = [13]`
- Output: `[13]`

**Example 3**

- Input: `pref = [5, 2]`
- Output: `[5, 7]`

---

## Solution
### Approach
The solution relies on the inverse property of the XOR operation. Since `pref[i] = pref[i-1] ^ arr[i]` (for `i > 0`), we can isolate `arr[i]` by XORing both sides by `pref[i-1]`, yielding `arr[i] = pref[i] ^ pref[i-1]`. The first element remains `arr[0] = pref[0]`.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we perform a single pass to compute the XOR differences.
- **Space Complexity**: O(n) to store the resulting array, or O(1) auxiliary space if we modify the input array in-place.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(pref: List[int]) -> List[int]:
    """
    Reconstructs the original array from its prefix XOR array.

    Logic:
    pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
    pref[i-1] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]
    Therefore, pref[i] ^ pref[i-1] = arr[i]
    """
    n = len(pref)
    if n == 0:
        return []

    res = [0] * n
    res[0] = pref[0]

    for i in range(1, n):
        res[i] = pref[i] ^ pref[i-1]

    return res
```
</details>
