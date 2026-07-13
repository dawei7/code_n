# Check if Array is Good

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2784 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-array-is-good](https://leetcode.com/problems/check-if-array-is-good/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-array-is-good/).

### Goal
Determine if a given array of integers represents a "good" array. An array is considered good if it contains exactly one instance of every integer from 1 to $n-1$, and exactly two instances of the integer $n$, where $n$ is the maximum value present in the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array to be evaluated.

**Return value**

- `bool`: Returns `True` if the array satisfies the "good" criteria, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `False`

**Example 2**

- Input: `nums = [1, 3, 3, 2]`
- Output: `True`

**Example 3**

- Input: `nums = [1, 1]`
- Output: `True`

---

## Solution
### Approach
The problem can be solved by counting the frequency of each element. By identifying the maximum value $n$ in the array, we can verify the required counts: the frequency of $n$ must be exactly 2, and the frequency of every integer from 1 to $n-1$ must be exactly 1. Alternatively, sorting the array allows for a direct comparison against the expected sequence `[1, 2, ..., n-1, n, n]`.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$ if sorting is used, or $O(N)$ if using a frequency map (hash table or array), where $N$ is the length of the input array.
- **Space Complexity**: $O(N)$ to store the frequency counts or the sorted copy of the array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums: list[int]) -> bool:
    if not nums:
        return False

    n = max(nums)

    # A "good" array must have exactly n + 1 elements
    # (1 to n-1 once, and n twice)
    if len(nums) != n + 1:
        return False

    counts = Counter(nums)

    # Check for integers 1 to n-1
    for i in range(1, n):
        if counts[i] != 1:
            return False

    # Check for integer n
    if counts[n] != 2:
        return False

    return True
```
</details>
