# Count of Interesting Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2845 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-of-interesting-subarrays](https://leetcode.com/problems/count-of-interesting-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-of-interesting-subarrays/).

### Goal
Given an array of integers, identify the total number of contiguous subarrays where the count of elements satisfying a specific condition (being congruent to `k` modulo `m`) results in a value that is also congruent to `k` modulo `m`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `modulo`: An integer `m`.
- `k`: An integer `k`.

**Return value**

- An integer representing the total count of "interesting" subarrays.

### Examples
**Example 1**

- Input: `nums = [3, 2, 4], modulo = 2, k = 1`
- Output: `3`
- Explanation: The interesting subarrays are [3], [3, 2], and [3, 2, 4].

**Example 2**

- Input: `nums = [3, 1, 9, 6], modulo = 3, k = 0`
- Output: `2`
- Explanation: The interesting subarrays are [3] and [9].

**Example 3**

- Input: `nums = [11, 12, 21, 14], modulo = 10, k = 1`
- Output: `1`
- Explanation: The interesting subarray is [11].

---

## Solution
### Approach
The problem is solved using the **Prefix Sum** technique combined with a **Hash Map (Frequency Table)**. By transforming the array into a binary sequence where an element is `1` if `nums[i] % modulo == k` and `0` otherwise, the problem reduces to finding subarrays whose sum `S` satisfies `S % modulo == k`. We maintain a running prefix sum and store the frequency of each `(prefix_sum % modulo)` encountered so far to calculate the number of valid subarrays ending at the current index in constant time.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(min(n, modulo))`, as the hash map stores at most `modulo` distinct remainders.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], modulo: int, k: int) -> int:
    """
    Counts the number of subarrays where the count of elements
    satisfying (x % modulo == k) is congruent to k (mod modulo).
    """
    # count_map stores the frequency of (prefix_sum % modulo)
    # Initialize with 0: 1 to handle subarrays starting from index 0
    count_map = defaultdict(int)
    count_map[0] = 1

    current_prefix_sum = 0
    total_interesting_subarrays = 0

    for x in nums:
        # Check if the current element satisfies the condition
        if x % modulo == k:
            current_prefix_sum += 1

        # We need: (current_prefix_sum - previous_prefix_sum) % modulo == k
        # This rearranges to: previous_prefix_sum % modulo == (current_prefix_sum - k) % modulo
        target = (current_prefix_sum - k) % modulo

        if target in count_map:
            total_interesting_subarrays += count_map[target]

        # Update the map with the current prefix sum remainder
        count_map[current_prefix_sum % modulo] += 1

    return total_interesting_subarrays
```
</details>
