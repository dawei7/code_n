# Maximum Number of Pairs in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2341 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-pairs-in-array](https://leetcode.com/problems/maximum-number-of-pairs-in-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-pairs-in-array/).

### Goal
Given an array of integers, determine the maximum number of pairs that can be formed by selecting two identical integers. After forming all possible pairs, count how many integers are left over. The final result should be an array containing these two counts: `[total_pairs, remaining_elements]`.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`). This list can contain positive, negative, or zero integers. Its length is between 1 and 100, and each element's value is between 0 and 100.

**Return value**

- A list of two integers (`List[int]`), where the first element is the total number of pairs formed, and the second element is the total number of remaining elements.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 1, 3, 2, 2]`
- Output: `[3, 1]`
  - Explanation:
    - Two `1`s form one pair.
    - Two `3`s form one pair.
    - Three `2`s form one pair, with one `2` remaining.
    - Total pairs: 1 + 1 + 1 = 3.
    - Total remaining: 1.

**Example 2**

- Input: `nums = [1, 1]`
- Output: `[1, 0]`
  - Explanation:
    - Two `1`s form one pair.
    - Total pairs: 1.
    - Total remaining: 0.

**Example 3**

- Input: `nums = [5]`
- Output: `[0, 1]`
  - Explanation:
    - No pairs can be formed.
    - Total pairs: 0.
    - Total remaining: 1.

---

## Solution
### Approach
The most straightforward approach involves counting the frequency of each unique number in the input array. Once the frequencies are known, for each distinct number:
1.  The number of pairs that can be formed from this specific number is its frequency divided by 2 (integer division).
2.  The number of elements of this specific type that are left over is its frequency modulo 2.

These individual counts for pairs and leftovers are then summed up across all distinct numbers to get the final total pairs and total leftovers. A hash map (or dictionary in Python) is an efficient data structure for storing and retrieving these frequencies.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of elements in the input array `nums`.
    - This is because we iterate through the array once to count the frequencies of all elements.
    - Subsequently, we iterate through the unique elements (at most `N` distinct elements) in the frequency map, which takes `O(D)` time, where `D` is the number of distinct elements. Since `D <= N`, the overall time complexity remains `O(N)`.
- **Space Complexity**: `O(D)`, where `D` is the number of distinct elements in the input array `nums`.
    - This space is used to store the frequencies of the unique elements in a hash map. In the worst-case scenario, all elements in `nums` are distinct, leading to a space complexity of `O(N)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
import collections
from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Calculates the maximum number of pairs that can be formed from identical integers
    in an array and the number of remaining elements.

    Args:
        nums: A list of integers.

    Returns:
        A list of two integers: [total_pairs, remaining_elements].
    """
    # Use collections.Counter to efficiently count frequencies of each number
    counts = collections.Counter(nums)

    total_pairs = 0
    total_leftovers = 0

    # Iterate through the frequencies of each unique number
    for count in counts.values():
        # For each number, calculate how many pairs can be formed
        total_pairs += count // 2
        # And how many elements of that number are left over
        total_leftovers += count % 2

    return [total_pairs, total_leftovers]
```
</details>
