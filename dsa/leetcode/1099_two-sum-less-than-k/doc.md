# Two Sum Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1099 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/two-sum-less-than-k/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, choose indices $i < j$ and let their values form the sum `nums[i] + nums[j]`. Among every such pair whose sum is strictly less than `k`, return the maximum sum.

The two values must come from different indices, although their numeric values may be equal. If no pair has a sum strictly below `k`, return `-1`.

### Function Contract

**Inputs**

- `nums`: an array of $n$ integers, where $1 \leq n \leq 100$ and $1 \leq \texttt{nums[i]} \leq 1000$.
- `k`: the strict upper bound for the pair sum, where $1 \leq \texttt{k} \leq 2000$.

**Return value**

The greatest value of `nums[i] + nums[j]` over distinct indices $i < j$ for which the sum is less than `k`, or `-1` when no valid pair exists.

### Examples

**Example 1**

- Input: `nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60`
- Output: `58`

Values 34 and 24 produce 58, and no valid pair has a larger sum below 60.

**Example 2**

- Input: `nums = [10, 20, 30], k = 15`
- Output: `-1`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort to expose monotonic choices.** Work with a sorted copy of `nums`. Place `left` at the smallest value and `right` at the largest. The current pair is the widest remaining combination, but its sum determines which endpoint can safely be discarded.

**Advance the smaller endpoint after a valid sum.** If `values[left] + values[right] < k`, record it as a candidate. Keeping the same left value while moving `right` inward cannot improve that sum, so every pair using this left endpoint is no better. Increment `left` to seek a larger candidate.

**Reduce the larger endpoint after an invalid sum.** If the current sum is at least `k`, pairing `values[right]` with any index between `left` and `right` only keeps or increases the sum. Therefore this right endpoint cannot participate in a valid remaining pair and can be decremented.

Each step discards one endpoint only after proving that it cannot yield a better valid answer. The pointers eventually cover all potentially optimal pair boundaries, and the best recorded candidate is consequently the maximum valid pair sum. If no candidate is recorded, no valid pair exists.

#### Complexity detail

Sorting the $n$ values costs $O(n \log n)$ time, and the two pointers make one $O(n)$ pass. The sorted copy uses $O(n)$ auxiliary space; the pointer state itself is constant-size.

#### Alternatives and edge cases

- **Check every pair:** A double loop is direct and correct but takes $O(n^2)$ time.
- **Sorting plus binary search:** For each left value, binary-search the largest compatible right value, also giving $O(n \log n)$ time.
- **Strict threshold:** A pair summing exactly to `k` is invalid and must force the right pointer inward.
- **Duplicate values:** Equal values may form a pair when they occupy different indices.
- **Fewer than two elements:** No pair exists, so the result is `-1`.
- **All sums too large:** The initialized `-1` remains unchanged.

</details>
