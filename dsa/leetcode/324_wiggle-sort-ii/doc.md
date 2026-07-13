# Wiggle Sort II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 324 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Greedy, Sorting, Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/wiggle-sort-ii/) |

## Problem Description
### Goal
Given a mutable integer array, rearrange its existing occurrences into strict wiggle order: `nums[0] < nums[1] > nums[2] < nums[3] > ...`. Every odd position must be strictly greater than both adjacent even positions that exist.

Modify the input in place and return nothing, preserving the complete original multiset including duplicates. A valid arrangement is guaranteed, although careless placement of equal values can violate a strict inequality. Any valid permutation is accepted. Meet the intended linear-time and constant-extra-space target rather than returning a separately sorted array.

### Function Contract
**Inputs**

- `nums`: the mutable integer array to rearrange

**Return value**

No separate value. The input array itself must become a strict wiggle permutation of its original multiset.

### Examples
**Example 1**

- Input: `nums = [1,5,1,1,6,4]`
- Valid result: `[1,6,1,5,1,4]`

**Example 2**

- Input: `nums = [1,3,2,2,3,1]`
- Valid result: `[2,3,1,3,1,2]`

**Example 3**

- Input: `nums = [1,1,2,2,2,1]`
- Valid result: `[1,2,1,2,1,2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Partition values around the median**

Use in-place quickselect to find the median value. The eventual odd positions must receive values greater than the median first, even positions receive values smaller than the median last, and copies equal to the median fill the remaining gaps. A three-way Dutch-national-flag partition can establish exactly those groups in one pass.

Quickselect uses the same three-way partition on the ordinary index range and continues only in the region containing the middle rank. Choosing a median-of-three pivot gives stable practical behavior; its expected running time is linear while retaining constant auxiliary storage.

**Virtual indices visit peaks before valleys**

Ordinary partition order would group large and small values contiguously. Instead, map logical partition position `i` to physical index $(1 + 2 \cdot i) \bmod (n | 1)$. This visits all odd indices first, followed by the even indices in a wraparound order.

Run three-way partitioning through that mapping. Values larger than the median move to the front of virtual order—the physical odd peak positions. Values smaller than the median move to its back—the physical even valley positions. Median copies remain between them and separate repeated extremes.

**The virtual partition implies every strict inequality**

After partitioning, every odd slot is drawn from the high side whenever needed, and every adjacent even slot is drawn from the low or median side. Reversing the effective halves through virtual order prevents equal duplicated values from being placed against each other in the dangerous middle boundary.

Because the problem guarantees that a strict arrangement exists, no value occurs too often to overwhelm all positions of one parity. The high/median/low placement therefore yields `even < odd` on the left of each peak and `odd > even` on its right. Only swaps are performed, so the result preserves the original multiset exactly.

#### Complexity detail

Quickselect takes expected $O(n)$ time, and the virtual-index three-way partition takes $O(n)$ time. Both operate through indices and swaps, using $O(1)$ auxiliary space. A deterministic poor pivot sequence can make this quickselect implementation $O(n^2)$ in the worst case.

#### Alternatives and edge cases

- **Sort and reverse-interleave two halves:** is simpler and correct in $O(n \log n)$ time with $O(n)$ copied storage.
- **Sort and alternate adjacent values directly:** can place equal median copies next to one another and violate strictness.
- **Validate against one expected array:** is incorrect because many different permutations satisfy the contract; validation must check both the multiset and every strict inequality.
- Two elements are valid when ordered low then high. Heavy duplication is the central edge case and is handled by the median group plus virtual indexing.

</details>
