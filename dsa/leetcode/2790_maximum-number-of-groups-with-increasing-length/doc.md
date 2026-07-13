# Maximum Number of Groups With Increasing Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2790 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-groups-with-increasing-length](https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/).

### Goal
Given a collection of items with various counts, determine the maximum number of groups you can form such that each group has a strictly greater length than the previous one. Each group must consist of distinct items (i.e., you cannot use the same item more than once within a single group).

### Function Contract
**Inputs**

- `usageLimits`: A list of integers where `usageLimits[i]` represents the total number of times the $i$-th item can be used across all groups.

**Return value**

- An integer representing the maximum number of groups that can be formed.

### Examples
**Example 1**

- Input: `usageLimits = [1, 2, 5]`
- Output: `3`
- Explanation: We can form groups of sizes 1, 2, and 3.

**Example 2**

- Input: `usageLimits = [2, 1, 2, 1]`
- Output: `2`
- Explanation: We can form groups of sizes 1 and 2.

**Example 3**

- Input: `usageLimits = [1, 1]`
- Output: `1`
- Explanation: We can only form one group of size 1.

---

## Solution
### Approach
The problem is solved using a **Greedy approach combined with Sorting**. By sorting the `usageLimits` in non-decreasing order, we can greedily attempt to build groups of increasing size. We maintain a running count of available items and compare it against the required number of items needed to form the next group of size $k$. If the total number of items accumulated so far is sufficient to satisfy the requirement for a group of size $k$, we increment our group count.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the length of `usageLimits`, primarily due to the sorting step. The subsequent linear scan is $O(N)$.
- **Space Complexity**: $O(1)$ or $O(N)$ depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(usageLimits: list[int]) -> int:
    """
    Calculates the maximum number of groups with strictly increasing lengths.

    The strategy is to sort the limits and greedily build groups.
    If we want to form 'k' groups, the smallest possible sizes are 1, 2, ..., k.
    The total number of items required is k*(k+1)/2.
    However, because we have constraints on individual item counts, we sort
    the limits and keep track of how many items we have 'accumulated' to
    satisfy the increasing group size requirements.
    """
    usageLimits.sort()

    groups = 0
    total_items_accumulated = 0

    for limit in usageLimits:
        # If the current item's limit allows us to increase the size of the
        # next group (which would be groups + 1), we increment the group count.
        # We track total_items_accumulated to ensure we have enough items
        # to satisfy the requirement of having strictly increasing sizes.
        total_items_accumulated += limit
        if total_items_accumulated >= (groups + 1):
            groups += 1
            total_items_accumulated -= groups

    return groups
```
</details>
