# Apply Operations to Maximize Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2818 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Greedy, Sorting, Monotonic Stack, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [apply-operations-to-maximize-score](https://leetcode.com/problems/apply-operations-to-maximize-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/apply-operations-to-maximize-score/).

### Goal
Given an array of integers and an integer `k`, you are tasked with selecting exactly `k` elements from the array. For each element, you can perform an operation: replace the element with the product of its prime factors (distinct). You want to maximize the product of the chosen `k` elements after performing these operations, where the selection must be made such that each element's contribution to the final product is determined by its "prime score" (the count of its distinct prime factors). Specifically, you must choose a subsequence of length `k` such that the product of the chosen elements is maximized, subject to the constraint that the elements are chosen based on their prime scores and their relative positions in the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the number of elements to select.

**Return value**

- An integer representing the maximum possible product of `k` elements modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [8, 3, 9, 3, 8], k = 2`
- Output: `81`
- Explanation: Prime scores are [1, 1, 1, 1, 1]. We pick 9 and 9 (or 8 and 9, etc). The max product is 81.

**Example 2**

- Input: `nums = [19, 12, 14, 6, 10, 18], k = 3`
- Output: `4788`

**Example 3**

- Input: `nums = [2, 4, 8, 16], k = 2`
- Output: `64`

---

## Solution
### Approach
1. **Sieve of Eratosthenes**: Precompute the number of distinct prime factors for all numbers up to the maximum value in `nums`.
2. **Monotonic Stack**: Determine the range `[L, R]` for each index `i` where `nums[i]` is the maximum element based on its prime score. This helps identify how many subsequences include `nums[i]`.
3. **Greedy Strategy**: Sort the elements by their values in descending order and pick the largest available elements until `k` elements are selected, using the counts derived from the monotonic stack.
4. **Modular Exponentiation**: Compute the final product modulo 10^9 + 7.

### Complexity Analysis
- **Time Complexity**: `O(N log(log M) + N)`, where `N` is the length of `nums` and `M` is the maximum value in `nums`. The sieve takes `O(M log log M)`, and the monotonic stack and sorting take `O(N log N)`.
- **Space Complexity**: `O(N + M)` to store the prime scores and the stack/auxiliary arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    max_val = max(nums)

    # Precompute prime scores only as far as this input needs.
    prime_scores = [0] * (max_val + 1)
    for i in range(2, max_val + 1):
        if prime_scores[i] == 0:
            for j in range(i, max_val + 1, i):
                prime_scores[j] += 1

    n = len(nums)
    scores = [prime_scores[x] for x in nums]

    # Monotonic stack to find how many subarrays have nums[i] as the max prime score
    # We use >= to handle duplicates consistently
    left = [-1] * n
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and scores[stack[-1]] < scores[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and scores[stack[-1]] <= scores[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # Calculate contribution of each index
    elements = []
    for i in range(n):
        count = (i - left[i]) * (right[i] - i)
        elements.append((nums[i], count))

    # Sort by value descending to pick the largest elements greedily
    elements.sort(key=lambda x: x[0], reverse=True)

    ans = 1
    remaining_k = k
    for val, count in elements:
        take = min(remaining_k, count)
        ans = (ans * pow(val, take, MOD)) % MOD
        remaining_k -= take
        if remaining_k == 0:
            break

    return ans
```
</details>
