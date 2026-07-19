# Sum of All Subset XOR Totals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1863 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) |

## Problem Description
### Goal
The XOR total of an array is the bitwise XOR of all its elements; the empty
array has XOR total zero. Given `nums`, consider every subset obtainable by
deleting any selection of its indexed elements and add all of those XOR totals.

Subsets are determined by index choices. Consequently, when equal values occur
at different positions, selections that contain the same values can still be
distinct and must each contribute to the sum. Return the complete subset-XOR
sum.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 12$ and
  $1 \le \texttt{nums}[i] \le 20$.

**Return value**

An integer equal to the sum of the XOR totals of all $2^n$ index subsets,
including the empty subset.

### Examples
**Example 1**

- Input: `nums = [1,3]`
- Output: `6`

The four XOR totals are $0$, $1$, $3$, and $1 \mathbin{\mathtt{XOR}} 3=2$.

**Example 2**

- Input: `nums = [5,1,6]`
- Output: `28`

**Example 3**

- Input: `nums = [3,4,5,6,7,8]`
- Output: `480`
