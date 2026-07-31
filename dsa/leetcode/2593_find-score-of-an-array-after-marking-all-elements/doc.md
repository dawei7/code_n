# Find Score of an Array After Marking All Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2593 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers and begin with a score of zero. Repeatedly choose the smallest value whose position has not yet been marked. When several unmarked positions contain that value, the smallest index must be chosen.

Add the chosen value to the score, then mark its position and each immediately adjacent position that exists. A marked position can never be selected later, although marking it again has no additional effect.

Continue until every position is marked, and return the resulting score.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \leq n \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^6$.

**Return value**

- The score obtained by following the required value-first, index-first selection process until all positions are marked.

### Examples

**Example 1**

- Input: `nums = [2,1,3,4,5,2]`
- Output: `7`

Choose the values `1`, `2`, and `4` in that order. Their sum is `7`; each choice also marks its existing neighbors.

**Example 2**

- Input: `nums = [2,3,5,1,3,2]`
- Output: `5`

After choosing `1` at index `3`, the equal unmarked values `2` are processed by increasing index, so indices `0` and `5` both contribute.
