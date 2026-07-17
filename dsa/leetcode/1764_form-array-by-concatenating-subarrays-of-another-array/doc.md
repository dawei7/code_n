# Form Array by Concatenating Subarrays of Another Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1764 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/) |

## Problem Description

### Goal

You are given an ordered list of integer arrays called `groups` and a separate integer array `nums`. For every `groups[i]`, choose a contiguous subarray of `nums` containing exactly the same values in the same order.

The chosen subarrays must occur in `groups` order and may not overlap, although unused values of `nums` may appear before, between, or after them. Return whether all groups can be placed under these rules.

### Function Contract

**Inputs**

- `groups`: between $1$ and $10^3$ nonempty integer arrays, each of length at most $10^3$.
- `nums`: an integer array with $1 \le N \le 10^3$, where $N=\lvert\texttt{nums}\rvert$.
- Every stored integer lies between $-10^7$ and $10^7$, inclusive.

Let

$$
S=\sum_{g\in\texttt{groups}}\lvert g\rvert
$$

with $S\le 10^3$, and let $L=\max_{g\in\texttt{groups}}\lvert g\rvert$.

**Return value**

- Return `True` if every group can match a distinct, non-overlapping contiguous region of `nums` in the given group order; otherwise return `False`.

### Examples

**Example 1**

- Input: `groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]`
- Output: `True`
- Explanation: The first group starts at index `3`, and the second follows it at index `6`.

**Example 2**

- Input: `groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]`
- Output: `False`
- Explanation: Both arrays occur, but only in the reverse of the required group order.

**Example 3**

- Input: `groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]`
- Output: `False`
- Explanation: The only occurrences share the value `3`, and overlapping matches are forbidden.

### Required Complexity

- **Time:** $O(N+S)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Choose the earliest available occurrence**

Maintain the first index of `nums` that is still available. For the current group, choosing its earliest occurrence at or after that position is always safe: any later occurrence would leave a suffix no longer than the one left by the earliest match, so it cannot make subsequent groups easier to place.

**Build a prefix table for one group**

Treat each integer group as a pattern and construct its Knuth–Morris–Pratt prefix table. After a mismatch, the table preserves the longest pattern prefix that can still match the scanned suffix instead of restarting comparisons from the next candidate position.

**Advance one global boundary**

Run KMP through `nums` from the available position until the first complete pattern match. Return the index immediately after that match and use it as the starting boundary for the next group. This guarantees group order and makes overlap impossible.

**Fail when a group has no remaining match**

If KMP reaches the end of `nums` before completing the current pattern, no placement exists from the current boundary. The earlier-match argument means choosing different earlier occurrences of previous groups could only move this boundary rightward, so returning `False` is conclusive.

Inductively, after each group the maintained boundary is the earliest possible end of any valid placement of the processed prefix. Therefore a match for every group constructs a valid arrangement, while a failure proves that none exists.

#### Complexity detail

Prefix tables across all groups take $O(S)$ time. Searches start where the preceding match ended, so KMP scans each position of `nums` at most once across the complete process, for $O(N+S)$ total time. Only the current group's prefix table is retained, requiring $O(L)$ space.

#### Alternatives and edge cases

- **Slice at every candidate start:** This greedy search is correct but can take $O(NS)$ time on repeated prefixes.
- **Nested element comparisons:** Avoiding slice allocation still has the same worst-case repeated-comparison behavior without a prefix table.
- **Rolling hash:** Hashing can compare candidate blocks quickly, but requires collision handling to provide deterministic correctness.
- **Exact concatenation:** Groups may match back-to-back with no unused values between them.
- **Gaps between groups:** Unmatched `nums` values are allowed and should simply be scanned past.
- **Overlapping occurrences:** The next search begins after the previous match, so a shared element cannot be reused.
- **Required order:** Finding all groups in a different order is not sufficient.
- **Repeated prefixes:** KMP reuses prefix information rather than rescanning a long partial match.
- **Negative and boundary values:** Integers are compared directly; their sign and magnitude do not alter matching.
- **Insufficient remaining length:** The search naturally fails when no complete group can fit in the remaining suffix.

</details>
