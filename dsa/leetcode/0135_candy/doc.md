# Candy

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 135 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/candy/) |

## Problem Description
### Goal
Children stand in a line, and each child has an integer rating. Assign candies so every child receives at least one. Whenever one child's rating is higher than that of an immediate neighbor, that child must also receive strictly more candies than that neighbor.

Return the smallest possible total number of candies satisfying all comparisons on both sides. Equal ratings impose no ordering requirement, and only adjacent children are compared; a distant higher rating does not directly constrain an assignment. The function reports the minimum total rather than the individual distribution, though every local rise and fall must be respected simultaneously.

### Function Contract
**Inputs**

- `ratings`: child ratings in line order

**Return value**

The minimum total number of candies satisfying both neighbor directions.

### Examples
**Example 1**

- Input: `ratings = [1, 0, 2]`
- Output: `5`

**Example 2**

- Input: `ratings = [1, 2, 2]`
- Output: `4`

**Example 3**

- Input: `ratings = [9]`
- Output: `1`
