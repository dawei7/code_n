# Number of Ways Where Square of Number Is Equal to Product of Two Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1577 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) |

## Problem Description
### Goal

Given two integer arrays, `nums1` and `nums2`, count index triplets of two symmetric types. A type-1 triplet selects one index `i` from `nums1` and two ordered-by-index positions `j < k` from `nums2` such that the square of `nums1[i]` equals `nums2[j] * nums2[k]`.

A type-2 triplet reverses the arrays: it selects one index `i` from `nums2` and positions `j < k` from `nums1`, requiring the square of `nums2[i]` to equal `nums1[j] * nums1[k]`.

Return the total number of type-1 and type-2 triplets. Indices define the triplets, so equal values at different positions contribute separately, while each unordered pair inside one array is counted once through the condition $j<k$.

### Function Contract
**Inputs**

- `nums1`: An integer array of length $N$, where $1 \le N \le 100$.
- `nums2`: An integer array of length $M$, where $1 \le M \le 100$.
- Every array value is between $1$ and $10^5$, inclusive.

**Return value**

Return the total number of valid index triplets of both types.

### Examples
**Example 1**

- Input: `nums1 = [7, 4], nums2 = [5, 2, 8, 9]`
- Output: `1`

**Example 2**

- Input: `nums1 = [1, 1], nums2 = [1, 1, 1]`
- Output: `9`

**Example 3**

- Input: `nums1 = [7, 7, 8, 3], nums2 = [1, 2, 9, 7]`
- Output: `2`

### Required Complexity

- **Time:** $O(N^2 + M^2)$
- **Space:** $O(N^2 + M^2)$

<details>
<summary>Approach</summary>

#### General

**Aggregate every unordered pair product**

For one array, enumerate every index pair `left < right` and store the frequency of `values[left] * values[right]` in a hash table. Repeated products must increase the frequency because they correspond to distinct index pairs.

Build this product-frequency table for both arrays. The table for `nums2` describes every possible paired side of a type-1 triplet, while the table for `nums1` serves type 2.

**Match each squared position against the opposite table**

For every value in `nums1`, look up `value * value` in the pair-product table for `nums2`. Its frequency is exactly the number of choices for `j < k` that combine with that particular `nums1` index. Sum those frequencies, then repeat with the arrays reversed.

Every valid triplet has one singled-out squared index and one unique unordered pair of indices in the other array, so it appears in exactly one lookup contribution. Conversely, a product-frequency match satisfies the required equality and represents that many distinct index pairs. Adding both directions therefore counts every valid triplet once.

#### Complexity detail

Enumerating all pairs costs $O(N^2)$ for `nums1` and $O(M^2)$ for `nums2`. The subsequent square lookups take $O(N+M)$ expected time, so the total is $O(N^2+M^2)$.

In the worst case, every pair can produce a distinct hash-table key. The two product maps therefore use $O(N^2+M^2)$ space.

#### Alternatives and edge cases

- **Count square frequencies first:** store squared-value counts, then enumerate opposite-array pairs and add matching square frequencies. This has the same time bound and can use only $O(N+M)$ frequency space.
- **Sort with two pointers:** for each squared value, a sorted opposite array can count factor pairs in linear time, but repeating that search for every value can reach cubic time without further aggregation.
- **Enumerate every triplet:** directly test each singled-out index against every opposite pair. It is correct but takes $O(NM^2+MN^2)$ time.
- **Array of length one:** that array supplies no pair, although its sole value may still be the squared side of a triplet.
- **Duplicate values:** equal values at different indices create distinct singles and pairs; frequency multiplication must preserve that multiplicity.
- **Matches in both directions:** type-1 and type-2 counts are independent and must be added.
- **Large values:** products and squares can reach $10^{10}$, so fixed-width implementations need a sufficiently wide integer type.
- **No matching products:** all hash lookups return zero, producing answer zero.

</details>
