# Count Special Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3404 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-special-subsequences](https://leetcode.com/problems/count-special-subsequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-special-subsequences/).

### Goal
Given an array `nums` consisting of integers `0`, `1`, and `2`, count the number of "special" subsequences. A special subsequence is defined as one that starts with one or more `0`s, followed by one or more `1`s, and finally followed by one or more `2`s. The order of elements within the subsequence must strictly adhere to this pattern. Since the number of subsequences can be very large, return the count modulo `10^9 + 7`.

### Function Contract
**Inputs**

- `nums`: A list of integers, where each integer is either `0`, `1`, or `2`.

**Return value**

- An integer representing the total count of special subsequences modulo `10^9 + 7`.

### Examples
**Example 1**

- Input: `nums = [0,1,2,2]`
- Output: `3`
- Explanation: The special subsequences are `[0,1,2]`, `[0,1,2]`, and `[0,1,2,2]`. Note that the two `[0,1,2]` subsequences are distinct because they are formed from different indices of the original array.

**Example 2**

- Input: `nums = [2,1,0]`
- Output: `0`
- Explanation: No special subsequences can be formed.

**Example 3**

- Input: `nums = [0,0,1,1,2,2]`
- Output: `12`
- Explanation: The special subsequences are formed by choosing one or more 0s, then one or more 1s, then one or more 2s. For instance, choosing the first 0, first 1, and first 2 gives `[0,1,2]`. Choosing the first 0, first 1, and second 2 gives another `[0,1,2]`.

---

## Solution
### Approach
This problem can be solved using dynamic programming. We can maintain counts of subsequences ending with `0`, `1`, and `2` as we iterate through the input array.

Let:
- `count0` be the number of subsequences ending with `0`.
- `count1` be the number of subsequences ending with `1`.
- `count2` be the number of subsequences ending with `2`.

When we encounter a `0`:
- A new subsequence ending in `0` can be formed by appending this `0` to existing subsequences ending in `0`.
- Additionally, this `0` itself can start a new subsequence.
- So, `new_count0 = count0 (existing) + count0 (append to existing) + 1 (new single 0)`. This simplifies to `new_count0 = 2 * count0 + 1`.

When we encounter a `1`:
- A new subsequence ending in `1` can be formed by appending this `1` to existing subsequences ending in `0` (forming `0...01`).
- It can also be formed by appending this `1` to existing subsequences ending in `1` (forming `0...01...1`).
- So, `new_count1 = count1 (existing) + count0 (append to 0s) + count1 (append to 1s)`. This simplifies to `new_count1 = count0 + 2 * count1`.

When we encounter a `2`:
- A new subsequence ending in `2` can be formed by appending this `2` to existing subsequences ending in `1` (forming `0...01...12`).
- It can also be formed by appending this `2` to existing subsequences ending in `2` (forming `0...01...12...2`).
- So, `new_count2 = count2 (existing) + count1 (append to 1s) + count2 (append to 2s)`. This simplifies to `new_count2 = count1 + 2 * count2`.

We need to perform all calculations modulo `10^9 + 7`.

### Complexity Analysis
- **Time Complexity**: O(N), where N is the length of the input array `nums`. We iterate through the array once.
- **Space Complexity**: O(1), as we only use a few variables to store the counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict
from math import gcd


def solve(nums):
    n = len(nums)
    pair_ratios = defaultdict(int)
    answer = 0

    for r in range(4, n - 2):
        q = r - 2
        for p in range(q - 1):
            divisor = gcd(nums[p], nums[q])
            pair_ratios[(nums[p] // divisor, nums[q] // divisor)] += 1

        for s in range(r + 2, n):
            divisor = gcd(nums[s], nums[r])
            answer += pair_ratios[(nums[s] // divisor, nums[r] // divisor)]

    return answer
```
</details>
