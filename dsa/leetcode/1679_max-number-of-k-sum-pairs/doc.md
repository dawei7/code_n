# Max Number of K-Sum Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1679 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/) |

## Problem Description
### Goal

Given an integer array `nums` and an integer target `k`, an operation chooses two currently present elements whose values sum to exactly `k` and removes both. Removed elements cannot participate in later operations, while duplicate values are separate elements and may support several different removals.

Return the maximum number of operations that can be performed. The order of the original array does not restrict which elements may be paired, and the specific pairs do not need to be returned. The objective is therefore to form as many disjoint value-complement pairs as the available multiplicities permit.

### Function Contract
**Inputs**

- `nums`: a list of $n$ positive integers, each representing one independently removable element
- `k`: the exact sum required for every removed pair

**Return value**

The maximum number of disjoint pairs from `nums` whose two values sum to `k`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4], k = 5`
- Output: `2`

**Example 2**

- Input: `nums = [3,1,3,4,3], k = 6`
- Output: `1`

**Example 3**

- Input: `nums = [2,2,2,3,1,1,4], k = 4`
- Output: `2`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Store only elements that still need partners**

Scan `nums` once while a frequency map records previously seen elements that have not yet been paired. For the current value `x`, its only possible partner is `k - x`. If the map contains an unmatched copy of that complement, consume one count and increment the operation total. Otherwise, store `x` as unmatched for a future element.

**Immediate matching cannot sacrifice a better choice**

Suppose an unmatched complement is available when `x` arrives. The current `x` cannot form a valid pair with any different value, and that stored complement likewise can pair only with a value equal to `x`. Matching those two now uses one element from each of the only compatible groups. Any optimal solution that leaves them unmatched or pairs either copy with an equivalent duplicate can exchange those choices for this pair without reducing its number of operations.

After each processed prefix, the operation count is maximal for the elements removed so far, and the map contains exactly the unpaired residue of that prefix. This remains valid even when `x = k - x`: the first copy is stored, the second consumes it, and an odd final copy remains unmatched. At the end, the map cannot contain both members of any complementary value classes—such a later arrival would already have consumed the earlier one—so no additional operation is possible. The accumulated count is therefore maximum.

#### Complexity detail

Each of the $n$ values performs a constant expected number of hash-map operations, giving $O(n)$ expected time. At most $n$ unmatched values are represented in the map, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Sort plus two pointers:** sorting enables a deterministic $O(n \log n)$ method with $O(1)$ extra pointer state when mutation is allowed, but it is slower asymptotically than hashing.
- **Search and remove for every element:** repeatedly scanning for a complement is straightforward but can take $O(n^2)$ time and makes index management error-prone.
- **Self-complementary values:** when $2x = k$, the contribution is half the frequency of `x`, rounded down.
- **Unequal complement frequencies:** a value class and its distinct complement can contribute only the smaller of their two counts.
- **Values at least `k`:** because all inputs are positive, such a value has no positive complement unless another legal value makes the exact sum; impossible complements simply remain unmatched.
- **No valid pair:** the correct maximum is zero even though the map may finish with many stored elements.

</details>
