# Count Number of Bad Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2364 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-number-of-bad-pairs](https://leetcode.com/problems/count-number-of-bad-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-number-of-bad-pairs/).

### Goal
Given a 0-indexed integer array `nums`, determine the total number of "bad pairs" `(i, j)` such that `0 <= i < j < nums.length` and `j - i != nums[j] - nums[i]`.

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of integers.

**Return value**

- `int` - The total number of bad pairs in the array.

### Examples
**Example 1**

- Input: `nums = [4, 1, 3, 3]`
- Output: `5`
- Explanation:
  - The total number of pairs is `(4 * 3) / 2 = 6`.
  - The pair `(1, 3)` is a good pair because `3 - 1 == nums[3] - nums[1]` (which simplifies to `2 == 3 - 1`).
  - The other 5 pairs are bad pairs. Thus, we return `5`.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `0`
- Explanation:
  - Every pair `(i, j)` satisfies `j - i == nums[j] - nums[i]`.
  - There are no bad pairs, so we return `0`.

---

## Solution
### Approach
The problem asks us to count pairs where `j - i != nums[j] - nums[i]`. Directly checking all pairs would require $O(N^2)$ time, which is too slow for large arrays.

We can optimize this by rewriting the condition for a **good pair**:
$$j - i = nums[j] - nums[i]$$

Rearranging the terms to group index-specific variables together:
$$nums[i] - i = nums[j] - j$$

Let $diff[k] = nums[k] - k$. A pair $(i, j)$ is good if and only if $diff[i] == diff[j]$.

Using this insight, we can count the number of **good pairs** and subtract them from the **total possible pairs** to find the number of bad pairs:
1. **Total Pairs**: For an array of length $N$, the total number of pairs $(i, j)$ with $i < j$ is given by the combination formula:
   $$\text{Total Pairs} = \frac{N \times (N - 1)}{2}$$
2. **Good Pairs**: We can iterate through the array and maintain a frequency map of the differences $nums[i] - i$. For each element, the number of previous elements with the same difference tells us how many new good pairs can be formed.
3. **Bad Pairs**: Finally, the result is $\text{Total Pairs} - \text{Good Pairs}$.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the length of the array `nums`. We traverse the array exactly once, performing constant-time $O(1)$ lookups and updates in our hash map.
- **Space Complexity**: $\mathcal{O}(N)$ in the worst case, as we may store up to $N$ unique differences in our hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    n = len(nums)
    total_pairs = n * (n - 1) // 2
    good_pairs = 0
    diff_counts = {}

    for i, num in enumerate(nums):
        diff = num - i
        if diff in diff_counts:
            good_pairs += diff_counts[diff]
            diff_counts[diff] += 1
        else:
            diff_counts[diff] = 1

    return total_pairs - good_pairs
```
</details>
