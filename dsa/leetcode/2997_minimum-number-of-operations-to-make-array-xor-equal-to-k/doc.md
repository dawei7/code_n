# Minimum Number of Operations to Make Array XOR Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2997 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-operations-to-make-array-xor-equal-to-k](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/).

### Goal
Given an array of integers and a target integer `k`, determine the minimum number of bit-flipping operations required to make the XOR sum of all elements in the array equal to `k`. A single operation consists of flipping any bit (changing 0 to 1 or 1 to 0) of any element in the array.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the target XOR sum.

**Return value**

- An integer representing the minimum number of bit flips needed.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 4], k = 1`
- Output: `2`

**Example 2**

- Input: `nums = [2, 0, 2, 0], k = 0`
- Output: `0`

**Example 3**

- Input: `nums = [4], k = 3`
- Output: `2`

---

## Solution
### Approach
The problem relies on the properties of the XOR operation. Specifically, the XOR sum of the entire array can be computed first. Let `current_xor` be the XOR sum of all elements in `nums`. The goal is to transform `current_xor` into `k`. The bits that differ between `current_xor` and `k` represent the positions where a flip is required. This is equivalent to calculating the Hamming distance between `current_xor` and `k`, which can be found by counting the number of set bits (1s) in the result of `current_xor ^ k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the array, as we must iterate through the array once to compute the total XOR sum.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space to store the XOR sum and the bit count.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum number of bit flips to make the XOR sum of nums equal to k.
    """
    # Calculate the XOR sum of all elements in the array
    current_xor = 0
    for num in nums:
        current_xor ^= num

    # The bits that need to be flipped are exactly the bits that differ
    # between the current_xor and the target k.
    # XORing current_xor and k gives a number where each set bit
    # represents a difference at that position.
    diff = current_xor ^ k

    # The number of operations is the count of set bits (population count)
    return bin(diff).count('1')
```
</details>
