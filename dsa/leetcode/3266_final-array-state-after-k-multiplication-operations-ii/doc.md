# Final Array State After K Multiplication Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3266 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [final-array-state-after-k-multiplication-operations-ii](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/).

### Goal
Given an array of integers, perform exactly `k` operations. In each operation, identify the smallest element in the array (if there are ties, pick the leftmost one) and multiply it by a given multiplier `m`. Since `k` can be very large, the solution must efficiently handle the multiplication process using modular arithmetic for the final result.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `k`: An integer representing the number of multiplication operations to perform.
- `multiplier`: An integer representing the value to multiply the smallest element by.

**Return value**

- A list of integers representing the final state of the array after `k` operations, with each element taken modulo `10^9 + 7`.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 5, 6], k = 5, multiplier = 2`
- Output: `[8, 4, 6, 5, 6]`

**Example 2**

- Input: `nums = [1, 2], k = 3, multiplier = 4`
- Output: `[16, 8]`

**Example 3**

- Input: `nums = [100000], k = 2, multiplier = 1`
- Output: `[100000]`

---

## Solution
### Approach
The problem requires a Min-Heap to efficiently track the smallest element. Because `k` can be extremely large, we cannot simulate the operations one by one. Instead, we perform individual multiplications until all elements in the heap reach a similar magnitude (relative to the maximum element in the initial array). Once the elements are balanced, we distribute the remaining operations using modular exponentiation to apply the multiplier uniformly across the array.

### Complexity Analysis
- **Time Complexity**: `O(n log n + k log n)` in the worst case for the initial simulation phase, but effectively `O(n log n + log k)` due to the mathematical optimization once elements are balanced.
- **Space Complexity**: `O(n)` to store the heap and the final array.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def solve(nums, k, multiplier):
    if multiplier == 1:
        return [x % (10**9 + 7) for x in nums]

    MOD = 10**9 + 7
    n = len(nums)
    heap = [(nums[i], i) for i in range(n)]
    heapq.heapify(heap)

    max_val = max(nums)

    # Simulation phase: multiply until all elements are close to max_val
    while k > 0 and heap[0][0] * multiplier <= max_val:
        val, idx = heapq.heappop(heap)
        new_val = val * multiplier
        heapq.heappush(heap, (new_val, idx))
        k -= 1

    # Mathematical phase: distribute remaining k operations
    # Each element will be multiplied by multiplier^(k // n)
    # The first (k % n) elements will be multiplied by an additional multiplier
    full_rounds = k // n
    extra_ops = k % n

    multiplier_pow = pow(multiplier, full_rounds, MOD)

    final_res = [0] * n

    # Sort heap to process elements in order of their current values
    sorted_heap = sorted(heap)

    for i in range(n):
        val, idx = sorted_heap[i]
        # Apply extra multiplier to the first 'extra_ops' elements
        if i < extra_ops:
            final_res[idx] = (val % MOD * multiplier_pow % MOD * multiplier % MOD) % MOD
        else:
            final_res[idx] = (val % MOD * multiplier_pow % MOD) % MOD

    return final_res
```
</details>
