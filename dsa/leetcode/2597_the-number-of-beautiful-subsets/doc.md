# The Number of Beautiful Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2597 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Backtracking, Sorting, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-number-of-beautiful-subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-number-of-beautiful-subsets/).

### Goal
Given an array of integers and a positive integer `k`, determine the total number of non-empty subsets of the array such that no two elements in the subset have an absolute difference exactly equal to `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the available elements.
- `k`: An integer representing the forbidden absolute difference.

**Return value**

- An integer representing the count of all valid non-empty subsets.

### Examples
**Example 1**

- Input: `nums = [2,4,6], k = 2`
- Output: `4`
- Explanation: The valid subsets are [2], [4], [6], [2, 6].

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `1`
- Explanation: The only valid subset is [1].

**Example 3**

- Input: `nums = [10,4,5,7,2,1], k = 3`
- Output: `23`

---

## Solution
### Approach
The problem is solved using Backtracking with pruning. By sorting the array, we can process elements and decide whether to include them in the current subset based on whether their inclusion violates the condition (i.e., if `x - k` is already present in the current subset). Alternatively, this can be modeled as a combinatorial problem by grouping numbers into chains based on their values modulo `k` and using dynamic programming to count valid combinations within each chain.

### Complexity Analysis
- **Time Complexity**: O(2^n) in the worst case for backtracking, where n is the length of the array. With optimization (grouping by modulo), it can be reduced to O(n log n) due to sorting.
- **Space Complexity**: O(n) to store the recursion stack and the frequency map of the current subset.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter, defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of beautiful subsets using a combinatorial approach.
    We group numbers by their remainder modulo k. Within each group,
    elements can only conflict if they are adjacent in the sorted sequence
    of that group (since they differ by exactly k).
    """
    # Count frequencies of each number
    counts = Counter(nums)

    # Group numbers by their remainder modulo k
    groups = defaultdict(list)
    for x in counts:
        groups[x % k].append(x)

    total_subsets = 1

    for rem in groups:
        # Sort numbers in the group to handle the difference k constraint
        group = sorted(groups[rem])

        # dp[i] stores the number of ways to form a subset using the first i elements
        # of the group such that no two elements have a difference of k.
        # If we don't include group[i]: ways = dp[i-1]
        # If we include group[i]: we can include it 2^count[group[i]] - 1 times.
        # If group[i] - group[i-1] == k, we cannot include group[i-1].

        n = len(group)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = group[i-1]
            take = (pow(2, counts[val]) - 1)

            if i > 1 and group[i-1] - group[i-2] == k:
                # Cannot pick both group[i-1] and group[i-2]
                dp[i] = dp[i-1] + dp[i-2] * take
            else:
                # Can pick group[i-1] freely with any valid subset of previous
                dp[i] = dp[i-1] * (take + 1)

        total_subsets *= dp[n]

    # Subtract 1 to exclude the empty subset
    return total_subsets - 1
```
</details>
