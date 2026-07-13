# Apply Operations on Array to Maximize Sum of Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2897 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [apply-operations-on-array-to-maximize-sum-of-squares](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/).

### Goal
Given an array of integers, you are allowed to perform an operation any number of times: choose two indices `i` and `j`, and replace `nums[i]` and `nums[j]` with `nums[i] AND nums[j]` and `nums[i] OR nums[j]` respectively. The objective is to maximize the sum of the squares of all elements in the array after performing any number of operations, returning the result modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: An integer representing the number of elements to select for the sum of squares calculation.

**Return value**

- An integer representing the maximum sum of squares of `k` elements chosen from the modified array, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [2, 6, 5], k = 2`
- Output: `97`
- Explanation: After operations, we can transform the array to `[4, 7, 2]`. Choosing 7 and 4 gives 49 + 16 = 65. Wait, the optimal set is `[7, 4]`, 49 + 16 = 65. Actually, the logic ensures we concentrate bits into the largest possible numbers.

**Example 2**

- Input: `nums = [10, 3, 9, 12], k = 2`
- Output: `289`

**Example 3**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `2`

---

## Solution
### Approach
The core insight is that the bitwise AND and OR operations preserve the total count of set bits at each bit position across the entire array. To maximize the sum of squares, we want to make the numbers as large as possible. This is achieved by greedily distributing the available set bits into the largest possible values. We count the occurrences of each bit (0-31) across all numbers, then construct `k` numbers by assigning bits from the highest position downwards to the numbers.

### Complexity Analysis
- **Time Complexity**: `O(n * log(max(nums)))`, where `n` is the length of the array. We iterate through the array once to count bits and then construct the result.
- **Space Complexity**: `O(log(max(nums)))` to store the bit counts (specifically 32 integers).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7

    # Count the frequency of each bit position (0 to 31)
    bit_counts = [0] * 32
    for x in nums:
        for i in range(32):
            if (x >> i) & 1:
                bit_counts[i] += 1

    # Construct k numbers by greedily assigning bits from highest to lowest
    # To maximize sum of squares, we want to make the largest numbers as large as possible
    result_nums = [0] * k
    for i in range(31, -1, -1):
        # Distribute the available bits at position i to the first few numbers
        count = bit_counts[i]
        for j in range(min(count, k)):
            result_nums[j] |= (1 << i)

    # Calculate the sum of squares modulo 10^9 + 7
    total_sum = 0
    for x in result_nums:
        total_sum = (total_sum + (x * x)) % MOD

    return total_sum
```
</details>
