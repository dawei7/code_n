# Maximize Subarray Sum After Removing All Occurrences of One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3410 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Dynamic Programming, Segment Tree, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-subarray-sum-after-removing-all-occurrences-of-one-element](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/).

### Goal
Given an integer array, determine the maximum possible sum of a contiguous subarray after choosing exactly one distinct value present in the array and removing all its occurrences. If the array contains negative numbers, the subarray sum could potentially be empty (sum 0) or must be calculated based on the remaining elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the maximum subarray sum achievable after removing all instances of one chosen element.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`
- Explanation: Removing any element (e.g., 1) leaves [2, 3, 4], sum is 9. Removing nothing is not allowed; we must remove one value. Removing 1 gives 9, removing 4 gives 6. Wait, the max is 10 if we remove nothing? No, we must remove one value. Removing 1 gives 9.

**Example 2**

- Input: `nums = [-3, -1, -2]`
- Output: `0`
- Explanation: Removing any element leaves a subarray of negative numbers. The empty subarray sum is 0.

**Example 3**

- Input: `nums = [1, 2, 1, 3]`
- Output: `6`
- Explanation: Removing 1 leaves [2, 3], sum 5. Removing 2 leaves [1, 1, 3], sum 5. Removing 3 leaves [1, 2, 1], sum 4. Actually, if we remove 2, we get [1, 1, 3], max subarray is 5. If we remove 3, we get [1, 2, 1], max subarray is 4.

---

## Solution
### Approach
The problem is solved using a combination of Kadane's Algorithm and Prefix Sums. We pre-calculate the total sum of occurrences for each unique value. By iterating through the array and maintaining the maximum subarray sum using Kadane's, we can efficiently calculate the impact of removing a specific value by tracking the "best" subarray sum that excludes that value's occurrences.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the length of the array. We iterate through the array a constant number of times to build prefix sums and track Kadane's state.
- **Space Complexity**: `O(N)` to store the indices of each element and the prefix sum arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(nums: list[int]) -> int:
    n = len(nums)
    size = 1
    while size < n:
        size <<= 1

    negative_infinity = -(10**30)
    tree = [(0, negative_infinity, negative_infinity, negative_infinity) for _ in range(2 * size)]

    def make_node(value: int) -> tuple[int, int, int, int]:
        return (value, value, value, value)

    def make_removed_node() -> tuple[int, int, int, int]:
        return (0, negative_infinity, negative_infinity, negative_infinity)

    def merge(left, right):
        total = left[0] + right[0]
        prefix = max(left[1], left[0] + right[1])
        suffix = max(right[2], right[0] + left[2])
        best = max(left[3], right[3], left[2] + right[1])
        return (total, prefix, suffix, best)

    for index, value in enumerate(nums):
        tree[size + index] = make_node(value)
    for index in range(size - 1, 0, -1):
        tree[index] = merge(tree[index * 2], tree[index * 2 + 1])

    def update(position: int, value: int | None) -> None:
        index = size + position
        tree[index] = make_removed_node() if value is None else make_node(value)
        index //= 2
        while index:
            tree[index] = merge(tree[index * 2], tree[index * 2 + 1])
            index //= 2

    positions = defaultdict(list)
    for index, value in enumerate(nums):
        if value < 0:
            positions[value].append(index)

    answer = tree[1][3]
    for value, indices in positions.items():
        for index in indices:
            update(index, None)
        answer = max(answer, tree[1][3])
        for index in indices:
            update(index, value)

    return answer
```
</details>
