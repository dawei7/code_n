# Maximum Size of a Set After Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3002 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-size-of-a-set-after-removals](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/).

### Goal
Given two integer arrays of equal length $n$, you must remove exactly $n/2$ elements from each array. The objective is to maximize the total number of unique elements present in the union of the two remaining sets.

### Function Contract
**Inputs**

- `nums1`: A list of integers of length $n$.
- `nums2`: A list of integers of length $n$.

**Return value**

- An integer representing the maximum possible size of the union of the two sets after removing $n/2$ elements from each.

### Examples
**Example 1**

- Input: `nums1 = [1,2,1,2]`, `nums2 = [1,1,1,1]`
- Output: `2`

**Example 2**

- Input: `nums1 = [1,2,3,4,5,6]`, `nums2 = [2,3,2,3,2,3]`
- Output: `5`

**Example 3**

- Input: `nums1 = [1,1,2,2,3,3]`, `nums2 = [4,4,5,5,6,6]`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a Greedy approach combined with Set theory. We first identify the unique elements in each array and the intersection of these sets. We prioritize keeping unique elements that are exclusive to one array, then fill the remaining removal quotas using the shared elements.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input arrays, due to the construction of sets and iterating through the elements.
- **Space Complexity**: $O(n)$ to store the unique elements of the arrays in sets.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1: list[int], nums2: list[int]) -> int:
    n = len(nums1)
    set1 = set(nums1)
    set2 = set(nums2)

    cap = n // 2
    common = len(set1 & set2)
    only1 = len(set1) - common
    only2 = len(set2) - common

    keep1 = min(only1, cap)
    keep2 = min(only2, cap)
    shared_capacity = (cap - keep1) + (cap - keep2)
    return keep1 + keep2 + min(common, shared_capacity)
```
</details>
