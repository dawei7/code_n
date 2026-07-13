# Split Array With Same Average

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 805 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-with-same-average/) |

## Problem Description

### Goal

Given an integer array `nums`, move every element into exactly one of two arrays `A` and `B`. Both groups must be nonempty, but they do not need to be contiguous and their internal order does not matter.

Return `True` if the partition can make $\operatorname{avg}(A) = \operatorname{avg}(B)$, and `False` otherwise. Each occurrence is assigned once even when values repeat, and an average is the group's sum divided by its number of elements.

### Function Contract

**Inputs**

- `nums`: a nonempty list of nonnegative integers.

**Return value**

- `True` if some nonempty proper subset has the same average as its complement; otherwise, `False`.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4,5,6,7,8]`
- Output: `True`
- Explanation: `[1,8]` and the remaining six values both have average `4.5`.

**Example 2**

- Input: `nums = [3,1]`
- Output: `False`
- Explanation: The only split produces singleton averages `3` and `1`.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `True`
- Explanation: The subset `[2]` and its complement `[1,3]` both average `2`.

### Required Complexity

- **Time:** $O(2^{n/2})$
- **Space:** $O(2^{n/2})$

<details>
<summary>Approach</summary>

#### General

**Turn equal averages into a zero sum**

Let `T` be the total and `n` the length. A subset of size `k` and sum `S` has the full-array average exactly when $S \cdot n = T \cdot k$. Replace each value `x` by $n \cdot x - T$; the transformed sum of that subset is then $n \cdot S - T \cdot k$, so the required condition becomes an exact zero-sum test with integers.

Before enumeration, check whether any size `1` through $\lfloor n/2 \rfloor$ can satisfy $T \cdot k$ divisible by `n`. If none can, neither that size nor its complementary size can work.

**Meet in the middle**

Split the transformed values into two halves and enumerate every subset sum within each half. A nonempty zero-sum subset contained in either half is immediately valid. Otherwise, for every nonempty right-half subset sum `s`, look for `-s` among nonempty left-half sums.

The one forbidden combination is choosing both complete halves, because that selects the entire array and always sums to zero. When the right subset is full, consult only sums made by non-full left subsets. Every accepted combination is therefore nonempty and proper, and every valid subset decomposes into exactly one left and one right choice that the search examines.

#### Complexity detail

Each half contains at most $\left\lceil n / 2 \right\rceil$ values, so enumerating and storing its subset sums takes $O(2^{n/2})$ time and space up to ceiling factors. Hash lookups combine complementary sums in expected constant time per right subset.

#### Alternatives and edge cases

- **Subset-sum DP by cardinality:** Track reachable sums for each chosen size and test $T \cdot k / n$; this is effective for bounded sums but has pseudo-polynomial dependence on the values.
- **Enumerate every subset:** Directly test all $2^{n}$ masks and exclude empty/full selections; it repeats work that meet-in-the-middle removes.
- **Floating-point averages:** Comparing division results risks precision errors; cross multiplication or the integer transformation is exact.
- **Single element:** No split into two nonempty groups exists.
- **All values equal:** Any nonempty proper subset works.
- **Complement symmetry:** It is sufficient to consider candidate sizes up to $\lfloor n/2 \rfloor$ in the divisibility check.
- **Whole-array zero sum:** The transformed total is always zero, so the full subset must be excluded explicitly.

</details>
