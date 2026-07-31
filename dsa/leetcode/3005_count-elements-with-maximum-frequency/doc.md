# Count Elements With Maximum Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3005 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-elements-with-maximum-frequency/) |

## Problem Description
### Goal
You are given an array `nums` of positive integers. The frequency of a value
is its number of occurrences in the array.

Find the greatest frequency attained by any value. Return the sum of the
frequencies of every value that attains that maximum. Equivalently, count all
array positions whose value belongs to a maximum-frequency group.

When several distinct values tie for the greatest frequency, include every
occurrence of every tied value. Values with any smaller frequency contribute
nothing to the returned total.

### Function Contract
**Inputs**

- `nums`: the nonempty positive-integer array

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $1\le N\le100$
and $1\le\texttt{nums[i]}\le100$.

**Return value**

Return the total number of occurrences contributed by all values tied for the
maximum frequency.

### Examples
**Example 1**

- Input: `nums = [1,2,2,3,1,4]`
- Output: `4`

Values 1 and 2 each occur twice, so together their maximum-frequency groups
contain four elements.

**Example 2**

- Input: `nums = [1,2,3,4,5]`
- Output: `5`

Every value occurs once and therefore every array element belongs to a tied
maximum-frequency group.
