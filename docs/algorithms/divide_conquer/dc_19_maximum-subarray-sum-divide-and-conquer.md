# Maximum Subarray Sum (Divide and Conquer)

| | |
|---|---|
| **ID** | `dc_19` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |

## Problem statement

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
*Constraint:* You MUST solve it using the Divide and Conquer approach, rather than the more optimal $O(N)$ Kadane's Algorithm.

**Input:** An integer array `nums`.
**Output:** An integer representing the maximum subarray sum.

## When to use it

- When specifically requested to prove you can map array interval problems to a recursion tree.
- When you need to answer multiple queries about the maximum subarray in *different* ranges of the array dynamically (in which case this exact logic is used to build a Segment Tree).

## Approach

**1. The Spatial Logic of the Max Subarray:**
If we split an array precisely in half (Left Half and Right Half), the global maximum contiguous subarray MUST exist in exactly one of three places:
1. It is entirely contained within the Left Half.
2. It is entirely contained within the Right Half.
3. It straddles the dividing line, spanning across both the Left and Right halves!

**2. The Divide Step:**
Find the `mid` point.
Recursively call `max_subarray(left, mid)` to find the best subarray strictly on the left.
Recursively call `max_subarray(mid + 1, right)` to find the best subarray strictly on the right.

**3. The Conquer Step (The Crossing Sum):**
How do we find the maximum subarray that straddles the dividing line?
It MUST include `nums[mid]` and `nums[mid+1]`.
So, we start at `mid` and iterate backwards to the left, keeping a running sum, and record the absolute maximum sum we ever hit. Let's call this `max_left_cross`.
Then, we start at `mid+1` and iterate forwards to the right, keeping a running sum, and record the absolute maximum sum we ever hit. Let's call this `max_right_cross`.
The absolute best crossing subarray sum is simply `max_left_cross + max_right_cross`!

**4. Final Resolution:**
Return the maximum of the three possibilities: `Left Half Max`, `Right Half Max`, or the `Crossing Max`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_19: Maximum Subarray Sum (Divide and Conquer).

Given an array of n integers (with at least one
"""


def solve(arr, n):
    """Maximum subarray sum via divide and conquer."""

    def rec(lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        # Best fully in the left half.
        left_best = rec(lo, mid)
        # Best fully in the right half.
        right_best = rec(mid + 1, hi)
        # Best crossing the middle: extend leftward from mid,
        # then rightward from mid+1, and combine.
        s = 0
        left_sum = arr[mid]
        for i in range(mid, lo - 1, -1):
            s += arr[i]
            if s > left_sum:
                left_sum = s
        s = 0
        right_sum = arr[mid + 1]
        for i in range(mid + 1, hi + 1):
            s += arr[i]
            if s > right_sum:
                right_sum = s
        cross = left_sum + right_sum
        return max(left_best, right_best, cross)

    return rec(0, n - 1)
```

</details>

## Walk-through

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`. N = 9.
Let's focus on the crossing calculation for the very top-level split:
`left = 0`, `right = 8`, `mid = 4` (val `-1`).
Left Half: `[-2, 1, -3, 4, -1]`. Right Half: `[2, 1, -5, 4]`.

1. **Calculate `max_left_cross` (from `mid=4` down to `0`):**
   - index 4 (val -1): sum = -1. `left_sum = -1`.
   - index 3 (val 4): sum = 3. `left_sum = 3`.
   - index 2 (val -3): sum = 0. `left_sum` remains `3`.
   - index 1 (val 1): sum = 1. `left_sum` remains `3`.
   - index 0 (val -2): sum = -1. `left_sum` remains `3`.
   - Best leftward sum is `3`.
2. **Calculate `max_right_cross` (from `mid=5` up to `8`):**
   - index 5 (val 2): sum = 2. `right_sum = 2`.
   - index 6 (val 1): sum = 3. `right_sum = 3`.
   - index 7 (val -5): sum = -2. `right_sum` remains `3`.
   - index 8 (val 4): sum = 2. `right_sum` remains `3`.
   - Best rightward sum is `3`.
3. **Combine:**
   - `cross_max = 3 + 3 = 6`.

*(Assume the left half returned 4, and right half returned 4).*
Return `max(4, 4, 6) = 6`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Average** | $O(N \log N)$ | $O(\log N)$ |
| **Worst** | $O(N \log N)$ | $O(\log N)$ |

The recursion tree has a depth of log_2 N.
At each level, calculating the crossing sum requires iterating linearly from the middle to the edges. Across all nodes at a specific level of the tree, the entire array is iterated exactly once, doing $O(N)$ work.
By the Master Theorem T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Space complexity is $O(\log N)$ for the recursion call stack.

## Variants & optimizations

- **Kadane's Algorithm ($O(N)$):** The strictly superior Dynamic Programming approach. `local_max = max(nums[i], local_max + nums[i])`, `global_max = max(global_max, local_max)`. It maintains a running sum and resets to 0 if the sum dips negative. Requires only $O(1)$ space.
- **Segment Tree ($O(N)$ build, $O(\log N)$ query):** If you need to repeatedly ask for the maximum subarray sum of DIFFERENT ranges within the same array (e.g., "What is the max sum between index 100 and 500?"), Kadane's takes $O(N)$ per query. A Segment Tree stores the `left_max`, `right_max`, `total_sum`, and `global_max` for every node in a binary tree, allowing $O(\log N)$ instantaneous queries!

## Real-world applications

- **Financial Trading Systems:** While Kadane's is better for static arrays, the Divide and Conquer/Segment Tree variant is heavily used in real-time order books to quickly query the maximum localized price drawdown or profit surge over arbitrary, dynamically changing historical time windows.

## Related algorithms in cOde(n)

- **[dp_06 - Kadane's Algorithm](../dynamic/dp_06_kadanes-algorithm.md)** — The strictly superior $O(N)$ DP approach.
- **[dc_02 - Majority Element](dc_02_majority-element.md)** — The identical algorithmic skeleton (split, recurse left, recurse right, merge crossing logic).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
