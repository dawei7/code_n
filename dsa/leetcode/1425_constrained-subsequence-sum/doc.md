# Constrained Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1425 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/constrained-subsequence-sum/) |

## Problem Description

### Goal

Choose a nonempty subsequence of `nums` while preserving the original index order. For every pair of consecutive selected elements at indices `i` and `j`, their gap must satisfy $j-i \le k$.

Return the maximum possible sum of such a constrained subsequence. The answer may be negative because at least one element must be selected, and skipping elements does not remove the gap restriction between the selected indices on either side.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.
- `k`: the largest allowed index gap between consecutive selected values, where $1 \le k \le n$.

**Return value**

- The maximum sum of a nonempty subsequence whose consecutive selected indices differ by at most `k`.

### Examples

**Example 1**

- Input: `nums = [10,2,-10,5,20], k = 2`
- Output: `37`

**Example 2**

- Input: `nums = [-1,-2,-3], k = 1`
- Output: `-1`

**Example 3**

- Input: `nums = [10,-2,-10,-5,20], k = 2`
- Output: `23`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Best sum ending at each index.** Let the current dynamic-programming value be the best valid subsequence sum whose final selected index is `i`. Its preceding selected index, if any, must lie among the previous `k` positions. Extending a negative previous sum cannot help, so

$$
\texttt{dp[i]} = \texttt{nums[i]} + \max\left(0, \max_{i-k \le j < i} \texttt{dp[j]}\right).
$$

The answer is the largest ending value over all indices.

**Maintain the window maximum.** Store candidate pairs `(index, dp)` in a deque whose values decrease from front to back. Before processing index `i`, remove a front index smaller than `i-k`. The remaining front is the largest legal previous value. After computing the new value, remove all back values no greater than it because the new candidate is both newer and at least as useful, then append it.

**Why the recurrence and deque are exact.** The recurrence considers every possible predecessor and the option to start a new subsequence. The deque front equals the recurrence's window maximum because expired candidates are removed and dominated candidates can never become optimal before the newer larger value. Therefore each computed ending sum is exact, and their maximum is the requested nonempty subsequence sum.

#### Complexity detail

Each index enters and leaves the monotonic deque at most once, so all $n$ transitions take $O(n)$ time. The deque contains only indices from the last $k$ positions and uses $O(k)$ space.

#### Alternatives and edge cases

- **Scan the previous window:** Evaluate the maximum over up to `k` earlier states for every index. It is correct but takes $O(nk)$ time.
- **Max heap:** Store negative DP values with indices and lazily discard expired entries. This takes $O(n\log n)$ time.
- **All negative values:** Starting fresh at the largest individual value is optimal; never return zero for the required nonempty subsequence.
- **Negative bridge:** A negative element may be skipped only if the resulting selected-index gap stays within `k`.
- **k equal to one:** The recurrence becomes the maximum subarray recurrence because selected neighbors must be adjacent.
- **Large k:** Any earlier positive ending sum may remain available, but expired-index handling is still required.
- **Equal DP values:** Keep the newer one when removing dominated deque entries.

</details>
