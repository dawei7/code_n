# Find the Median of the Uniqueness Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3134 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-median-of-the-uniqueness-array](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/).

### Goal
Given an integer array, consider all possible contiguous subarrays. For each subarray, calculate the number of distinct elements it contains. The "uniqueness array" is the collection of these distinct counts for every possible subarray, sorted in non-decreasing order. The goal is to find the median value of this uniqueness array. If the total number of subarrays is $N$, the median is the element at index $\lceil N/2 \rceil - 1$ (0-indexed).

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the median value of the uniqueness array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `1`
- Explanation: Subarrays are [1], [2], [3], [1,2], [2,3], [1,2,3]. Distinct counts: 1, 1, 1, 2, 2, 3. Sorted: [1, 1, 1, 2, 2, 3]. Median is at index (6+1)//2 - 1 = 2, which is 1.

**Example 2**

- Input: `nums = [3, 4, 3, 3]`
- Output: `2`

**Example 3**

- Input: `nums = [73, 33, 9]`
- Output: `2`

---

## Solution
### Approach
The problem is solved using a combination of **Binary Search on the Answer** and a **Sliding Window** technique. Since the uniqueness array is monotonic in nature (the count of distinct elements is non-decreasing as we expand subarrays), we can binary search for the smallest value $k$ such that at least $\lceil N/2 \rceil$ subarrays have $\le k$ distinct elements. The sliding window efficiently counts how many subarrays have at most $k$ distinct elements in $O(n)$ time.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the array. The binary search runs in $O(\log n)$ iterations, and each check using the sliding window takes $O(n)$.
- **Space Complexity**: $O(n)$ to store the frequency map used in the sliding window.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int]) -> int:
    n = len(nums)
    total_subarrays = n * (n + 1) // 2
    target = (total_subarrays + 1) // 2

    def count_subarrays_with_at_most_k_distinct(k: int) -> int:
        """Counts how many subarrays have at most k distinct elements."""
        count = 0
        left = 0
        freq = defaultdict(int)
        distinct = 0

        for right in range(n):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1

            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1

            # All subarrays ending at 'right' starting from 'left' to 'right'
            # have at most k distinct elements.
            count += (right - left + 1)
        return count

    # Binary search for the smallest k such that count_subarrays(k) >= target
    low = 1
    high = len(set(nums))
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if count_subarrays_with_at_most_k_distinct(mid) >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```
</details>
