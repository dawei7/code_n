# Maximum Width Ramp

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 962 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-width-ramp](https://leetcode.com/problems/maximum-width-ramp/) |

## Problem Description

### Goal

In an integer array `nums`, a ramp is a pair of indices `(i, j)` satisfying both $i<j$ and `nums[i] <= nums[j]`. Its width is the distance between those indices, $j-i$.

Choose a valid ramp with the greatest possible width and return that width. The pair may span values between its endpoints; only the endpoint inequality matters. Equality is permitted. If the array contains no pair satisfying the ramp conditions, return `0`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $N$, where $2 \le N \le 5\times10^4$.
- Every value satisfies $0 \le \texttt{nums[i]} \le 5\times10^4$.

**Return value**

Return the maximum value of $j-i$ over all ramps `(i, j)`, or `0` when no ramp exists.

### Examples

**Example 1**

- Input: `nums = [6,0,8,2,1,5]`
- Output: `4`
- Explanation: Indices `(1, 5)` form a ramp because `nums[1] = 0 <= 5 = nums[5]`.

**Example 2**

- Input: `nums = [9,8,1,0,1,9,4,0,4,1]`
- Output: `7`
- Explanation: The equal endpoint values at indices `(2, 9)` form a width-`7` ramp.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Keep only useful left endpoints.** Scan from left to right and push index `i` onto a stack only when `nums[i]` is strictly smaller than the value at the current top. The stack therefore holds indices with strictly decreasing values. Any skipped index has an earlier index with a value no larger, so the skipped index can never produce a wider ramp than that earlier candidate.

**Test right endpoints from widest to narrowest.** Scan `j` from the last index toward the first. While the top candidate satisfies `nums[stack[-1]] <= nums[j]`, it forms a ramp: update the maximum with `j - stack[-1]` and pop it. Because right endpoints are processed in decreasing order, this is the farthest possible valid `j` for that left index; the candidate can never improve after being popped.

**Why all optimal pairs survive.** Every potentially optimal left endpoint is represented by the decreasing stack, either directly or by an earlier dominating index. The reverse scan finds the farthest compatible right endpoint before discarding each candidate. Thus the largest recorded distance equals the maximum width over all valid ramps.

#### Complexity detail

Each index is pushed at most once and popped at most once, and the two scans are linear. The running time is $O(N)$ and the monotonic stack uses $O(N)$ auxiliary space in the strictly decreasing case.

#### Alternatives and edge cases

- **Sorted indices:** Sort indices by their values and track the smallest index seen. This obtains the maximum width in $O(N\log N)$ time and $O(N)$ space.
- **Prefix minima and suffix maxima:** Build both arrays, then advance two pointers to find the widest compatible pair in $O(N)$ time with $O(N)$ space.
- **All index pairs:** Testing every `(i, j)` directly is correct but takes $O(N^2)$ time.
- **Strictly decreasing array:** No valid ramp exists, so the result is `0`.
- **Equal endpoints:** The relation is non-strict, so equal values may form a ramp and can span the full array.
- **Adjacent ramp:** A width of `1` is valid when its two values satisfy the endpoint inequality.

</details>
