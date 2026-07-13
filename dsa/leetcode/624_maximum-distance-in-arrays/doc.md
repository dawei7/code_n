# Maximum Distance in Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 624 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-distance-in-arrays/) |

## Problem Description
### Goal
You are given at least two integer arrays, each sorted in ascending order. Choose one integer from one array and a second integer from a different array; the two selected values may not come from the same input array.

Define the distance between integers `a` and `b` as their absolute difference $| a - b |$. Return the maximum distance obtainable from any valid choice of two arrays and values. The arrays may contain negative values, duplicate values, or only one element.

### Function Contract
**Inputs**

- `arrays`: at least two nonempty integer arrays, each sorted in ascending order

**Return value**

- The maximum absolute difference between values selected from different input arrays

### Examples
**Example 1**

- Input: `arrays = [[1,2,3],[4,5],[1,2,3]]`
- Output: `4`

**Example 2**

- Input: `arrays = [[1],[1]]`
- Output: `0`

### Required Complexity

- **Time:** $O(M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only endpoints can be globally extreme**

Because each array is sorted, its first value is its minimum and its last value is its maximum. Any largest cross-array absolute difference must pair one array's minimum with another array's maximum; interior values cannot improve either endpoint.

**Keep extremes from earlier arrays**

Initialize `minimum` and `maximum` from the first array. For each later array, compare its maximum with the earlier minimum and compare its minimum with the earlier maximum. These two candidates cover both possible orientations of a cross-array extreme.

**Compare before updating**

Only after evaluating both candidates should the current endpoints extend the running `minimum` and `maximum`. This ordering guarantees that every candidate uses the current array on one side and a strictly earlier array on the other, so the forbidden same-array pair is never considered.

**Why one pass covers the optimum**

Take an optimal pair and consider whichever of its two arrays is processed later. When that later array is scanned, the earlier array's relevant endpoint is already represented by the running extreme. The algorithm evaluates a candidate at least as large as that optimal pair, while every evaluated candidate is legal, so the recorded maximum is exact.

#### Complexity detail

Let `M` be the number of arrays. Reading two endpoints and performing constant work per array takes $O(M)$ time, independent of the total number of interior elements. The running extrema and answer use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Compare every pair of arrays:** evaluate their endpoint combinations directly; it is correct but costs $O(M^2)$ time.
- **Track the two global minima and maxima with source indices:** also solves the different-array restriction, but requires more state and tie handling than the streaming comparison.
- **Flatten and sort all values:** loses source identity unless every value retains its array index and also processes irrelevant interior values.
- The global minimum and maximum may belong to the same array; comparing before updating prevents using that illegal distance.
- Single-element arrays have the same minimum and maximum and need no special handling.
- Equal values across all arrays produce distance zero.
- Negative values work unchanged because the two directed endpoint differences are nonnegative candidates.

</details>
