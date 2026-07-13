# Minimum Operations to Make Array Sum Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3512 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-array-sum-divisible-by-k](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/).

### Goal
Given an array of integers and a divisor `k`, determine the minimum number of elements that must be removed from the array such that the sum of the remaining elements is divisible by `k`. If it is impossible to achieve this by removing any number of elements (other than the entire array), return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the divisor.

**Return value**

- An integer representing the minimum number of elements to remove, or -1 if it is impossible to satisfy the condition.

### Examples
**Example 1**

- Input: `nums = [3, 1, 4, 2], k = 6`
- Output: `1`
- Explanation: The total sum is 10. 10 % 6 = 4. Removing the element 4 leaves [3, 1, 2], sum 6, which is divisible by 6.

**Example 2**

- Input: `nums = [6, 3, 5, 2], k = 9`
- Output: `2`
- Explanation: The total sum is 16. 16 % 9 = 7. Removing 5 and 2 leaves [6, 3], sum 9, which is divisible by 9.

**Example 3**

- Input: `nums = [1, 2, 3], k = 3`
- Output: `0`
- Explanation: The total sum is 6, which is already divisible by 3.

---

## Solution
### Approach
The problem is solved using the **Prefix Sum** technique combined with a **Hash Map**.
1. Calculate the total sum of the array and find its remainder `target = total_sum % k`. If `target == 0`, return 0.
2. We need to find the longest subarray whose sum modulo `k` equals `target`.
3. Let `prefix_sum[i]` be the sum of elements from index 0 to `i`. We look for indices `i` and `j` such that `(prefix_sum[j] - prefix_sum[i]) % k == target`.
4. This rearranges to `prefix_sum[i] % k == (prefix_sum[j] % k - target + k) % k`.
5. By storing the latest index of each prefix sum remainder in a hash map, we can find the maximum length of such a subarray in linear time.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array once.
- **Space Complexity**: `O(min(n, k))`, as the hash map stores at most `k` distinct remainders.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    total_sum = sum(nums)
    target = total_sum % k

    if target == 0:
        return 0

    # We want to find the longest subarray with sum % k == target
    # Let prefix_sum[j] % k = p_j and prefix_sum[i] % k = p_i
    # We need (p_j - p_i) % k == target
    # p_i = (p_j - target) % k

    prefix_map = {0: -1}
    current_sum = 0
    max_len = -1

    for i, num in enumerate(nums):
        current_sum = (current_sum + num) % k

        needed = (current_sum - target + k) % k
        if needed in prefix_map:
            max_len = max(max_len, i - prefix_map[needed])

        prefix_map[current_sum] = i

    return len(nums) - max_len if max_len != -1 else -1
```
</details>
