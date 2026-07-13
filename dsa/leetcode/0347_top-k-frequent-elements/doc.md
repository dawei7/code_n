# Top K Frequent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 347 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort, Counting, Quickselect |
| Official Link | [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) |

## Problem Description
### Goal
Given a nonempty integer array and a valid count `k`, measure the occurrence frequency of every distinct value. Select exactly the `k` values having the greatest frequencies, with the input guarantee ensuring a unique qualifying set at the cutoff.

Return those distinct values in any order, listing each once regardless of its source count. Negative values and zero participate normally, and duplicate occurrences affect frequency rather than output multiplicity. Meet the required complexity better than sorting all input occurrences or all distinct values by frequency. The function returns the values themselves, not their counts.

### Function Contract
**Inputs**

- `nums`: a non-empty list of integers
- `k`: the number of most-frequent distinct values to return

**Return value**

- A list containing exactly the `k` values with the greatest occurrence counts, in any order.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 2, 2, 3], k = 2`
- Output: `[1, 2]`

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `[1]`

**Example 3**

- Input: `nums = [4, 4, 4, 4, 2, 2, 2, 3], k = 2`
- Output: `[4, 2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Use frequencies as bucket indices**

Sorting values by frequency would organize more information than the answer needs and costs $O(u \log u)$ for `u` distinct values. Frequencies have a small integer range that makes bucket grouping linear: no value can occur fewer than once or more than `n` times.

First count every value with a hash map. Create $n + 1$ buckets, where bucket index `f` stores all values whose frequency is `f`. Place each distinct value into the bucket selected by its count, then scan bucket indices from `n` downward. Append values encountered until exactly `k` have been collected.

**Why the first k emitted values are correct**

After counting, the map contains the exact frequency of every distinct value. Bucket placement preserves that information because a value goes into precisely the bucket equal to its count. During the descending scan, every value emitted before another has frequency at least as large. Therefore the first `k` emitted values form the required top-frequency set; the uniqueness guarantee ensures no ambiguous boundary can require choosing among equally frequent values.

**Trace the occupied buckets**

For `[1, 1, 1, 2, 2, 3]`, the buckets at indices `3`, `2`, and `1` contain `1`, `2`, and `3`. Scanning downward returns `1` and `2` and stops.

#### Complexity detail

Counting visits `n` input positions. Placing `u` distinct values and scanning the $n + 1$ bucket array take $O(u + n)$, so total time is $O(n)$. The frequency map, buckets, and result together use $O(n)$ space in the worst case.

#### Alternatives and edge cases

- **Sort distinct values by frequency:** takes $O(n + u \log u)$ time for `u` distinct values.
- **Size-k min-heap:** takes $O(n + u \log k)$ and may use less selection storage when `k` is small, but misses the required worst-case linear bound.
- **Quickselect:** offers expected $O(n)$ time but needs delicate partitioning and can degrade to quadratic time without stronger pivot guarantees.
- Negative values and zero are ordinary hash keys.
- When `k` equals the number of distinct values, every distinct value must be returned.
- Output order is irrelevant, but the result cannot contain duplicates because the buckets store map keys rather than input occurrences.

</details>
