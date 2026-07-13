# Count Beautiful Splits in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3388 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-beautiful-splits-in-an-array](https://leetcode.com/problems/count-beautiful-splits-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-beautiful-splits-in-an-array/).

### Goal
Given an array of integers, determine the number of ways to partition the array into three non-empty contiguous subarrays (let's call them `nums1`, `nums2`, and `nums3`) such that either `nums1` is a prefix of `nums2`, or `nums2` is a prefix of `nums3`.

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le \text{nums.length} \le 5000$.

**Return value**

- An integer representing the total count of valid partitions $(i, j)$ such that the array is split at indices $i$ and $j$ ($0 < i < j < n$).

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 1]`
- Output: `3`
- Explanation: Valid splits are at indices (1, 2), (1, 3), and (2, 3).

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 2, 2, 2, 2]`
- Output: `12`

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with Longest Common Prefix (LCP) precomputation. We precompute an LCP table where `lcp[i][j]` stores the length of the longest common prefix between the suffix starting at `i` and the suffix starting at `j`. This allows $O(1)$ verification of whether one subarray is a prefix of another.

### Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the length of the array. The LCP table takes $O(n^2)$ to build, and the nested loops to count splits also take $O(n^2)$.
- **Space Complexity**: $O(n^2)$ to store the LCP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0

    mod1 = 1_000_000_007
    mod2 = 1_000_000_009
    base = 911_382_323

    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)

    for i, value in enumerate(nums):
        encoded = value + 1
        pow1[i + 1] = (pow1[i] * base) % mod1
        pow2[i + 1] = (pow2[i] * base) % mod2
        pref1[i + 1] = (pref1[i] * base + encoded) % mod1
        pref2[i + 1] = (pref2[i] * base + encoded) % mod2

    def same(left: int, right: int, length: int) -> bool:
        left_hash1 = (pref1[left + length] - pref1[left] * pow1[length]) % mod1
        right_hash1 = (pref1[right + length] - pref1[right] * pow1[length]) % mod1
        if left_hash1 != right_hash1:
            return False

        left_hash2 = (pref2[left + length] - pref2[left] * pow2[length]) % mod2
        right_hash2 = (pref2[right + length] - pref2[right] * pow2[length]) % mod2
        return left_hash2 == right_hash2

    count = 0

    for first_end in range(1, n - 1):
        first_prefixes_second = 2 * first_end <= n and same(0, first_end, first_end)

        if first_prefixes_second and 2 * first_end < n:
            count += n - 2 * first_end

        max_second_end = (n + first_end) // 2
        for second_end in range(first_end + 1, max_second_end + 1):
            if first_prefixes_second and second_end >= 2 * first_end:
                continue
            second_length = second_end - first_end
            if same(first_end, second_end, second_length):
                count += 1

    return count
```
</details>
