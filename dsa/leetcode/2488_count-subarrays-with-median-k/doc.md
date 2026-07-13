# Count Subarrays With Median K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2488 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-subarrays-with-median-k](https://leetcode.com/problems/count-subarrays-with-median-k/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-subarrays-with-median-k/).

### Goal
Given an array of distinct integers and a target value `k`, determine the total number of contiguous subarrays where the median is exactly `k`. For an array of length `n`, the median is defined as the element at index `(n-1)/2` in the sorted version of the subarray.

### Function Contract
**Inputs**

- `nums`: A list of distinct integers.
- `k`: An integer that must be present in the array.

**Return value**

- An integer representing the count of subarrays whose median is `k`.

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 4, 5], k = 4`
- Output: `3`
- Explanation: The subarrays are `[4]`, `[4, 5]`, and `[1, 4, 5]`.

**Example 2**

- Input: `nums = [2, 3, 1], k = 3`
- Output: `1`
- Explanation: The only subarray is `[3]`.

**Example 3**

- Input: `nums = [1], k = 1`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Prefix Sum** approach combined with a **Hash Map**. We transform the array into a sequence of `+1` (if `nums[i] > k`), `-1` (if `nums[i] < k`), and `0` (if `nums[i] == k`). A subarray has median `k` if the sum of these transformed values is either `0` (for odd length) or `1` (for even length). We track the prefix sums to the left of `k` in a hash map and compare them with prefix sums to the right of `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array once to find `k` and once to compute prefix sums.
- **Space Complexity**: `O(n)` to store the frequency of prefix sums in the hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    k_index = -1
    for i in range(n):
        if nums[i] == k:
            k_index = i
            break

    # counts stores the frequency of prefix sums to the left of k_index
    # We use a dictionary to store the balance: (count of > k) - (count of < k)
    counts = {0: 1}
    current_balance = 0

    # Traverse left from k_index to store prefix balances
    for i in range(k_index - 1, -1, -1):
        if nums[i] < k:
            current_balance -= 1
        else:
            current_balance += 1
        counts[current_balance] = counts.get(current_balance, 0) + 1

    ans = 0
    current_balance = 0
    # Traverse right from k_index and check for valid subarrays
    # A subarray is valid if the total balance is 0 or 1
    for i in range(k_index, n):
        if nums[i] < k:
            current_balance -= 1
        elif nums[i] > k:
            current_balance += 1

        # We need total_balance to be 0 or 1
        # left_balance + right_balance = 0 => left_balance = -right_balance
        # left_balance + right_balance = 1 => left_balance = 1 - right_balance
        ans += counts.get(-current_balance, 0)
        ans += counts.get(1 - current_balance, 0)

    return ans
```
</details>
