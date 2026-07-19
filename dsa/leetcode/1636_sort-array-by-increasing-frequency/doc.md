# Sort Array by Increasing Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1636 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-array-by-increasing-frequency/) |

## Problem Description
### Goal
Given an integer array `nums`, reorder all of its elements according to the frequency of their values. A value that occurs fewer times must appear before every value that occurs more often. When two distinct values have the same frequency, the larger value must appear first.

Return the completely reordered array. Equal values remain together because every copy receives the same frequency and value-based ordering keys.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 100$ and $-100 \le \texttt{nums[i]} \le 100$.

**Return value**

Return an array containing exactly the input elements, ordered first by increasing frequency and then, for equal frequencies, by decreasing numeric value.

### Examples
**Example 1**

- Input: `nums = [1,1,2,2,2,3]`
- Output: `[3,1,1,2,2,2]`

The values 3, 1, and 2 occur one, two, and three times respectively.

**Example 2**

- Input: `nums = [2,3,1,3,2]`
- Output: `[1,3,3,2,2]`

Values 2 and 3 both occur twice, so the larger value 3 precedes 2.

**Example 3**

- Input: `nums = [-1,1,-6,4,5,-6,1,4,1]`
- Output: `[5,-1,4,4,-6,-6,1,1,1]`
