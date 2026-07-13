# Sum of Digit Differences of All Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3153 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-digit-differences-of-all-pairs](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/).

### Goal
Given an array of integers of equal length (when represented as strings), calculate the total sum of digit differences across all possible pairs of numbers in the array. A "digit difference" for a pair is defined as the count of positions where the digits at that position differ.

### Function Contract
**Inputs**

- `nums`: A list of integers where every integer has the same number of digits.

**Return value**

- An integer representing the sum of digit differences for all unique pairs $(i, j)$ where $0 \le i < j < n$.

### Examples
**Example 1**

- Input: `nums = [13, 23, 12]`
- Output: `4`
- Explanation:
  - (13, 23): diff at index 0 (1 vs 2) = 1
  - (13, 12): diff at index 1 (3 vs 2) = 1
  - (23, 12): diff at index 0 (2 vs 1), index 1 (3 vs 2) = 2
  - Total = 1 + 1 + 2 = 4.

**Example 2**

- Input: `nums = [10, 10, 10, 10]`
- Output: `0`
- Explanation: All pairs are identical, so there are no digit differences.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using **Combinatorial Counting**. Instead of iterating through all $O(n^2)$ pairs, we observe that the total sum is the sum of differences at each digit position independently. For a specific position, if we have counts of each digit (0-9), the number of pairs that *do not* differ is the sum of $\binom{count[d]}{2}$ for all digits $d \in [0, 9]$. The number of pairs that *do* differ is the total number of pairs $\binom{n}{2}$ minus the number of pairs that match.

### Complexity Analysis
- **Time Complexity**: $O(n \cdot d)$, where $n$ is the number of elements in `nums` and $d$ is the number of digits in each integer. We iterate through each number once to populate the frequency counts.
- **Space Complexity**: $O(d)$, as we maintain a frequency table of size $10 \times d$ to store the counts of each digit at each position.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    # Convert numbers to strings to easily access digits by position
    s_nums = [str(num) for num in nums]
    num_digits = len(s_nums[0])

    total_diff = 0

    # For each digit position, count occurrences of each digit (0-9)
    for pos in range(num_digits):
        counts = [0] * 10
        for s in s_nums:
            digit = int(s[pos])
            counts[digit] += 1

        # Total pairs at this position is n * (n - 1) // 2
        # Pairs that match are sum of (count * (count - 1) // 2) for each digit
        # Pairs that differ = Total pairs - Matching pairs
        total_pairs = n * (n - 1) // 2
        matching_pairs = 0
        for c in counts:
            if c > 1:
                matching_pairs += (c * (c - 1)) // 2

        total_diff += (total_pairs - matching_pairs)

    return total_diff
```
</details>
