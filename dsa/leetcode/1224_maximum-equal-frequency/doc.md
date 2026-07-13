# Maximum Equal Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1224 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-equal-frequency](https://leetcode.com/problems/maximum-equal-frequency/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-equal-frequency/).

### Goal
Find the longest prefix such that, after removing exactly one element from that prefix, every remaining distinct number appears the same number of times.

### Function Contract
**Inputs**

- `nums`: integer array.

**Return value**

The maximum valid prefix length.

### Examples
**Example 1**

- Input: `nums = [2,2,1,1,5,3,3,5]`
- Output: `7`

**Example 2**

- Input: `nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]`
- Output: `13`

**Example 3**

- Input: `nums = [1,1,1,2,2,2]`
- Output: `5`

---

## Solution
### Approach
Frequency counting with frequency-of-frequency invariants.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(nums):
    counts = Counter()
    freq = Counter()
    answer = 0
    max_freq = 0

    for i, value in enumerate(nums, 1):
        old = counts[value]
        if old:
            freq[old] -= 1
        counts[value] = old + 1
        freq[old + 1] += 1
        max_freq = max(max_freq, old + 1)

        if (
            max_freq == 1
            or max_freq * freq[max_freq] + 1 == i
            or (max_freq - 1) * (freq[max_freq - 1] + 1) + 1 == i
        ):
            answer = i
    return answer
```
</details>
