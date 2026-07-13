# Find the Sum of Subsequence Powers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3098 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-sum-of-subsequence-powers](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/).

### Goal
Given an array of integers and an integer `k`, identify all subsequences of length `k`. For each subsequence, calculate its "power," defined as the minimum absolute difference between any two elements within that subsequence. The objective is to return the sum of these powers across all possible subsequences of length `k`, modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the required length of the subsequences.

**Return value**

- An integer representing the sum of the powers of all subsequences of length `k`, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 3`
- Output: `1`
- Explanation: The only subsequence of length 3 is [1, 2, 3]. The differences are |2-1|=1, |3-2|=1, |3-1|=2. The minimum is 1.

**Example 2**

- Input: `nums = [8, 4, 2], k = 2`
- Output: `12`
- Explanation: Subsequences are [8, 4] (diff 4), [8, 2] (diff 6), [4, 2] (diff 2). Sum = 4 + 6 + 2 = 12. Wait, the example logic follows: |8-4|=4, |8-2|=6, |4-2|=2. Sum = 12.

**Example 3**

- Input: `nums = [1, 1, 1], k = 2`
- Output: `0`
- Explanation: All subsequences are [1, 1], power is 0. Sum = 0.

---

## Solution
### Approach
The problem is solved using a combination of sorting, dynamic programming, and the inclusion-exclusion principle (or counting via DP). Since the power is defined by the minimum difference, we sort the array first. We then use DP to count how many subsequences have a minimum difference of at least `x`. By calculating this for all possible differences `x`, we can derive the sum of powers using the property: Sum = Σ (count(min_diff >= x)).

### Complexity Analysis
- **Time Complexity**: O(n^3 * k), where n is the length of the array. Sorting takes O(n log n), and the DP state involves iterating through n, k, and the possible differences.
- **Space Complexity**: O(n^2 * k) to store the DP table for the subsequence counts.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    mod = 10**9 + 7
    arr = sorted(nums)
    n = len(arr)

    diffs = sorted({arr[j] - arr[i] for i in range(n) for j in range(i + 1, n) if arr[j] > arr[i]})
    if not diffs:
        return 0

    def count_with_min_gap(gap: int) -> int:
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            dp[1][i] = 1

        for length in range(2, k + 1):
            prefix = 0
            left = 0
            for right in range(n):
                while left < right and arr[right] - arr[left] >= gap:
                    prefix = (prefix + dp[length - 1][left]) % mod
                    left += 1
                dp[length][right] = prefix

        return sum(dp[k]) % mod

    answer = 0
    previous = 0
    for gap in diffs:
        count = count_with_min_gap(gap)
        answer = (answer + (gap - previous) * count) % mod
        previous = gap

    return answer
```
</details>
