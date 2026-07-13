# Minimum Operations to Make Elements Within K Subarrays Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3505 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-make-elements-within-k-subarrays-equal](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/).

### Goal
Given an array of integers and an integer `k`, determine the minimum number of operations required to make all elements within every possible subarray of length `k` equal to the same value. An operation consists of incrementing or decrementing any element in the array by 1. Since every element must eventually belong to a subarray of length `k` where all elements are equal, this effectively implies that the entire array must be transformed into a sequence where every window of size `k` has identical elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the size of the sliding window.

**Return value**

- An integer representing the minimum total operations (sum of absolute differences) to satisfy the condition.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 2`
- Output: `2`
- Explanation: We can change the array to `[2, 2, 2]`. Operations: |1-2| + |3-2| = 2.

**Example 2**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `0`
- Explanation: The array already satisfies the condition.

**Example 3**

- Input: `nums = [1, 10, 1], k = 2`
- Output: `9`
- Explanation: We can change the array to `[1, 1, 1]`. Operations: |10-1| = 9.

---

## Solution
### Approach
The problem relies on the property that to minimize the sum of absolute differences $\sum |x_i - target|$, the optimal `target` is the **median** of the set of numbers. Since the constraint requires every window of size `k` to have equal elements, this implies that $nums[i] = nums[i+k]$ for all valid $i$. We can decompose the array into $k$ independent groups based on indices modulo $k$. For each group, we find the median and calculate the cost to transform all elements in that group to the median.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$, where $n$ is the length of the array, due to sorting each of the $k$ groups.
- **Space Complexity**: $O(n)$ to store the partitioned groups.

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left


class Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        index += 1
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def kth(self, target: int) -> int:
        index = 0
        bit = 1 << (len(self.tree).bit_length() - 1)
        while bit:
            nxt = index + bit
            if nxt < len(self.tree) and self.tree[nxt] < target:
                target -= self.tree[nxt]
                index = nxt
            bit //= 2
        return index


def solve(nums: list[int], x: int, k: int) -> int:
    n = len(nums)
    values = sorted(set(nums))
    compressed = [bisect_left(values, value) for value in nums]
    count_tree = Fenwick(len(values))
    sum_tree = Fenwick(len(values))
    window_cost = [0] * (n - x + 1)

    for right, (value, index) in enumerate(zip(nums, compressed)):
        count_tree.add(index, 1)
        sum_tree.add(index, value)
        if right >= x:
            old_index = compressed[right - x]
            old_value = nums[right - x]
            count_tree.add(old_index, -1)
            sum_tree.add(old_index, -old_value)
        if right >= x - 1:
            median_index = count_tree.kth((x + 1) // 2)
            median = values[median_index]
            left_count = count_tree.sum(median_index)
            left_sum = sum_tree.sum(median_index)
            total_sum = sum_tree.sum(len(values) - 1)
            right_count = x - left_count
            right_sum = total_sum - left_sum
            window_cost[right - x + 1] = (
                median * left_count - left_sum + right_sum - median * right_count
            )

    inf = 10**30
    previous = [0] * (n + 1)
    for chosen in range(1, k + 1):
        current = [inf] * (n + 1)
        for length in range(1, n + 1):
            current[length] = current[length - 1]
            if length >= x and previous[length - x] < inf:
                current[length] = min(
                    current[length],
                    previous[length - x] + window_cost[length - x],
                )
        previous = current
    return previous[n]
```
</details>
