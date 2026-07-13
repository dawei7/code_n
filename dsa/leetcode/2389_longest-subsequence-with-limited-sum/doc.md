# Longest Subsequence With Limited Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2389 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-subsequence-with-limited-sum](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-subsequence-with-limited-sum/).

### Goal
Given an array of positive integers `nums` and an array of positive integers `queries`, your task is to determine, for each query, the maximum possible length of a subsequence from `nums` such that the sum of its elements does not exceed the given query value. The result should be an array containing the answer for each query in the order they appear in the input `queries` array.

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of positive integers.
- `queries`: `List[int]` - An array of positive integers representing the sum limits.

**Return value**

`List[int]` - An array `answer` where `answer[i]` is the maximum length of a subsequence from `nums` whose sum is less than or equal to `queries[i]`.

### Examples
**Example 1**

- Input: `nums = [4,5,2,1]`, `queries = [3,10,21]`
- Output: `[2,3,4]`
- Explanation:
    - For `queries[0] = 3`: The sorted `nums` is `[1,2,4,5]`. The subsequence `[1,2]` has sum `3` and length `2`. This is the longest possible.
    - For `queries[1] = 10`: The subsequence `[1,2,4]` has sum `7` and length `3`. Adding `5` would make the sum `12`, exceeding `10`.
    - For `queries[2] = 21`: The subsequence `[1,2,4,5]` has sum `12` and length `4`. This is the longest possible (all elements).

**Example 2**

- Input: `nums = [2,3,4,5]`, `queries = [1]`
- Output: `[0]`
- Explanation:
    - For `queries[0] = 1`: No element in `nums` is less than or equal to `1`. Thus, no subsequence can be formed, and the length is `0`.

**Example 3**

- Input: `nums = [1]`, `queries = [100]`
- Output: `[1]`
- Explanation:
    - For `queries[0] = 100`: The subsequence `[1]` has sum `1` and length `1`. This is the longest possible.

---

## Solution
### Approach
The problem can be efficiently solved by combining **Sorting**, **Prefix Sums**, and **Binary Search**.

1.  **Greedy Choice (Sorting):** To maximize the length of a subsequence given a sum limit, we should always prioritize picking the smallest numbers first. This is a greedy approach. Therefore, the first step is to sort the `nums` array in non-decreasing order.

2.  **Prefix Sums:** After sorting `nums`, we can compute a prefix sum array. Each element `prefix_sums[i]` will store the sum of the first `i+1` elements of the sorted `nums` array (i.e., `nums[0] + nums[1] + ... + nums[i]`). This array allows us to quickly find the sum of any initial segment of the sorted `nums`.

3.  **Binary Search:** For each query `q`, we need to find the largest index `k` such that `prefix_sums[k] <= q`. The value `k+1` will then be the maximum length of the subsequence. This search for an upper bound in a sorted array (the prefix sums array) is a classic application of binary search. Specifically, we are looking for the "insertion point" where `q` would be placed to maintain sorted order, such that all elements to its left are less than or equal to `q`. The `bisect_right` function from Python's `bisect` module is ideal for this. The index returned by `bisect_right` directly corresponds to the count of elements (length) whose sum is less than or equal to the query.

### Complexity Analysis
- **Time Complexity**:
    - Sorting `nums`: `O(N log N)`, where `N` is the length of `nums`.
    - Calculating prefix sums: `O(N)`.
    - For each query, performing a binary search on the `prefix_sums` array: `O(log N)`. Since there are `M` queries, this step takes `O(M log N)`.
    - Total time complexity: `O(N log N + M log N)`.

- **Space Complexity**:
    - Storing the `prefix_sums` array: `O(N)`.
    - Storing the `answer` array: `O(M)`.
    - Total space complexity: `O(N + M)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
import bisect

def solve(nums: list[int], queries: list[int]) -> list[int]:
    # Step 1: Sort the nums array to ensure we pick the smallest elements first
    nums.sort()

    # Step 2: Compute prefix sums of the sorted nums array
    prefix_sums = []
    current_sum = 0
    for num in nums:
        current_sum += num
        prefix_sums.append(current_sum)

    # Step 3: For each query, use binary search on the prefix_sums array
    ans = []
    for query in queries:
        # bisect_right returns an insertion point which comes after (to the right of)
        # any existing entries of the query value.
        # This index directly corresponds to the count of elements in nums
        # whose sum is less than or equal to the query.
        #
        # Example: nums = [1, 2, 4, 5], prefix_sums = [1, 3, 7, 12]
        # If query = 10:
        # bisect.bisect_right(prefix_sums, 10) returns 3.
        # This means prefix_sums[0] (1), prefix_sums[1] (3), prefix_sums[2] (7)
        # are all <= 10. prefix_sums[2] (value 7) is the sum of the first 3 elements of nums.
        # So, the maximum length is 3.
        length = bisect.bisect_right(prefix_sums, query)
        ans.append(length)

    return ans
```
</details>
