# Toss Strange Coins

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1230 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/toss-strange-coins/) |

## Problem Description

### Goal

You have `n` independent coins whose probabilities of landing heads are not necessarily equal. For the $i$th coin, `prob[i]` is the probability that its single toss produces heads; consequently, its probability of tails is `1 - prob[i]`.

Toss every coin exactly once. Given an integer `target`, return the probability that exactly `target` of the `n` coins show heads. Coins with probability `0` or `1` are allowed, and the requested count may be zero or may include every coin.

### Function Contract

**Inputs**

- `prob`: A list of $n$ head probabilities, where $1\le n\le1000$ and $0\le\texttt{prob[i]}\le1$.
- `target`: The exact required number of heads $t$, where $0\le t\le n$.

**Return value**

- The probability that exactly `target` coins land heads after all independent tosses.

### Examples

**Example 1**

- Input: `prob = [0.4]`, `target = 1`
- Output: `0.4`

The only coin must land heads.

**Example 2**

- Input: `prob = [0.5,0.5,0.5,0.5,0.5]`, `target = 0`
- Output: `0.03125`

All five fair coins must land tails, which has probability $(1/2)^5$.

**Example 3**

- Input: `prob = [0.5,0.5,0.5]`, `target = 2`
- Output: `0.375`

There are three equally likely choices for which one of the three coins lands tails.
