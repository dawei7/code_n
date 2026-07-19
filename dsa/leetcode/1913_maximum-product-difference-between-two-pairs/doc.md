# Maximum Product Difference Between Two Pairs

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) |
| Frontend ID | 1913 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The product difference between pairs $(a,b)$ and $(c,d)$ is $ab-cd$. Given a positive integer array `nums`, select four distinct indices `w`, `x`, `y`, and `z`, using `nums[w]` and `nums[x]` for the product that is added and `nums[y]` and `nums[z]` for the product that is subtracted.

Maximize this difference and return its value. Equal values at different indices remain distinct selectable elements, but no single array position may be used in both pairs.

### Function Contract

**Inputs**

- `nums`: a list of $N$ positive integers.
- $4 \le N \le 10^4$.
- $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the maximum value of `nums[w] * nums[x] - nums[y] * nums[z]` over four distinct indices.

### Examples

**Example 1**

- Input: `nums = [5,6,2,7,4]`
- Output: `34`

The two largest values give `6 * 7`, and the two smallest remaining values give `2 * 4`.

**Example 2**

- Input: `nums = [4,2,5,9,7,4,8]`
- Output: `64`

The maximum is `9 * 8 - 2 * 4 = 64`.

**Example 3**

- Input: `nums = [1,2,3,4]`
- Output: `10`

All four values are used: `4 * 3 - 1 * 2 = 10`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the choice to four extrema**

Because every value is positive, increasing either factor in the added product can only improve the result. Its best possible factors are therefore the largest and second-largest array elements. Likewise, decreasing either factor in the subtracted product improves the result, so that product uses the smallest and second-smallest elements.

These four order statistics correspond to four distinct positions. If values are equal, sequential tracking still records two separate occurrences, which satisfies the distinct-index requirement.

**Track the extrema in one pass**

Maintain two slots for the smallest values and two for the largest values. A new value that reaches the first slot shifts its former occupant into the second slot; otherwise it may replace only the second slot. Use inclusive comparisons for the first slots so duplicate extrema occupy both positions when they occur twice.

After the scan, return `largest * second_largest - smallest * second_smallest`. Every alternative added product is no larger, and every alternative subtracted product is no smaller, so no other four-index selection can produce a greater difference.

#### Complexity detail

The algorithm examines each of the $N$ values once and performs constant work per value, giving $O(N)$ time. The four tracked extrema use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sort the array:** Sorting and using the first two and last two values is concise, but takes $O(N\log N)$ time and may use nonconstant auxiliary space.
- **Selection sort:** It also exposes the needed endpoints but takes $O(N^2)$ comparisons.
- **Exactly four elements:** All positions must be used, although their assignment to the two products remains determined by the extrema.
- **Duplicate extrema:** Two equal minimum or maximum values at different indices are both valid factors.
- **All values equal:** The two products are equal, so the answer is zero.
- **Domain extremes:** Products fit the required result range, but implementations in fixed-width languages should still use an adequately wide numeric type.

</details>
