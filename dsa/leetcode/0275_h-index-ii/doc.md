# H-Index II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 275 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/h-index-ii/) |

## Problem Description
### Goal
Given nonnegative citation counts already sorted in ascending order, compute the researcher's h-index. A value `h` is valid when at least `h` papers have citation counts greater than or equal to `h`.

Return the largest valid `h`, bounded by the number of papers rather than by the largest citation count. Use the supplied sorted order to meet the required logarithmic running time, locating the boundary where the number of remaining papers can be supported by their citation values. For one paper, the result is `1` when it has at least one citation and `0` otherwise; duplicate citation counts occupy separate paper positions.

### Function Contract
**Inputs**

- `citations`: sorted nonnegative citation counts

**Return value**

The largest `h` for which at least `h` papers have at least `h` citations.

### Examples
**Example 1**

- Input: `citations = [0,1,3,5,6]`
- Output: `3`

**Example 2**

- Input: `citations = [1,2,100]`
- Output: `2`

**Example 3**

- Input: `citations = []`
- Output: `0`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Feasibility becomes monotone in sorted order**

At sorted index `i`, exactly $n - i$ papers lie at or above `citations[i]`. The index is feasible when `citations[i] >= n - i`; feasibility remains true for every index to its right.

Binary search keeps every possible first feasible index in `[left, right]`. A feasible midpoint moves the right boundary left to seek an earlier one; an infeasible midpoint discards itself and every earlier index.

**The boundary converts directly into the h-index**

Binary search locates the first index `left` satisfying `citations[left] >= n - left`. The suffix then contains `n - left` papers, each with at least that many citations. If a preceding index exists, its failure proves the larger candidate associated with that longer suffix is impossible. Therefore `n - left` is exactly maximal.

#### Complexity detail

The search interval halves each iteration for $O(\log n)$ time. Two boundaries and a midpoint use $O(1)$ space.

#### Alternatives and edge cases

- **Linear scan:** ignores the sorted-input advantage and takes $O(n)$.
- Empty input returns zero; an h-index may equal the complete paper count.

</details>
