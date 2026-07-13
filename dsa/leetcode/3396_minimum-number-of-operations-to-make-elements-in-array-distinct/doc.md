# Minimum Number of Operations to Make Elements in Array Distinct

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3396 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-operations-to-make-elements-in-array-distinct](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/).

### Goal
Given an array of integers, determine the minimum number of operations needed so the remaining array has all distinct elements. In one operation, remove the first three elements from the array; if fewer than three elements remain, remove all of them. The empty array is considered distinct.

### Function Contract
**Inputs**

- `nums`: A list of integers.

**Return value**

- An integer representing the minimum number of prefix-removal operations needed to make the remaining elements distinct.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 2, 1, 7]`
- Output: `2`
- Explanation:
  - Remove `[3, 2, 1]`, leaving `[2, 1, 7]`, which is distinct.

**Example 2**

- Input: `nums = [4, 5, 6, 4, 4]`
- Output: `2`
- Explanation:
  - Remove `[4, 5, 6]`, leaving `[4, 4]`.
  - Remove the remaining two elements, leaving an empty array.

**Example 3**

- Input: `nums = [6, 7, 8, 9]`
- Output: `0`
- Explanation: The array already contains distinct elements.

---

## Solution
### Approach
The core idea is to iterate through the array and, for each number, ensure it's unique. If a number is already present, we need to increment it until it becomes a unique value. A hash set (or a frequency map) is an efficient way to keep track of the numbers we've already encountered and assigned.

A greedy approach works here: sort the array first. Then, iterate through the sorted array. For each element `nums[i]`, if it's less than or equal to the previous element `nums[i-1]`, we must increment `nums[i]` to `nums[i-1] + 1`. The number of operations for this element will be `(nums[i-1] + 1) - nums[i]`. We then update `nums[i]` to this new value for subsequent comparisons.

Alternatively, without sorting, we can use a hash set to keep track of seen numbers. For each number `num` in the input array, we check if `num` is already in our `seen` set. If it is, we repeatedly increment `num` and add 1 to our total operations count until `num` is not in `seen`. Once `num` is unique, we add it to the `seen` set.

### Complexity Analysis
- **Time Complexity**: `O(N log N)` if sorting is used, where N is the number of elements in `nums`. If a hash set is used without sorting, in the worst case (e.g., `[0, 0, 0, ..., 0]`), each element might require multiple increments, leading to a potential `O(N^2)` complexity in the worst-case scenario for the hash set approach. However, if the range of numbers is limited or the distribution is not extremely skewed, the average case for the hash set approach can be closer to `O(N)`. The sorting approach is generally more predictable.
- **Space Complexity**: `O(1)` if sorting is done in-place and no auxiliary data structures are used beyond a few variables. If a hash set is used, the space complexity is `O(N)` in the worst case to store all unique elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    seen = set()

    for index in range(len(nums) - 1, -1, -1):
        if nums[index] in seen:
            return index // 3 + 1
        seen.add(nums[index])

    return 0
```
</details>
