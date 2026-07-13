# Find X-Sum of All K-Long Subarrays II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3321 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-x-sum-of-all-k-long-subarrays-ii](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/).

### Goal
Given an array of integers, calculate the "X-Sum" for every contiguous subarray of length `k`. The X-Sum is defined as the sum of the `x` most frequent elements in the subarray. If two elements have the same frequency, the larger element is prioritized. If there are fewer than `x` distinct elements in the subarray, the X-Sum is simply the sum of all elements in the subarray.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the length of the sliding window.
- `x`: An integer representing the number of top frequent elements to sum.

**Return value**

- A list of integers representing the X-Sum for each sliding window of size `k`.

### Examples
**Example 1**

- Input: `nums = [1,1,2,2,3,4,2,3], k = 6, x = 2`
- Output: `[6, 10, 12]`

**Example 2**

- Input: `nums = [3,8,7,8,7,5], k = 2, x = 2`
- Output: `[11, 15, 15, 15, 12]`

**Example 3**

- Input: `nums = [1,1,1,1], k = 2, x = 1`
- Output: `[2, 2, 2]`

---

## Solution
### Approach
The problem is solved using a sliding window approach combined with two balanced binary search trees (or two sorted sets) to maintain the top `x` frequent elements. We track the frequency of each number using a hash map. The two sets partition the elements into "top `x`" and "others," allowing us to efficiently update the X-Sum as the window slides by moving elements between sets and maintaining the sum of the top `x` group.

### Complexity Analysis
- **Time Complexity**: `O(n log k)`, where `n` is the length of `nums`. Each insertion and deletion in the sorted sets takes `O(log k)` time.
- **Space Complexity**: `O(n)`, required to store the frequency map and the elements within the sliding window sets.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict
from heapq import heappop, heappush


def solve(nums: list[int], k: int, x: int) -> list[int]:
    freq = defaultdict(int)
    top = set()
    rest = set()
    top_min = []
    rest_max = []
    current_sum = 0

    def key(value: int) -> tuple[int, int]:
        return freq[value], value

    def push_top(value: int) -> None:
        heappush(top_min, key(value))

    def push_rest(value: int) -> None:
        f, v = key(value)
        heappush(rest_max, (-f, -v))

    def clean_top() -> None:
        while top_min:
            f, value = top_min[0]
            if value in top and freq[value] == f:
                return
            heappop(top_min)

    def clean_rest() -> None:
        while rest_max:
            nf, nv = rest_max[0]
            value = -nv
            if value in rest and freq[value] == -nf:
                return
            heappop(rest_max)

    def remove_current(value: int) -> None:
        nonlocal current_sum
        if value in top:
            top.remove(value)
            current_sum -= freq[value] * value
        elif value in rest:
            rest.remove(value)

    def move_rest_to_top() -> None:
        nonlocal current_sum
        clean_rest()
        nf, nv = heappop(rest_max)
        value = -nv
        rest.remove(value)
        top.add(value)
        current_sum += -nf * value
        push_top(value)

    def move_top_to_rest() -> None:
        nonlocal current_sum
        clean_top()
        f, value = heappop(top_min)
        top.remove(value)
        current_sum -= f * value
        rest.add(value)
        push_rest(value)

    def rebalance() -> None:
        while len(top) < x and rest:
            move_rest_to_top()
        while len(top) > x:
            move_top_to_rest()

        while top and rest:
            clean_top()
            clean_rest()
            top_key = top_min[0]
            rest_key = (-rest_max[0][0], -rest_max[0][1])
            if rest_key <= top_key:
                break
            move_top_to_rest()
            move_rest_to_top()

    def add(value: int) -> None:
        remove_current(value)
        freq[value] += 1
        rest.add(value)
        push_rest(value)
        rebalance()

    def remove(value: int) -> None:
        remove_current(value)
        freq[value] -= 1
        if freq[value] > 0:
            rest.add(value)
            push_rest(value)
        else:
            del freq[value]
        rebalance()

    result = []
    for i, value in enumerate(nums):
        add(value)
        if i >= k:
            remove(nums[i - k])
        if i >= k - 1:
            result.append(current_sum)

    return result
```
</details>
