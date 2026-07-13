# Ways to Split Array Into Good Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2750 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [ways-to-split-array-into-good-subarrays](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/).

### Goal
Given a binary array, determine the number of ways to partition it into contiguous subarrays such that each subarray contains exactly one '1'. If it is impossible to partition the array this way (e.g., the array contains no '1's), the result should be 0. Since the number of ways can be large, return the result modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers consisting only of 0s and 1s.

**Return value**

- An integer representing the total number of valid partitions modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [0,1,0,0,1]`
- Output: `3`

**Example 2**

- Input: `nums = [0,1,0]`
- Output: `1`

**Example 3**

- Input: `nums = [1]`
- Output: `1`

---

## Solution
### Approach
The problem can be solved using a combinatorial approach. If we identify the indices of all '1's in the array, any valid split must occur in the gaps between consecutive '1's. Specifically, if there are $k$ ones at indices $i_1, i_2, \dots, i_k$, there are $k-1$ gaps between them. For each gap between $i_j$ and $i_{j+1}$, the number of possible split points is equal to the number of zeros between these two ones plus one (the choice to split at any of the zero positions or not split at all). The total number of ways is the product of these choices.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we perform a single pass to identify the positions of the '1's.
- **Space Complexity**: $O(1)$ if we only track the previous index of '1', or $O(k)$ where $k$ is the number of '1's if we store their indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7

    # Find indices of all 1s
    ones_indices = [i for i, val in enumerate(nums) if val == 1]

    # If there are no 1s, it's impossible to have a subarray with exactly one 1
    if not ones_indices:
        return 0

    # If there is only one 1, there is exactly 1 way (the whole array)
    if len(ones_indices) == 1:
        return 1

    # The number of ways to split is the product of (number of zeros between consecutive 1s + 1)
    ans = 1
    for i in range(len(ones_indices) - 1):
        # The number of zeros between ones_indices[i] and ones_indices[i+1]
        # is (ones_indices[i+1] - ones_indices[i] - 1)
        # The number of ways to place a split is (zeros + 1)
        gap = ones_indices[i+1] - ones_indices[i]
        ans = (ans * gap) % MOD

    return ans
```
</details>
