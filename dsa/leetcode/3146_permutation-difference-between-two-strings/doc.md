# Permutation Difference between Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3146 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/permutation-difference-between-two-strings/) |

## Problem Description
### Goal
You are given two lowercase strings `s` and `t`. Every character occurs at most once in `s`, and `t` is a permutation of `s`, so both strings contain exactly the same distinct characters.

For each character, compare its zero-based position in `s` with its position in `t`. The permutation difference is the sum of the absolute values of all those position changes. Return that total over every character in the strings.

### Function Contract
**Inputs**

- `s`: A string of distinct lowercase English letters.
- `t`: A permutation of `s`.

Let $n = \lvert\texttt{s}\rvert = \lvert\texttt{t}\rvert$. The constraint is $1 \le n \le 26$.

**Return value**

Return the sum, over every character, of the absolute difference between its index in `s` and its index in `t`.

### Examples
**Example 1**

- Input: `s = "abc", t = "bac"`
- Output: `2`
- Explanation: Characters `a` and `b` each move one position, while `c` does not move, giving $1+1+0=2$.

**Example 2**

- Input: `s = "abcde", t = "edbac"`
- Output: `12`
- Explanation: The five absolute index differences are $3$, $1$, $2$, $2$, and $4$, whose sum is $12$.
