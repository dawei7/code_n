# Range Addition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 370 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/range-addition/) |

## Problem Description
### Goal
Begin with an integer array of the requested `length`, initialized entirely to zero. Each update `[start, end, increment]` adds `increment` to every position from `start` through `end`, including both endpoints.

Apply all updates cumulatively and return the final array. Ranges may overlap, increments may be positive or negative, and an index receives the sum of every update covering it. Updates do not overwrite earlier values, and no per-update output is needed. With no updates, return the requested number of zeroes unchanged. Meet the linear aggregate target rather than visiting every index in every range separately.

### Function Contract
**Inputs**

- `length`: the non-negative length of the result array
- `updates`: a list of triples `[start, end, increment]` describing inclusive index ranges

**Return value**

- The length-`length` array after all additions have been accumulated.

### Examples
**Example 1**

- Input: `length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]`
- Output: `[-2,0,3,5,3]`

**Example 2**

- Input: `length = 3, updates = [[0,2,1]]`
- Output: `[1,1,1]`

**Example 3**

- Input: `length = 1, updates = []`
- Output: `[0]`

### Required Complexity

- **Time:** $O(length + q)$
- **Space:** $O(length)$

<details>
<summary>Approach</summary>

#### General

**Record where an update starts and stops affecting values**

Instead of touching every element in an updated range, maintain a difference array. For update `[start,end,increment]`, add `increment` at `start`. This means the running total should increase beginning there. If `end + 1` is inside the array, subtract the same increment there so its effect stops immediately after the inclusive range.

Each update now changes at most two positions regardless of its width.

**Recover final values with one prefix scan**

Walk left to right while maintaining the running sum of difference entries. At index `i`, that sum contains exactly the increments whose starts are at or before `i` and whose stopping markers are after `i`. Store it as the final value at that index.

**Why overlapping ranges combine correctly**

Difference markers are additive. Every update contributes one positive boundary and, when needed, one matching negative boundary. Prefix summation includes that contribution precisely on its intended interval. Adding markers for multiple updates superimposes their effects, including positive and negative increments, so the reconstructed value equals the sum of all updates covering each index.

**Trace the first example**

The three updates place boundary changes at their starts and just after their ends. Accumulating those changes across five positions yields running totals `-2, 0, 3, 5, 3`, which are the required final entries.

#### Complexity detail

Let `q` be the number of updates. Writing two boundary markers per update takes $O(q)$ time, and the final prefix scan takes $O(length)$, for $O(length + q)$ total. The difference/result array uses $O(length)$ space.

#### Alternatives and edge cases

- **Modify every covered element:** is simple but can take $O(length \cdot q)$ time for wide overlapping updates.
- **Segment tree with lazy propagation:** supports interleaved range updates and queries, but is unnecessary when only the final array is requested.
- **Event map of boundaries:** can be useful for an enormous sparse coordinate domain, but this problem requires every output position.
- An update ending at the final index has no in-bounds stopping marker.
- Negative increments combine through the same boundary arithmetic.
- An empty update list leaves every entry zero.
- A one-element range adds only to its single index.

</details>
