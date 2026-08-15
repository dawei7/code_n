# Find Polygon With the Largest Perimeter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2971 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. You may choose some of its
values as the side lengths of a polygon, which must have at least three sides.

For ordered positive lengths $a_1\le a_2\le\cdots\le a_k$, such a polygon
exists exactly when the longest side is smaller than the sum of every other
side:

$$
a_k < \sum_{i=1}^{k-1} a_i.
$$

The polygon's perimeter is the sum of all its side lengths. Return the largest
perimeter obtainable from a selection of `nums`, or `-1` when no selection can
form a polygon.

### Function Contract

**Inputs**

- `nums`: the available positive integer side lengths

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$3\le N\le10^5$ and $1\le\texttt{nums[i]}\le10^9$.

**Return value**

The greatest sum of a subset containing at least three lengths that satisfies
the polygon inequality, or `-1` if no such subset exists.

### Examples

#### Example 1

- **Input:** `nums = [5,5,5]`
- **Output:** `15`
- **Explanation:** All three equal sides form a polygon with perimeter `15`.

#### Example 2

- **Input:** `nums = [1,12,1,2,5,50,3]`
- **Output:** `12`
- **Explanation:** Sides `1,1,2,3,5` form the maximum-perimeter polygon; neither `12` nor `50` can be supported by the available smaller lengths.

#### Example 3

- **Input:** `nums = [5,5,50]`
- **Output:** `-1`
- **Explanation:** The sum of the two smaller sides is not greater than the longest side.
