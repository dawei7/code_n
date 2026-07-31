# Maximum Number of Operations With the Same Score I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3038 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/) |

## Problem Description
### Goal
You are given an integer array `nums`. One operation removes the first two remaining elements, and the score of that operation is their sum.

Operations may continue while at least two elements remain, but every performed operation must have the same score. Return the maximum number of consecutive front-removal operations that can be performed under this rule. Once the next pair has a different sum, processing stops; a later pair cannot be reached or counted.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: An integer array with $2 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the number of consecutive pairs, beginning with `nums[0]` and `nums[1]`, whose sums equal the score established by that first pair. A final unpaired element is ignored.

### Examples
**Example 1**

- Input: `nums = [3,2,1,4,5]`
- Output: `2`
- Explanation: Removing `[3,2]` and then `[1,4]` gives score `5` both times. Only one element then remains.

**Example 2**

- Input: `nums = [1,5,3,3,4,1,3,2,2,3]`
- Output: `2`
- Explanation: The first two scores are `6`, but the next front pair `[4,1]` scores `5`, so no later pair can be processed.

**Example 3**

- Input: `nums = [5,3]`
- Output: `1`
- Explanation: The only available pair defines the score and produces one operation.
