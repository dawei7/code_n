# Minimum Number of Removals to Make Mountain Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1671 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |

## Problem Description
### Goal
An array is a mountain when it has at least three elements and some interior peak index. Values before that peak must be strictly increasing, and values after it must be strictly decreasing. Both sides must therefore contain at least one element; a purely increasing or purely decreasing sequence is not a mountain.

Given an integer array `nums`, remove as few elements as possible while preserving the relative order of all remaining elements so that they form a mountain array. Return the minimum removal count. The input guarantee ensures that at least one valid mountain subsequence can be retained.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $3 \le n \le 1000$ and values may repeat.

**Return value**

Return the minimum number of elements that must be removed so the remaining subsequence is strictly increasing to one interior peak and strictly decreasing afterward.

### Examples
**Example 1**

- Input: `nums = [1,3,1]`
- Output: `0`

**Example 2**

- Input: `nums = [2,1,1,5,6,2,3,1]`
- Output: `3`
- Explanation: retaining `[1,5,6,3,1]` produces a five-element mountain.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn removals into a longest-subsequence objective.** Removing elements preserves the order of those left behind. Minimizing removals is therefore equivalent to maximizing the length of a mountain subsequence, then subtracting that length from $n$.

**Measure the best ascent ending at every index.** Scan `nums` from left to right using patience-sorting tails. For each value, binary-search the first tail greater than or equal to it and record the resulting position plus one. This gives `increasing[i]`, the length of a longest strictly increasing subsequence ending at `i`. Using a lower-bound search is essential: an equal value replaces a tail but cannot extend a strict subsequence.

**Measure the best descent starting at every index.** Apply the same increasing-length procedure to the reversed array, then reverse the resulting lengths. In original order, `decreasing[i]` is the length of a longest strictly decreasing subsequence beginning at `i`, because reading that suffix backward turns its decreasing relation into an increasing one.

**Choose only valid peaks.** Index `i` can be a mountain peak only if both recorded lengths exceed one. For such an index, combine the two subsequences through their shared peak, obtaining length `increasing[i] + decreasing[i] - 1`. The maximum combined length is the longest retained mountain, so the answer is $n$ minus that maximum.

**Why the two sides can be combined.** The increasing subsequence ends at `nums[i]` and uses only earlier indices; the decreasing subsequence begins at the same value and uses only later indices. They overlap only at `i`, preserve original order, and satisfy strict inequalities on both sides. Conversely, any valid mountain has some peak, and each of its sides is bounded by the corresponding longest-side length recorded for that peak. Maximizing the combination therefore captures an optimal mountain subsequence.

#### Complexity detail

Each of the two patience-sorting scans performs one $O(\log n)$ binary search per element, taking $O(n\log n)$ time. The two length arrays and the tails arrays require $O(n)$ space. The final peak scan is linear and does not change either bound.

#### Alternatives and edge cases

- **Quadratic subsequence DP:** Compare every earlier pair for the increasing and decreasing lengths. It is direct and correct but requires $O(n^2)$ time.
- **Fenwick or segment tree:** Coordinate-compress values and query the best strict length below each value. This also achieves $O(n\log n)$ time but uses a heavier data structure.
- **Longest mountain subarray:** Two-pointer runs find only contiguous mountains, while removals may join elements that were separated in the input.
- Equal adjacent or separated values cannot both occupy one strict side of the retained mountain.
- A candidate peak with no smaller retained value on either side is invalid even if one side's subsequence is long.
- The optimal mountain may discard elements from the prefix, suffix, and interior simultaneously.
- An array that is already a strict mountain requires zero removals.
- Multiple peaks may yield the same maximum retained length; only that length affects the answer.

</details>
