# Duplicate Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1089 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/duplicate-zeros/) |

## Problem Description

### Goal

Given a fixed-length integer array `arr`, duplicate every occurrence of zero and shift the remaining elements to the right. The array length must not change, so values shifted beyond its original final index are discarded and never written.

Perform the modification directly in `arr` and return nothing. Nonzero values retain their relative order, each zero consumes two positions when both fit, and a duplicate that would lie just beyond the fixed boundary is truncated.

### Function Contract

**Inputs**

- `arr`: a mutable array of $n$ integers, where $1 \le n \le 10^4$ and every value is from 0 through 9.

**Return value**

- Returns `None`; after mutation, `arr` equals the first $n$ values of the sequence obtained by replacing every original zero with two zeros.

### Examples

**Example 1**

- Input: `arr = [1, 0, 2, 3, 0, 4, 5, 0]`
- Output: `[1, 0, 0, 2, 3, 0, 0, 4]`

**Example 2**

- Input: `arr = [1, 2, 3]`
- Output: `[1, 2, 3]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count how far values must move:** Scan the portion of the original array that can still contribute after duplication. Count duplicable zeros while shrinking the effective final source boundary by one for each extra zero.

**Handle a zero on the truncation boundary:** If a zero occupies the last source position that can contribute, only its first copy fits. Write that zero at the final array position, move the effective boundary left, and stop counting; treating it as two fitting copies would misalign the backward pass.

**Write backward to avoid overwriting sources:** Starting from the last contributing source index, copy values to their positions offset by the remaining duplicate count. For a zero, write the later copy, decrease the offset, and write the earlier copy. Backward movement guarantees each source value is read before its location can be overwritten.

The counting pass determines exactly how many extra zero positions precede each contributing value. The backward pass places every value at that shifted position, and the boundary case accounts for the sole possible half-duplicated zero. Thus the fixed array becomes precisely the truncated expanded sequence without auxiliary storage.

#### Complexity detail

The forward counting pass and backward writing pass each inspect at most $n$ positions, giving $O(n)$ time. Only indices, a boundary, and the duplicate count are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Insert and truncate for every zero:** It is easy to express but shifts a suffix on every insertion and can take $O(n^2)$ time.
- **Build an expanded copy:** Slicing the first $n$ values is correct but violates the $O(1)$ in-place space requirement.
- **No zeros:** Every value is copied to its current position and the array is unchanged.
- **All zeros:** The array remains all zeros, although the conceptual expansion is twice as long.
- **Zero at the effective boundary:** Only one copy may fit and requires the special forward-pass case.
- **Zero at the original final index:** Its duplicate is discarded beyond the array boundary.

</details>
