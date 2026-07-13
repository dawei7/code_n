# Maximum Possible Number by Binary Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3309 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-possible-number-by-binary-concatenation](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/).

### Goal
Given an array of three integers, determine the largest possible integer that can be formed by concatenating the binary representations of these three integers in any arbitrary order.

### Function Contract
**Inputs**

- `nums`: A list of exactly three integers (where each integer is between 1 and 127).

**Return value**

- An integer representing the maximum value achievable after concatenating the binary strings of the input numbers in any permutation.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `30`
- Explanation: Binary representations are 1 (1), 2 (10), 3 (11). Concatenating as 3, 2, 1 gives "11101" which is 29, but 3, 1, 2 gives "11110" which is 30.

**Example 2**

- Input: `nums = [2, 8, 16]`
- Output: `1296`
- Explanation: Concatenating 16, 8, 2 gives "10000100010" which is 1296.

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `7`
- Explanation: Concatenating 1, 1, 1 gives "111" which is 7.

---

## Solution
### Approach
The problem is solved using **Permutation Enumeration**. Since the input array size is fixed at 3, there are only $3! = 6$ possible permutations. We generate all permutations, convert each integer to its binary string representation (excluding the '0b' prefix), concatenate them, and convert the resulting binary string back to a decimal integer to find the maximum.

### Complexity Analysis
- **Time Complexity**: $O(1)$. Since the input size is fixed at 3, the number of permutations is constant (6), and the bit length of each number is small (max 7 bits), leading to constant time execution.
- **Space Complexity**: $O(1)$. We only store a constant number of strings and integers regardless of the input values.

### Reference Implementations
<details>
<summary>python</summary>

```python
from itertools import permutations

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum possible number by concatenating the binary
    representations of the three integers in nums in any order.
    """
    max_val = 0

    # Generate all permutations of the input list
    for p in permutations(nums):
        # Convert each number to binary string, removing the '0b' prefix
        binary_str = "".join(bin(x)[2:] for x in p)

        # Convert the concatenated binary string back to an integer
        current_val = int(binary_str, 2)

        # Update the maximum value found so far
        if current_val > max_val:
            max_val = current_val

    return max_val
```
</details>
