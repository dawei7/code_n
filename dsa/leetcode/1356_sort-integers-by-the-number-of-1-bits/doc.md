# Sort Integers by The Number of 1 Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1356 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) |

## Problem Description

### Goal

You are given an array `arr` of nonnegative integers. Sort its values in ascending order according to the number of `1` bits in each value's binary representation.

When two values contain the same number of `1` bits, place the numerically smaller value first. Preserve duplicate occurrences and return the fully ordered array. Thus the primary key is population count and the secondary key is the integer itself.

### Function Contract

**Inputs**

- `arr`: a nonempty array of nonnegative integers.
- Let $n$ be its length.

**Return value**

- Return all input values sorted by ascending bit count, breaking ties by ascending numeric value.

### Examples

**Example 1**

- Input: `arr = [0,1,2,3,4,5,6,7,8]`
- Output: `[0,1,2,4,8,3,5,6,7]`

**Example 2**

- Input: `arr = [1024,512,256,128,64,32,16,8,4,2,1]`
- Output: `[1,2,4,8,16,32,64,128,256,512,1024]`

**Example 3**

- Input: `arr = [2,2,1]`
- Output: `[1,2,2]`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Express both ordering rules in one key.** For each value, compute the number of set bits in its binary representation. Associate the tuple `(value.bit_count(), value)` with that element. Tuple comparison first orders by population count and uses the original integer only when the counts tie, exactly matching the contract.

Apply a comparison sort with this key. Every pair of output elements is then in the required order: a smaller bit count comes first, and equal counts are numerically ascending. Since every input occurrence participates independently in sorting, duplicates are preserved.

#### Complexity detail

Sorting $n$ bounded integers takes $O(n \log n)$ key comparisons. Population count is constant time for the problem's bounded integer range and is evaluated once per element by the key-based sort. Returning a separate ordered list uses $O(n)$ space, including the sorting buffer and output.

#### Alternatives and edge cases

- **Selection sort by the same key:** This is correct but performs $O(n^2)$ comparisons.
- **Bucket by bit count:** The bounded integer range permits bit-count buckets followed by numeric sorting inside each bucket, but the total sorting bound remains $O(n \log n)$ in the general case.
- **Zero:** Its binary representation has no set bits, so it precedes every positive value.
- **Equal bit counts:** Numeric order, not original position, decides the result.
- **Duplicates:** Equal values have identical keys and every occurrence remains in the output.

</details>
