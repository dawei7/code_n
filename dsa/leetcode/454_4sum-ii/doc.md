# 4Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 454 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/4sum-ii/) |

## Problem Description
### Goal
Given four integer arrays of equal length, choose one index independently from each array. A quadruple `(i, j, k, l)` qualifies when `nums1[i] + nums2[j] + nums3[k] + nums4[l]` equals zero.

Return the number of qualifying index quadruples. Duplicate values at different indices create separate choices, and the same numerical four-value combination may therefore contribute many times. Indices belong to their respective arrays and have no ordering relationship across arrays. The function returns only the count, not the index tuples or distinct value combinations, and must avoid enumerating the full four-dimensional product directly.

### Function Contract
**Inputs**

- `nums1`, `nums2`, `nums3`, `nums4`: integer arrays of the same length

**Return value**

- The number of tuples `(i, j, k, l)` for which `nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0`

### Examples
**Example 1**

- Input: `nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]`
- Output: `2`

**Example 2**

- Input: `nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]`
- Output: `1`

**Example 3**

- Input: `nums1 = [1], nums2 = [1], nums3 = [1], nums4 = [1]`
- Output: `0`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Split the four choices into two independent halves**

For a quadruple to total zero, the sum chosen from the first two arrays must be the negation of the sum chosen from the last two. Enumerating pairs on each side reduces four nested choices to two quadratic stages.

**Store multiplicity, not only membership**

Build a frequency map for every sum $a + b$. Equal values at different indices represent different pairs, so each occurrence increments the map rather than being collapsed into a set. For every $c + d$, add the stored frequency of $-(c + d)$ to the answer.

**Why every tuple is counted exactly once**

Each index quadruple has one unique first-half pair and one unique second-half pair. It contributes once when the second pair queries the complementary sum, while the map frequency accounts for every first pair producing that value. Noncomplementary pairs contribute zero, so the accumulated count is exactly the desired set of tuples.

#### Complexity detail

Each half contains $n^{2}$ index pairs. Building the frequency table and querying all second-half pairs therefore take $O(n^2)$ expected time with a hash table. At most $n^{2}$ distinct sums are stored, giving $O(n^2)$ space.

#### Alternatives and edge cases

- **Store both pair-sum lists and sort:** complementary values can be counted with two pointers in $O(n^2 \log n)$ time and $O(n^2)$ space.
- **Three loops plus a frequency table for the fourth array:** is correct but costs $O(n^3)$ time.
- **Four direct loops:** checks every quadruple in $O(n^4)$ time.
- **Duplicate values:** multiply the number of index choices; never deduplicate an input array or pair sum.
- **No complement:** a missing hash key contributes zero.
- **All zeros:** every one of the `n⁴` index quadruples is valid, so the result may be much larger than $n^{2}$.
- **Negative values:** complement lookup handles signs without a special case.

</details>
