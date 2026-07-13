# Count the Number of Good Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2537 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-the-number-of-good-subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-the-number-of-good-subarrays/).

### Goal
Given an integer array `nums` and an integer `k`, determine the total number of contiguous subarrays that qualify as "good." A subarray is defined as "good" if it contains at least `k` pairs of identical elements. A pair is defined as two indices `(i, j)` such that `i < j` and `nums[i] == nums[j]`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the minimum number of identical pairs required.

**Return value**

- An integer representing the total count of good subarrays.

### Examples
**Example 1**

- Input: `nums = [1,1,1,1,1], k = 10`
- Output: `1`
- Explanation: The only subarray with at least 10 pairs is the entire array itself.

**Example 2**

- Input: `nums = [3,1,4,3,2,2,4], k = 2`
- Output: `4`
- Explanation: The good subarrays are [3,1,4,3,2,2], [3,1,4,3,2,2,4], [1,4,3,2,2,4], and [4,3,2,2,4].

**Example 3**

- Input: `nums = [1,2,3], k = 1`
- Output: `0`
- Explanation: No subarray contains any identical pairs.

---

## Solution
### Approach
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (frequency dictionary). We maintain a window `[left, right]` and track the current number of pairs. When adding an element `x` that has appeared `n` times previously, we increment the pair count by `n`. When removing an element `x` that appears `n` times in the current window, we decrement the pair count by `n-1`. Since the number of pairs is monotonic with respect to the window size, we can efficiently count valid subarrays.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is added and removed from the window at most once.
- **Space Complexity**: `O(n)` in the worst case to store the frequency map of elements within the current window.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of good subarrays using a sliding window approach.
    A subarray is good if it has at least k pairs.
    """
    n = len(nums)
    count = 0
    left = 0
    current_pairs = 0
    freq = defaultdict(int)

    for right in range(n):
        # Add the current element to the window
        # If it appeared 'f' times before, it forms 'f' new pairs
        x = nums[right]
        current_pairs += freq[x]
        freq[x] += 1

        # While the window is valid (has at least k pairs),
        # all subarrays starting at 'left' and ending at 'right' or further
        # are also valid.
        while current_pairs >= k:
            # All subarrays from [left, right], [left, right+1]...[left, n-1] are good
            count += (n - right)

            # Shrink the window from the left
            left_val = nums[left]
            freq[left_val] -= 1
            # Removing an element that appeared 'f' times removes 'f-1' pairs
            current_pairs -= freq[left_val]
            left += 1

    return count
```
</details>
