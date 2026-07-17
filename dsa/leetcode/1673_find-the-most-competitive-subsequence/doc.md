# Find the Most Competitive Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1673 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-most-competitive-subsequence/) |

## Problem Description
### Goal
Choose exactly $k$ elements from `nums` while preserving their original relative order. Elements not chosen may be erased from any positions, so the result is a subsequence rather than necessarily a contiguous subarray.

Among all length-$k$ subsequences, return the most competitive one: compare two candidates from left to right, and at the first index where they differ, the candidate with the smaller value is more competitive. Equal values do not decide the order, so comparison continues to the next position.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$ whose values may repeat.
- `k`: the required positive subsequence length, with $1 \le k \le n$.

**Return value**

Return the lexicographically smallest subsequence of `nums` containing exactly $k$ elements.

### Examples
**Example 1**

- Input: `nums = [3,5,2,6], k = 2`
- Output: `[2,6]`

**Example 2**

- Input: `nums = [2,4,3,3,5,4,9,6], k = 4`
- Output: `[2,3,3,4]`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**View the budget as removable elements.** Exactly $n-k$ values must be discarded. Scan `nums` from left to right while storing the best prefix chosen so far in a stack. A later smaller value should replace larger values at the end of that prefix whenever the remaining removal budget permits it.

**Remove a dominated suffix greedily.** Before appending the current value, repeatedly pop the stack while its top is greater, the stack is nonempty, and removals remain. Replacing the earliest possible larger selected value with the current smaller value makes the candidate lexicographically better. Values deeper in the stack are already fixed before that position, and popping consumes one of the deletions needed to keep the final length at $k$.

**Keep equal values stable.** Use a strict greater-than comparison for popping. Replacing an equal earlier value with a later copy cannot improve the current position and only discards future flexibility, so the earlier equal value remains.

**Spend unused removals on trailing candidates.** Append a scanned value after the beneficial pops only while the stack contains fewer than $k$ values. Once it is full, a current value that could not improve the stack is discarded and consumes one removal. This performs the trailing deletions online and keeps the stored prefix capped at the required output length.

**Why each greedy replacement is safe.** When a larger stack top is popped for a smaller current value, the result first differs from the old candidate at that popped position and is smaller there. The deletion budget proves enough total elements remain to complete length $k$. Any optimal candidate that kept the larger value at that position would therefore be lexicographically worse, so applying all such replacements cannot exclude the optimum.

#### Complexity detail

Every input value is considered once, pushed at most once, and popped at most once, so the total stack work is $O(n)$. The stack is capped at the required output length and therefore uses $O(k)$ auxiliary space.

#### Alternatives and edge cases

- **Repeated feasible-window minimum:** For each output position, scan the range in which the next choice may occur. This is correct but can inspect $O(nk)$ values.
- **Segment tree range minima:** Repeated minimum-index queries can achieve $O(k\log n)$ time, but the monotonic stack is simpler and asymptotically linear.
- **Sort by value:** Sorting loses the original relative-order requirement and does not produce a valid subsequence in general.
- If $k=n$, no deletion is available and the original array must be returned.
- If $k=1$, the smallest array value is chosen; among equal minima, the earliest is sufficient.
- A descending array spends the deletion budget removing its early large values.
- An ascending array leaves the stack intact and discards only its suffix.
- Equal values are preserved in their original order and may appear multiple times in the answer.

</details>
