# Maximize the Confusion of an Exam

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2024 |
| Difficulty | Medium |
| Topics | String, Binary Search, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) |

## Problem Description

### Goal

An exam answer key is a string whose characters are `T` and `F`. You may
change the answer at any position to either symbol, performing this operation
at most `k` times.

After those changes, find the greatest possible length of a consecutive block
containing only `T` answers or only `F` answers. Changes outside the chosen
block are unnecessary and do not affect its length.

### Function Contract

Let $N$ be the length of `answerKey`.

**Inputs**

- `answerKey`: a string of $N$ characters, each either `T` or `F`, where
  $1 \le N \le 5 \cdot 10^4$.
- `k`: the maximum number of answers that may be changed, where
  $1 \le k \le N$.

**Return value**

- The maximum length of a consecutive equal-answer block achievable with at
  most `k` changes.

### Examples

**Example 1**

- Input: `answerKey = "TTFF", k = 2`
- Output: `4`
- Explanation: Changing both `F` answers produces four consecutive `T`
  answers.

**Example 2**

- Input: `answerKey = "TFFT", k = 1`
- Output: `3`

**Example 3**

- Input: `answerKey = "TTFTTFTT", k = 1`
- Output: `5`
