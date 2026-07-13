# Partition Equal Subset Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 416 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) |

## Problem Description
### Goal
Given a nonempty array of positive integers, divide its element occurrences into two disjoint subsets. Every array position must belong to exactly one subset, and duplicate values at different positions remain separate selectable occurrences.

Return `True` when the two subset sums can be equal and `False` otherwise. This is equivalent to finding one subset totaling half the complete array sum, which is impossible when that total is odd. Subsets do not need to correspond to contiguous positions or have equal cardinality. The function returns only feasibility, not the two partitions themselves.

### Function Contract
**Inputs**

- `nums`: a nonempty array of positive integers

**Return value**

- Return `True` when some subset sums to half of the array total; otherwise return `False`.

### Examples
**Example 1**

- Input: `nums = [1,5,11,5]`
- Output: `True`

**Example 2**

- Input: `nums = [1,2,3,5]`
- Output: `False`

**Example 3**

- Input: `nums = [2,2,1,1]`
- Output: `True`

### Required Complexity

- **Time:** $O(nT)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Reduce equal partitioning to one target sum**

If the total is odd, two integer subset sums cannot be equal. Otherwise let `T = total / 2`. Choosing any subset with sum `T` automatically leaves all remaining elements with the same sum.

**Encode reachable sums as bits**

Use an integer whose bit `s` is one exactly when sum `s` is reachable. Initially only sum zero is reachable, so the bitset is `1`. For value `x`, shifting left by `x` maps every old reachable sum `s` to $s + x$; OR it with the old bitset to represent excluding or including the value.

**Why each value is used at most once**

Compute the shift from the pre-update bitset and combine it in one assignment. New sums created by the current value cannot feed another shift during that same iteration, matching the zero-or-one choice for each array element.

**Read the target decision**

After all values, bit `T` is set exactly when some subset choices total `T`. This follows inductively because each update enumerates both possibilities for the newest value over every subset of the processed prefix.

#### Complexity detail

The language-neutral Boolean dynamic program has `n` updates across sums through `T`, taking $O(nT)$ time and $O(T)$ space. Python's packed integer performs each row as word-level shift and OR operations while preserving the same state semantics.

#### Alternatives and edge cases

- **Descending Boolean array:** updates sums from `T` down to each value and has the stated $O(nT)$ time and $O(T)$ space.
- **Memoized include-or-exclude search:** visits at most $O(nT)$ index-and-sum states but adds recursion and hash overhead.
- **Uncached subset enumeration:** can explore $O(2^n)$ choices.
- An odd total is immediately impossible.
- One element alone cannot form two equal positive-sum subsets.
- Duplicate values are separate selectable elements.
- A value greater than `T` cannot belong to the target subset, though the bitset update remains safe.

</details>
