# Find the Length of the Longest Common Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3043 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-length-of-the-longest-common-prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/).

### Goal
Given two arrays of positive integers, identify the length of the longest prefix shared by any integer from the first array and any integer from the second array. A prefix is defined as the leading sequence of digits of an integer.

### Function Contract
**Inputs**

- `arr1`: A list of positive integers.
- `arr2`: A list of positive integers.

**Return value**

- An integer representing the maximum length of a common prefix found between any pair of numbers $(x, y)$ where $x \in arr1$ and $y \in arr2$. If no common prefix exists, return 0.

### Examples
**Example 1**

- Input: `arr1 = [1, 10, 100], arr2 = [1000]`
- Output: `3`
- Explanation: The longest common prefix is "100", which has length 3.

**Example 2**

- Input: `arr1 = [1, 2, 3], arr2 = [4, 5, 6]`
- Output: `0`
- Explanation: No common prefixes exist.

**Example 3**

- Input: `arr1 = [12, 34, 56], arr2 = [123, 456]`
- Output: `2`
- Explanation: The longest common prefix is "12", which has length 2.

---

## Solution
### Approach
The problem is efficiently solved using a **Hash Set** to store all possible prefixes of numbers in the first array. By iterating through each number in `arr1` and generating all its prefixes, we can perform $O(1)$ lookups. We then iterate through `arr2`, generate its prefixes, and check for existence in the set to find the maximum length.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot L + M \cdot L)$, where $N$ and $M$ are the lengths of `arr1` and `arr2` respectively, and $L$ is the maximum number of digits in an integer (at most 10).
- **Space Complexity**: $O(N \cdot L)$ to store the prefixes of all numbers in `arr1` in the hash set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(arr1: List[int], arr2: List[int]) -> int:
    """
    Finds the length of the longest common prefix between any two numbers
    from arr1 and arr2 using a hash set for prefix storage.
    """
    prefix_set = set()

    # Store all possible prefixes of numbers in arr1
    for num in arr1:
        s = str(num)
        current_prefix = ""
        for char in s:
            current_prefix += char
            prefix_set.add(current_prefix)

    max_len = 0

    # Check prefixes of numbers in arr2 against the set
    for num in arr2:
        s = str(num)
        current_prefix = ""
        for char in s:
            current_prefix += char
            if current_prefix in prefix_set:
                max_len = max(max_len, len(current_prefix))
            else:
                # If the current prefix isn't in the set, longer ones won't be either
                break

    return max_len
```
</details>
