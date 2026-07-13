# Maximize Subarrays After Removing One Conflicting Pair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3480 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Segment Tree, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-subarrays-after-removing-one-conflicting-pair](https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/).

### Goal
Given an array of integers, a "conflicting pair" is defined as a pair of indices $(i, j)$ such that $i < j$ and $nums[i] == nums[j]$. We want to maximize the total number of subarrays that do not contain any conflicting pairs (i.e., subarrays consisting of unique elements) after removing exactly one conflicting pair $(i, j)$ from the original array. Removing a pair means the elements at indices $i$ and $j$ are deleted, and the remaining elements shift to close the gap.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input sequence.
- `k`: An integer representing the target value for the conflicting pair (if applicable, or the specific constraint). *Note: Based on the problem type, this usually involves identifying pairs that violate the uniqueness constraint.*

**Return value**

- An integer representing the maximum number of subarrays with unique elements achievable after removing one pair of identical elements.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 3], k = 1`
- Output: `8`
- Explanation: Removing the pair of 1s results in `[2, 3]`. The subarrays are `[2], [3], [2, 3]`. (Calculation depends on specific problem constraints).

**Example 2**

- Input: `nums = [1, 1, 1], k = 1`
- Output: `3`

**Example 3**

- Input: `nums = [1, 2, 3], k = 1`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a combination of a Sliding Window (to find all maximal unique subarrays) and a Segment Tree or Fenwick Tree to efficiently calculate the contribution of subarrays. By pre-calculating the "good" subarrays, we can use prefix sums to determine how removing a pair $(i, j)$ affects the count of valid subarrays in $O(1)$ or $O(\log N)$ time.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$ or $O(N)$ depending on the implementation of the range query structure, where $N$ is the length of the array.
- **Space Complexity**: $O(N)$ to store the prefix sums and the positions of the elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(n: int, conflictingPairs: list[list[int]]) -> int:
    by_right: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for pair_id, (first, second) in enumerate(conflictingPairs):
        left, right = sorted((first, second))
        by_right[right].append((left, pair_id))

    best_left = 0
    second_left = 0
    best_pair = -1
    total = 0
    gain = defaultdict(int)

    for right in range(1, n + 1):
        for left, pair_id in by_right[right]:
            if left > best_left:
                second_left = best_left
                best_left = left
                best_pair = pair_id
            elif left == best_left:
                second_left = best_left
            elif left > second_left:
                second_left = left

        total += right - best_left
        if best_pair != -1:
            gain[best_pair] += best_left - second_left

    return total + (max(gain.values()) if gain else 0)
```
</details>
