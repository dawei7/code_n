# Sum of Imbalance Numbers of All Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2763 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-imbalance-numbers-of-all-subarrays](https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/).

### Goal
Calculate the total "imbalance number" across every possible contiguous subarray of a given integer array. The imbalance number of a sequence is defined as the count of elements `x` such that `x + 1` is not present in the sequence, excluding the minimum element of that sequence.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 ≤ nums[i] ≤ n.

**Return value**

- An integer representing the sum of imbalance numbers for all contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [2, 3, 1]`
- Output: `0`
- Explanation: Subarrays are [2], [3], [1], [2,3], [3,1], [2,3,1]. All have an imbalance of 0.

**Example 2**

- Input: `nums = [1, 3, 3]`
- Output: `1`
- Explanation: The subarray [1, 3] has an imbalance of 1 because 2 is missing.

**Example 3**

- Input: `nums = [4, 5, 6, 1, 2]`
- Output: `3`

---

## Solution
### Approach
The problem is solved by iterating through all possible starting positions `i` of a subarray and expanding to the right `j`. As we expand, we maintain a set of seen numbers to track the imbalance. Specifically, when adding a number `x`, we check if `x-1` and `x+1` are already in the set to update the imbalance count dynamically.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the input array, as we iterate through all subarrays.
- **Space Complexity**: `O(n)` to store the set of elements present in the current subarray.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    """
    Calculates the sum of imbalance numbers of all subarrays.
    An imbalance number is the count of elements x in a subarray such that
    x + 1 is not present in the subarray, excluding the minimum element.
    """
    n = len(nums)
    total_imbalance = 0

    for i in range(n):
        seen = set()
        current_imbalance = 0
        for j in range(i, n):
            x = nums[j]

            if x not in seen:
                # If x-1 and x+1 are both present, adding x reduces imbalance by 1
                # because x+1 is no longer "missing" its predecessor.
                if (x - 1) in seen and (x + 1) in seen:
                    current_imbalance -= 1
                # If neither x-1 nor x+1 are present, adding x increases imbalance by 1
                # (unless it's the new minimum, but the logic handles this via the set).
                elif (x - 1) not in seen and (x + 1) not in seen:
                    if seen: # Only increment if not the very first element
                        current_imbalance += 1

                seen.add(x)

            total_imbalance += current_imbalance

    return total_imbalance
```
</details>
