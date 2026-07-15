# Advantage Shuffle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 870 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/advantage-shuffle/) |

## Problem Description
### Goal
You are given equal-length integer arrays `nums1` and `nums2`. The advantage of `nums1` over `nums2` is the number of indices `i` for which `nums1[i] > nums2[i]`; equality does not count as a win.

Rearrange all elements of `nums1` into any permutation that maximizes this advantage. Every occurrence from `nums1` must appear exactly once in the result, including duplicates. More than one optimal permutation may exist, and any one of them may be returned.

### Function Contract
**Inputs**

- `nums1`: an integer array of length $n$.
- `nums2`: another integer array of the same length, where $1 \leq n \leq 10^5$ and every value in both arrays lies in $[0,10^9]$.

**Return value**

Return any permutation of `nums1` that maximizes the number of indices satisfying `result[i] > nums2[i]`.

### Examples
**Example 1**

- Input: `nums1 = [2,7,11,15], nums2 = [1,10,4,11]`
- Output: `[2,11,7,15]`

This arrangement wins at all four indices.

**Example 2**

- Input: `nums1 = [12,24,8,32], nums2 = [13,25,32,11]`
- Output: `[24,32,8,12]`

It wins three positions, which is the maximum possible.

**Example 3**

- Input: `nums1 = [2,2,3], nums2 = [1,1,2]`
- Output: `[2,2,3]`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Compare the largest remaining opponent first**

Sort `nums1`. Also sort the pairs `(nums2[i], i)` so each opponent value retains its original result index. Process those pairs from largest value to smallest while maintaining pointers to the smallest and largest unused values from `nums1`.

If the largest remaining `nums1` value is strictly greater than the current opponent, assign it to that opponent and record a win. If it is not greater, no remaining value can win this position. Assign the smallest remaining value as a deliberate loss, preserving every larger value for smaller opponents.

**Why each greedy choice preserves an optimum**

When the largest value cannot beat the largest remaining opponent, every arrangement loses that position; sacrificing the smallest value cannot reduce the attainable win count elsewhere. When the largest value can beat the opponent, an optimal matching can include that win: if the largest value was assigned to a smaller opponent, exchange its assignment with whichever value faced the current opponent. The largest still wins the current position, and the displaced value loses no win that could not be recovered by the exchange.

Thus each processed position makes a choice compatible with some maximum-cardinality set of wins. Restoring assignments to the original `nums2` indices produces a permutation of `nums1` with globally maximum advantage.

#### Complexity detail

Sorting `nums1` and the indexed `nums2` pairs costs $O(n\log n)$ time. The greedy pass is $O(n)$. The sorted values, indexed pairs, and result array each use $O(n)$ space.

#### Alternatives and edge cases

- **Try every permutation:** It directly searches all arrangements but requires factorial time.
- **Find the smallest winner by linear scan:** This greedy rule is correct, yet repeated scans and removals can make the implementation $O(n^2)$.
- **Match equal values as wins:** Advantage requires strict `>`, so ties must be treated as losses.
- **All positions winnable:** Every opponent receives a larger value and the advantage is $n$.
- **No position winnable:** Any permutation is optimal, but the result must still preserve the exact multiset of `nums1`.
- **Duplicate values:** Sorting and pointer movement consume each occurrence separately.
- **Non-unique optimum:** Output order is flexible; correctness depends on the multiset and achieved win count, not equality with one exemplar.

</details>
