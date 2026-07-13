# Count Almost Equal Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3267 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-almost-equal-pairs-ii](https://leetcode.com/problems/count-almost-equal-pairs-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-almost-equal-pairs-ii/).

### Goal
Given an array of integers, determine the number of pairs `(i, j)` such that `i < j` and the two numbers can be made equal by performing at most two "swap" operations on the digits of one of the numbers. A swap operation involves choosing two indices in the string representation of the number and swapping the digits at those positions.

### Function Contract
**Inputs**

- `nums`: A list of integers where each integer is between 1 and 1,000,000.

**Return value**

- An integer representing the total count of pairs `(i, j)` that satisfy the "almost equal" condition.

### Examples
**Example 1**

- Input: `nums = [1023, 2310]`
- Output: `1`
- Explanation: 1023 can become 2310 by swapping '1' with '2' and '0' with '3'.

**Example 2**

- Input: `nums = [1, 10, 30]`
- Output: `3`
- Explanation: (1, 10), (1, 30), and (10, 30) are all valid pairs after padding with leading zeros.

**Example 3**

- Input: `nums = [12, 12]`
- Output: `1`

---

## Solution
### Approach
The problem is solved by normalizing all numbers to the same string length (padding with leading zeros) and using a Hash Map to store the frequency of numbers encountered so far. For each number, we generate all possible variations reachable within two swaps. Since the maximum number of digits is 7, the number of permutations is small enough to generate efficiently. We use a set to store unique variations to avoid double-counting when checking against the frequency map.

### Complexity Analysis
- **Time Complexity**: `O(N * D^4)`, where `N` is the length of the input array and `D` is the maximum number of digits (7). Generating all variations within 2 swaps involves choosing 2 pairs of indices, which is roughly `O(D^4)`.
- **Space Complexity**: `O(N * D^4)` to store the frequency map of all possible variations for each number.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int]) -> int:
    # Normalize all numbers to the same length (max 7 digits)
    max_len = len(str(max(nums)))

    def get_variations(n_str):
        s = list(n_str.zfill(max_len))
        res = {tuple(s)}

        # 1 swap
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]
                res.add(tuple(s))
                # 2 swaps: perform another swap on the result of the first
                for k in range(n):
                    for l in range(k + 1, n):
                        s[k], s[l] = s[l], s[k]
                        res.add(tuple(s))
                        s[k], s[l] = s[l], s[k] # backtrack
                s[i], s[j] = s[j], s[i] # backtrack
        return res

    count = 0
    freq = defaultdict(int)

    for x in nums:
        s_x = str(x).zfill(max_len)
        variations = get_variations(s_x)

        # For each variation, check how many times we've seen it before
        for var in variations:
            count += freq[var]

        # Add the original number to the frequency map
        freq[tuple(s_x)] += 1

    return count
```
</details>
