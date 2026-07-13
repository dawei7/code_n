# Maximum Beauty of an Array After Applying Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2779 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-beauty-of-an-array-after-applying-operation](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/).

### Goal
Given an integer array `nums` and a non-negative integer `k`, you are allowed to modify each element `nums[i]` to any value within the range `[nums[i] - k, nums[i] + k]` exactly once.

The "beauty" of the array is defined as the length of the longest subsequence consisting of entirely equal elements. Your task is to find and return the maximum possible beauty of the array after applying this operation optimally.

### Function Contract
**Inputs**

- `nums`: `list[int]` - An array of integers.
- `k`: `int` - A non-negative integer representing the maximum allowed adjustment radius for each element.

**Return value**

- `int` - The maximum possible length of a subsequence of equal elements after modifications.

### Examples
**Example 1**

- Input: `nums = [4, 6, 1, 2]`, `k = 2`
- Output: `3`
- Explanation: We can choose the subsequence `[4, 1, 2]`. By choosing a target value of `3`, we can transform:
  - `4` to `3` (since $|4 - 3| \le 2$)
  - `1` to `3` (since $|1 - 3| \le 2$)
  - `2` to `3` (since $|2 - 3| \le 2$)
  The length of this subsequence is `3`, which is the maximum possible.

**Example 2**

- Input: `nums = [1, 1, 1, 1]`, `k = 10`
- Output: `4`
- Explanation: All elements are already equal, so no operations are needed to achieve a beauty of `4`.

---

## Solution
### Approach
The problem can be modeled as finding the maximum number of overlapping intervals. For each element $x$ in `nums`, we can think of it as representing an interval $[x - k, x + k]$. We want to find a point $y$ that is covered by the maximum number of intervals.

By sorting the array `nums`, we can simplify this interval overlap problem into a **Sliding Window (Two Pointers)** problem:
1. If we sort `nums` in non-decreasing order, any valid subsequence of elements that can be transformed to the same value will form a contiguous subarray.
2. For any subarray `nums[left...right]` to be transformable to a single value, the difference between the maximum element (`nums[right]`) and the minimum element (`nums[left]`) must not exceed $2k$. That is, `nums[right] - nums[left] <= 2 * k`.
3. We can maintain a sliding window `[left, right]`. As we expand the window by incrementing `right`, if the condition `nums[right] - nums[left] > 2 * k` is violated, we shrink the window from the left.
4. Alternatively, we can use a non-shrinking sliding window where the window size only grows or stays constant, representing the maximum valid window size found so far.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ where $N$ is the length of the array `nums`. This is dominated by the sorting step. The sliding window traversal itself takes $\mathcal{O}(N)$ time as both pointers traverse the array at most once.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space if the sorting is performed in-place (or $\mathcal{O}(N)$ depending on the language's internal sorting implementation).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum beauty of the array after applying the operation.

    The beauty is the maximum number of elements that can be made equal.
    This is equivalent to finding the longest subarray in the sorted version
    of nums where the difference between the maximum and minimum elements
    is at most 2 * k.
    """
    nums.sort()
    left = 0

    # Non-shrinking sliding window
    for right in range(len(nums)):
        if nums[right] - nums[left] > 2 * k:
            left += 1

    return len(nums) - left
```
</details>
