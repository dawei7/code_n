# Minimum Operations to Form Subsequence With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2835 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-form-subsequence-with-target-sum](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/).

### Goal
Given a list of powers of two (represented as integers) and a target integer, determine the minimum number of operations required to form the target sum using a subsequence of the given numbers. An operation consists of splitting a power of two (e.g., $2^i$) into two smaller powers of two ($2^{i-1} + 2^{i-1}$). If it is impossible to form the target, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers where each element is a power of two ($2^i$).
- `target`: An integer representing the desired sum.

**Return value**

- An integer representing the minimum number of split operations, or -1 if the target cannot be formed.

### Examples
**Example 1**

- Input: `nums = [1, 2, 8]`, `target = 7`
- Output: `1`

**Example 2**

- Input: `nums = [1, 32, 1, 2]`, `target = 12`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 4, 8]`, `target = 13`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using a Greedy approach combined with Bit Manipulation. First, check if the sum of all elements in `nums` is less than the `target`; if so, return -1. We maintain a frequency count of the available powers of two. We iterate through the bits of the `target` from least significant to most significant. If the $i$-th bit is set, we attempt to satisfy it using available powers of two. If we lack the exact power, we split larger powers into smaller ones. If we have an excess of smaller powers, we carry them over to higher bits.

### Complexity Analysis
- **Time Complexity**: $O(n + \log(\text{target}))$, where $n$ is the length of `nums`. We iterate through the array once to count frequencies and then iterate through the bits of the target (at most 32-64 bits).
- **Space Complexity**: $O(1)$ (or $O(\log(\max(\text{nums})))$), as the frequency array size is bounded by the number of possible powers of two (typically 32 or 64).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], target: int) -> int:
    if sum(nums) < target:
        return -1

    max_bit = max(max(nums).bit_length(), target.bit_length()) + 1
    counts = [0] * (max_bit + 1)
    for x in nums:
        counts[x.bit_length() - 1] += 1

    ops = 0

    for i in range(max_bit):
        if (target >> i) & 1:
            if counts[i] > 0:
                counts[i] -= 1
            else:
                j = i + 1
                while j < max_bit and counts[j] == 0:
                    j += 1
                if j == max_bit:
                    return -1

                while j > i:
                    counts[j] -= 1
                    counts[j - 1] += 2
                    ops += 1
                    j -= 1
                counts[i] -= 1

        counts[i + 1] += counts[i] // 2

    return ops
```
</details>
