# Maximum Number of Pairs in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2341 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-pairs-in-array/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, repeatedly choose two equal values,
remove both of them, and count that removal as one pair. Continue until no two
remaining integers are equal. The order in which equal pairs are removed does
not affect the final counts.

Return a two-element array. Its first value is the maximum number of pairs
formed by exhausting this operation, and its second value is the number of
integers left after all possible pairs have been removed.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 100$ and every
  value lies in $[0,100]$.

**Return value**

`[pairs, leftovers]`, where `pairs` is the number of removed equal-value pairs
and `leftovers` is the number of unpaired integers.

### Examples

#### Example 1

- **Input:** `nums = [1,3,2,1,3,2,2]`
- **Output:** `[3,1]`
- **Explanation:** One pair is removed for each of values 1, 2, and 3, leaving one
  additional 2.

#### Example 2

- **Input:** `nums = [1,1]`
- **Output:** `[1,0]`
- **Explanation:** The two equal values form one pair and nothing remains.

#### Example 3

- **Input:** `nums = [0]`
- **Output:** `[0,1]`
- **Explanation:** A single value cannot form a pair.
