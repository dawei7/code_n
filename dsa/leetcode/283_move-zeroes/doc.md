# Move Zeroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 283 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/move-zeroes/) |

## Problem Description
### Goal
Given a mutable integer array, move every occurrence of zero to the array's end. All nonzero values must remain in the same relative order in which they originally appeared, including duplicates and negative values.

Modify the supplied array in place and return nothing. Preserve its length and complete multiset, filling the positions after the retained nonzero sequence with exactly the original number of zeroes. Do not return or depend on a separate full-size copy. Arrays containing no zeroes, only zeroes, or fewer than two elements already satisfy part or all of the required arrangement.

### Function Contract
**Inputs**

- `nums`: the mutable integer array

**Return value**

Returns `None`; after in-place mutation, nonzero values retain their original order and all remaining positions contain zero.

### Examples
**Example 1**

- Input: `nums = [0,1,0,3,12]`
- Output: `[1,3,12,0,0]`

**Example 2**

- Input: `nums = [0]`
- Output: `[0]`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `[1,2,3]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compact stable nonzero values into the prefix**

Maintain the index where the next nonzero value belongs. Scan the array; whenever a nonzero value appears, swap it into that write position and advance the write index.

Before each scan position, the prefix ending at the write index contains exactly the nonzero values already seen, in their original order. Positions between the write and scan indices are zeros.

**Every swap extends the stable prefix**

Each encountered nonzero is placed at the first position after all earlier nonzeros, so their relative order is preserved. When the scan index differs from the write index, the displaced value is zero and moves into the not-yet-finalized suffix. At completion the prefix contains every nonzero exactly once and all remaining positions contain the original number of zeros.

#### Complexity detail

One pass performs at most one swap per element for $O(n)$ time and uses only two indices.

#### Alternatives and edge cases

- **Shift the suffix for every zero:** preserves order but can take $O(n^2)$.
- Creating a filtered copy violates the in-place space requirement; all-zero and zero-free arrays remain valid.

</details>
