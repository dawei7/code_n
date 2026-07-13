# Minimum Number of Groups to Create a Valid Assignment

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2910 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-groups-to-create-a-valid-assignment](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/).

### Goal
Given an array of integers, partition all elements into groups such that each group contains only one type of integer. A valid assignment requires that for any two groups of the same integer type, the difference in their sizes is at most 1. The objective is to minimize the total number of groups formed.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the items to be grouped.

**Return value**

- An integer representing the minimum total number of groups possible under the given constraints.

### Examples
**Example 1**

- Input: `nums = [3,2,3,2,3]`
- Output: `2`
- Explanation: We can form two groups of 3s (size 3) and two groups of 2s (size 2). Total groups: 2.

**Example 2**

- Input: `nums = [10,10,10,3,1,1]`
- Output: `4`
- Explanation: We can group 10s into one group of 3, 3s into one group of 1, and 1s into one group of 2. Total groups: 4.

**Example 3**

- Input: `nums = [1,1,3,3,3,3,3,3]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a greedy approach combined with mathematical optimization. First, we count the frequency of each number. Let the minimum frequency be `min_f`. Any valid group size `k` must satisfy the condition that each frequency `f` can be partitioned into groups of size `k` and `k+1`. Specifically, `f = a*k + b*(k+1)` where `a+b` is the number of groups. We iterate through all possible group sizes `k` from `min_f` down to 1. For a fixed `k`, we check if every frequency can be validly partitioned. The first `k` that satisfies this for all frequencies yields the minimum number of groups.

### Complexity Analysis
- **Time Complexity**: O(N + M * sqrt(min_f)), where N is the number of elements and M is the number of unique elements. We iterate through possible group sizes up to the minimum frequency.
- **Space Complexity**: O(M) to store the frequency map of the elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter
import math

def solve(nums: list[int]) -> int:
    counts = Counter(nums)
    freqs = list(counts.values())
    min_f = min(freqs)

    def get_groups(f, k):
        # We want to represent f = a*k + b*(k+1)
        # This is equivalent to f = (a+b)*k + b
        # where 0 <= b <= a+b
        # Let n = a+b (total groups). Then f = n*k + b, where 0 <= b <= n
        # This implies n*k <= f <= n*(k+1)
        # n >= f / (k+1) and n <= f / k
        # So we need to find if there exists an integer n in [ceil(f/(k+1)), floor(f/k)]

        n_min = math.ceil(f / (k + 1))
        n_max = f // k

        if n_min <= n_max:
            return n_min
        return float('inf')

    # Try possible group sizes k starting from min_f down to 1
    for k in range(min_f, 0, -1):
        total_groups = 0
        possible = True
        for f in freqs:
            groups = get_groups(f, k)
            if groups == float('inf'):
                possible = False
                break
            total_groups += groups

        if possible:
            return total_groups

    return -1
```
</details>
