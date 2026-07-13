# Number of Pairs Satisfying Inequality

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2426 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-pairs-satisfying-inequality](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/).

### Goal
Given two integer arrays `nums1` and `nums2` of the same length and an integer `diff`, count the number of index pairs `(i, j)` such that `0 <= i < j < n` and the inequality `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff` holds true.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.
- `diff`: An integer representing the allowed tolerance.

**Return value**

- An integer representing the total count of valid pairs `(i, j)` that satisfy the given inequality.

### Examples
**Example 1**

- Input: `nums1 = [3, 2, 5], nums2 = [2, 2, 1], diff = 1`
- Output: `3`

**Example 2**

- Input: `nums1 = [3, -1], nums2 = [-2, 2], diff = -1`
- Output: `0`

---

## Solution
### Approach
The inequality `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff` can be rearranged to `(nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff`. By defining a new array `arr` where `arr[k] = nums1[k] - nums2[k]`, the problem reduces to finding pairs `(i, j)` such that `i < j` and `arr[i] - arr[j] <= diff`, or `arr[i] - diff <= arr[j]`. This is a classic variation of the "Count Inversions" problem, which can be solved efficiently using a modified Merge Sort or a Binary Indexed Tree (Fenwick Tree) with coordinate compression.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the input arrays. This is achieved by the divide-and-conquer approach of Merge Sort.
- **Space Complexity**: `O(n)` to store the auxiliary array used during the merge process.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums1: list[int], nums2: list[int], diff: int) -> int:
    # Transform the inequality:
    # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
    # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
    # Let arr[k] = nums1[k] - nums2[k]
    # arr[i] - arr[j] <= diff  =>  arr[i] - diff <= arr[j]

    arr = [n1 - n2 for n1, n2 in zip(nums1, nums2)]

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, count_l = merge_sort(arr[:mid])
        right, count_r = merge_sort(arr[mid:])

        count = count_l + count_r

        # Count pairs (i, j) where left[i] - diff <= right[j]
        # Since both halves are sorted, we use two pointers
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] - diff > right[j]:
                j += 1
            count += (len(right) - j)

        # Standard merge step
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    _, total_pairs = merge_sort(arr)
    return total_pairs
```
</details>
