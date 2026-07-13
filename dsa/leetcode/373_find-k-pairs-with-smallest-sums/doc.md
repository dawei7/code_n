# Find K Pairs with Smallest Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 373 |
| Difficulty | Medium |
| Topics | Array, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) |

## Problem Description
### Goal
Given two integer arrays `nums1` and `nums2` sorted in non-decreasing order, every cross-array index pair `(i, j)` produces the value pair `[nums1[i], nums2[j]]` with sum `nums1[i] + nums2[j]`. Select the globally smallest such pair sums.

Return exactly `k` value pairs because the input guarantees `1 <= k <= len(nums1) * len(nums2)`. Distinct index pairs remain separate candidates even when duplicate values make their outputs equal. Return the pairs in any order; any tied choices at the final cutoff are acceptable. Avoid generating and sorting the full Cartesian product when only a small prefix is requested.

### Function Contract
**Inputs**

- `nums1`: a nondecreasing integer list
- `nums2`: a nondecreasing integer list
- `k`: the maximum number of pairs to return

**Return value**

- Any collection of `min(k, len(nums1) * len(nums2))` value pairs having globally smallest sums. Pair order and choices tied at the cutoff may vary.

### Examples
**Example 1**

- Input: `nums1 = [1,7,11], nums2 = [2,4,6], k = 3`
- Output: `[[1,2],[1,4],[1,6]]`

**Example 2**

- Input: `nums1 = [1,1,2], nums2 = [1,2,3], k = 2`
- Output: `[[1,1],[1,1]]`

**Example 3**

- Input: `nums1 = [1,2], nums2 = [3], k = 3`
- Output: `[[1,3],[2,3]]`

### Required Complexity

- **Time:** $O(k \log \min(k,m))$
- **Space:** $O(\min(k,m))$

<details>
<summary>Approach</summary>

#### General

**View all pair sums as sorted rows**

For each index `i` in `nums1`, pairing `nums1[i]` with successive values of sorted `nums2` forms a nondecreasing row of sums. The full Cartesian product is therefore a collection of sorted rows, and the task asks for the first `k` values in their merged order.

Only the first `min(k, len(nums1))` rows can matter: before any later row's first pair is needed, there are already at least $k$ row-start pairs with no larger first-array values.

**Merge row fronts with a min-heap**

Seed the heap with pair `(i,0)` from each relevant row, keyed by its sum. Repeatedly remove the smallest heap entry and output its two values. If that row has another column, push `(i,j+1)`. Stop after `k` removals or when the heap is empty.

**Why every popped pair is globally next**

The heap contains the smallest not-yet-output pair from every active row. Any later pair in a row is no smaller than that row's front, so none can precede the minimum heap entry. After popping one front, advancing only its row restores this condition. Induction proves that the heap emits pair sums in global nondecreasing order, including duplicate index pairs with equal values.

**Handle ties as semantic choices**

Several index pairs can share the cutoff sum. Any selection of the required multiplicity at or below that threshold is valid. Validation therefore checks available value-pair multiplicities and the k-th sum threshold rather than enforcing one heap tie order.

#### Complexity detail

Let `m = len(nums1)` and $h = \min(k,m)$. Heap initialization uses $O(h)$ entries. At most `k` pop/push steps each cost $O(\log h)$, for $O(k \log \min(k,m))$ time after constant-time array access. The heap uses $O(\min(k,m))$ auxiliary space, while the returned pairs are output space.

#### Alternatives and edge cases

- **Generate and sort every pair:** costs $O(mn \log(mn))$ time and $O(mn)$ space even when `k` is small.
- **Binary-search a sum threshold:** can count qualifying pairs efficiently, but reconstructing exactly `k` pairs around ties adds complexity.
- **Seed one heap row per second-array value:** is symmetric and may be preferable when `nums2` is shorter.
- Empty input arrays produce no pairs.
- If `k` exceeds the Cartesian-product size, every index pair is returned.
- Duplicate values represent distinct index combinations and must retain their available multiplicity.
- Negative values and tied sums require no special heap logic.

</details>
