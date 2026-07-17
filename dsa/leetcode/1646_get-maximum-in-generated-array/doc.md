# Get Maximum in Generated Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1646 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/get-maximum-in-generated-array/) |

## Problem Description
### Goal
Given an integer `n`, generate a 0-indexed array `nums` of length `n + 1`. Set `nums[0] = 0`, and set `nums[1] = 1` when that index exists.

For every valid generated index, an even index `2 * i` receives `nums[i]`, while an odd index `2 * i + 1` receives `nums[i] + nums[i + 1]`. Return the maximum value anywhere in the completed array.

### Function Contract
**Inputs**

- `n`: the final generated index, where $0 \le n \le 100$.

**Return value**

Return the maximum among `nums[0]` through `nums[n]` after applying the recurrence to every valid index.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `3`

The generated array is `[0,1,1,2,1,3,2,3]`.

**Example 2**

- Input: `n = 2`
- Output: `1`

**Example 3**

- Input: `n = 3`
- Output: `2`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Generate in index order.** Handle `n = 0` separately. Otherwise allocate `n + 1` entries, initialize indices 0 and 1, and visit each index from 2 through `n`. For current index `j`, let `i = j // 2`. If `j` is even, copy `nums[i]`; if it is odd, add `nums[i]` and `nums[i + 1]`.

Both source indices are smaller than the destination index, so their values have already been generated. This ordering applies each recurrence exactly once and produces the uniquely defined array. Track the largest value as each entry is written, avoiding a separate maximum scan.

#### Complexity detail

The loop writes each of the $n+1$ array positions at most once, taking $O(n)$ time. The generated array uses $O(n)$ space. Since the complete source domain has only 101 inputs and at most 101 generated entries, the package uses a bounded-domain certificate with an exhaustive recurrence oracle instead of claiming a stable runtime scaling trend.

#### Alternatives and edge cases

- **Recursive value computation:** Memoize the recurrence for every requested index and then take the maximum. It has the same asymptotic bounds but adds recursion overhead.
- **Generate parent pairs:** For each parent index `i`, write both children `2 * i` and `2 * i + 1` when in range. This is equivalent but needs careful boundary checks.
- **Recompute every value recursively:** Omitting memoization repeats shared subproblems and performs unnecessary work.
- At `n = 0`, the sole value is zero.
- At `n = 1`, the maximum is the initialized value one.
- The odd-index rule reads `nums[i + 1]`, which is already available because $i+1 < 2i+1$ for every applicable $i$.
- The maximum need not occur at index `n`, so returning only the final entry is incorrect.

</details>
