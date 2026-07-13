# Wiggle Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 376 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) |

## Problem Description
### Goal
Given an integer array, choose a subsequence by deleting any number of elements while preserving the retained indices' order. It is a wiggle sequence when every consecutive difference is nonzero and the signs of those differences alternate positive, negative, positive, or negative, positive, negative.

Return the maximum possible wiggle subsequence length. A one-value sequence is valid, and a two-value sequence is valid when its values differ. Equal adjacent selected values produce a zero difference and cannot extend the pattern. Selected elements need not be contiguous. A one-element input returns `1`. Return only the maximum length, not the subsequence, and meet the follow-up target of $O(n)$ time.

### Function Contract
**Inputs**

- `nums`: a list of integers

**Return value**

- The length of the longest wiggle subsequence. A one-value subsequence has length one.

### Examples
**Example 1**

- Input: `nums = [1,7,4,9,2,5]`
- Output: `6`

**Example 2**

- Input: `nums = [1,17,5,10,13,15,10,5,16,8]`
- Output: `7`

**Example 3**

- Input: `nums = [1,2,3,4,5,6,7,8,9]`
- Output: `2`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the best sequence ending in each sign**

Maintain `up`, the longest wiggle subsequence seen so far whose last difference is positive, and `down`, the analogous length for a negative last difference. Both begin at one because any single value can start either future state.

When the current value is greater than the previous value, it can follow the best downward-ending sequence, so set `up = down + 1`. When it is smaller, set `down = up + 1`. Equal adjacent values create no valid difference and leave both states unchanged.

**Why adjacent comparisons are sufficient**

Within a rising run, keeping the latest—and therefore highest—value is never worse than keeping an earlier lower endpoint: it gives at least as much room for the next required drop. Symmetrically, within a falling run, the latest lowest value is the best endpoint for a future rise. Updating only when the sign changes, or replacing an endpoint while the sign stays the same, preserves an optimal subsequence without examining every earlier index.

The `up` and `down` recurrence expresses exactly this exchange. A positive step extends the best sequence that previously needed a rise, and a negative step extends the best sequence that needed a fall. At the end, the larger state is an optimal wiggle length.

**Trace a complete wiggle**

For `[1,7,4,9,2,5]`, every adjacent difference alternates sign. The states extend on every step, reaching length six, so the full array is already an optimal wiggle subsequence.

#### Complexity detail

The algorithm scans the `n` values once and performs constant work per adjacent pair, giving $O(n)$ time. It stores only two lengths, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Quadratic dynamic programming:** compares every earlier endpoint and uses $O(n^2)$ time plus $O(n)$ storage.
- **Explicitly collect local peaks and valleys:** yields the same greedy result but stores a subsequence when only its length is required.
- **Count raw sign changes without handling equals:** can incorrectly treat zero differences as wiggles.
- A strictly increasing or decreasing array has maximum length two when it has at least two values.
- All-equal values produce length one.
- Equal values between two trends may be skipped without changing the optimum.
- Negative numbers require no special handling because only comparisons matter.

</details>
