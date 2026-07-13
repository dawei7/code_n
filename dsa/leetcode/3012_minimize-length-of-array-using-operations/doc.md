# Minimize Length of Array Using Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3012 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimize-length-of-array-using-operations](https://leetcode.com/problems/minimize-length-of-array-using-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimize-length-of-array-using-operations/).

### Goal
Given an array of integers, you can repeatedly select two elements $x$ and $y$ and replace them with $x \pmod y$. The objective is to minimize the final length of the array after performing any number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the minimum possible length of the array.

### Examples
**Example 1**

- Input: `nums = [1, 4, 3, 1]`
- Output: `1`

**Example 2**

- Input: `nums = [5, 5, 5, 10, 5]`
- Output: `2`

**Example 3**

- Input: `nums = [2, 3, 4]`
- Output: `1`

---

## Solution
### Approach
The problem relies on the properties of the modulo operator. If the minimum element $m$ in the array appears once, we can use it to reduce all other elements to values smaller than $m$, eventually reducing the array to length 1. If the minimum element $m$ appears $k$ times, we can reduce all elements not equal to $m$ to 0 (or values smaller than $m$), and then use the $m$ values to reduce each other. Specifically, if there exists an element $x$ in the array such that $x \pmod m \neq 0$, we can reduce the array to length 1. Otherwise, the result is $\lceil k/2 \rceil$.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we need to find the minimum element and its frequency.
- **Space Complexity**: $O(1)$, as we only store a few variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List
import math

def solve(nums: List[int]) -> int:
    """
    To minimize the array length:
    1. Find the minimum element 'm' and its frequency 'count'.
    2. If there exists any element 'x' in nums such that x % m != 0,
       we can use 'm' to reduce 'x' to 'x % m', which is smaller than 'm'.
       This allows us to eventually reduce the entire array to a single element.
    3. If all elements are divisible by 'm', we can only reduce the 'count'
       number of 'm's. Each operation on two 'm's results in 0 (since m % m == 0).
       We can pair up the 'm's to reduce them. The number of remaining elements
       will be ceil(count / 2).
    """
    min_val = min(nums)
    count = nums.count(min_val)

    # Check if there is any element not divisible by the minimum
    for x in nums:
        if x % min_val != 0:
            return 1

    # If all are divisible, we can reduce the count of min_val by half
    return (count + 1) // 2
```
</details>
