# Smallest Substring With Identical Characters I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3398 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-substring-with-identical-characters-i](https://leetcode.com/problems/smallest-substring-with-identical-characters-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-substring-with-identical-characters-i/).

### Goal
Given a binary string `s` and an integer `numOps`, determine the minimum possible value of the maximum length of any contiguous substring consisting of identical characters, after performing at most `numOps` operations. An operation consists of flipping a character (changing '0' to '1' or vice versa).

### Function Contract
**Inputs**

- `s` (str): A binary string consisting of '0's and '1's.
- `numOps` (int): The maximum number of character flips allowed.

**Return value**

- `int`: The smallest possible value for the maximum length of any contiguous block of identical characters.

### Examples
**Example 1**

- Input: `s = "000001", numOps = 1`
- Output: `2`

**Example 2**

- Input: `s = "0000", numOps = 2`
- Output: `1`

**Example 3**

- Input: `s = "0101", numOps = 0`
- Output: `1`

---

## Solution
### Approach
The problem exhibits a monotonic property: if it is possible to achieve a maximum identical substring length of `k`, it is also possible for any length greater than `k`. This allows us to use **Binary Search on the Answer**. For a fixed length `mid`, we calculate the minimum number of operations required to ensure no contiguous block exceeds length `mid`. This is done by identifying all contiguous blocks of identical characters and calculating how many flips are needed to break them into segments of size at most `mid`.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the string. The binary search runs in `O(log n)` iterations, and each check takes `O(n)` time to traverse the string.
- **Space Complexity**: `O(n)` to store the lengths of contiguous blocks, though this can be optimized to `O(1)` by processing the string on the fly.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str, numOps: int) -> int:
    if not s:
        return 0

    # Identify lengths of contiguous blocks of identical characters
    blocks = []
    if not s:
        return 0

    curr_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_len += 1
        else:
            blocks.append(curr_len)
            curr_len = 1
    blocks.append(curr_len)

    def can_achieve(max_len: int) -> bool:
        if max_len == 1:
            start_zero = sum(char != ("0" if index % 2 == 0 else "1") for index, char in enumerate(s))
            start_one = len(s) - start_zero
            return min(start_zero, start_one) <= numOps
        if max_len == 0:
            return False
        ops_needed = 0
        for length in blocks:
            if length > max_len:
                # To break a block of size 'length' into pieces of size 'max_len',
                # we need floor(length / (max_len + 1)) operations.
                ops_needed += length // (max_len + 1)
        return ops_needed <= numOps

    # Binary search for the minimum possible maximum length
    low = 1
    high = len(s)
    ans = len(s)

    while low <= high:
        mid = (low + high) // 2
        if can_achieve(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```
</details>
