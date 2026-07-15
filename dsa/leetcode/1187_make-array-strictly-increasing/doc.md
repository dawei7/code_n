# Make Array Strictly Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1187 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-strictly-increasing/) |

## Problem Description

### Goal

You are given two integer arrays, `arr1` and `arr2`. An operation chooses indices `i` and `j` within their respective arrays and performs the assignment `arr1[i] = arr2[j]`. The chosen value is not removed from `arr2`, so any index there remains available for later operations.

Find the minimum number of operations, possibly zero, needed to make `arr1` strictly increasing: every element must be greater than the element immediately before it. Return `-1` if no sequence of allowed assignments can produce such an array.

### Function Contract

**Inputs**

- `arr1`: A list of length $n$, where $1\le n\le2000$ and $0\le\texttt{arr1[i]}\le10^9$.
- `arr2`: A list of length $m$, where $1\le m\le2000$ and $0\le\texttt{arr2[j]}\le10^9$.

**Return value**

- The minimum number of assignments required to make `arr1` strictly increasing, or `-1` when it is impossible.

### Examples

**Example 1**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [1,3,2,4]`
- Output: `1`

Replace `arr1[1]` with `2` to obtain `[1,2,3,6,7]`.

**Example 2**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [4,3,1]`
- Output: `2`

Replacing the two middle values produces `[1,3,4,6,7]`.

**Example 3**

- Input: `arr1 = [1,5,3,6,7]`, `arr2 = [1,6,3,3]`
- Output: `-1`

### Required Complexity

- **Time:** $O(nm\log m)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Represent only the previous value.** After a prefix of `arr1` has been processed, a state maps its final value to the fewest replacements used to reach a strictly increasing prefix ending there. The initial state has previous value `-1` and cost zero, which is safe because every input value is nonnegative.

**Keep or replace the current element.** From state `(previous, operations)`, retain the current `arr1` value only when `value > previous`. For a replacement, sort and deduplicate `arr2`, then use binary search to find its smallest value strictly greater than `previous`. No larger replacement with the same operation count can be better: it leaves fewer choices for every later element. Record the lower cost whenever multiple paths produce the same final value.

**Discard dominated states.** Process the next states by increasing final value while tracking the smallest operation count seen. If an earlier state has both a smaller final value and no greater cost, any later state with the same or higher cost can never lead to a better continuation. Removing it preserves every potentially optimal path while limiting the frontier to at most the number of distinct replacement values plus the current original value. If the frontier becomes empty, no strictly increasing construction exists; otherwise the minimum final cost is the answer.

#### Complexity detail

Let $m$ also denote the number of distinct values remaining after deduplicating `arr2`; this can only decrease the original length. Sorting costs $O(m\log m)$. At most $m+1$ live states are processed for each of the $n$ positions, and each replacement transition uses an $O(\log m)$ binary search. The overall bound is $O(nm\log m)$ time. The current and next frontiers plus the sorted candidates use $O(m)$ space.

#### Alternatives and edge cases

- **Linear replacement search:** Scanning sorted `arr2` from the beginning for every state is correct but raises a transition from $O(\log m)$ to $O(m)$.
- **Two-dimensional dynamic programming:** A table indexed by prefix and replacement count can derive compatible replacement runs, but it uses $O(n^2)$ storage without rolling-array optimization.
- **Already strictly increasing:** Keeping every original element leaves the answer at zero.
- **Duplicate replacement values:** Equal values are interchangeable and cannot appear consecutively in a strictly increasing result, so deduplicating `arr2` is safe.
- **Reuse semantics:** An `arr2` value is not consumed, although strict increase usually prevents choosing the same value for two positions in one result.
- **Single-element `arr1`:** It is already strictly increasing, so zero operations are sufficient.
- **No compatible successor:** A state with neither a larger original value nor a larger replacement disappears; an empty frontier means the answer is `-1`.
- **Strict comparison:** Equality is invalid. Both the keep test and binary search must require a value strictly greater than the previous one.

</details>
