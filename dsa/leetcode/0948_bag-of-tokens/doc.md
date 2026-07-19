# Bag of Tokens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 948 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/bag-of-tokens/) |

## Problem Description

### Goal

You begin with the given amount of `power`, a score of zero, and a bag of unplayed tokens whose integer values are listed in `tokens`. Each token may be played at most once, in exactly one of two orientations.

Playing a token face-up is allowed when the current power is at least its value; this spends that much power and gains one score. Playing a token face-down is allowed when the current score is at least one; this gains power equal to the token's value and loses one score. You may stop after any number of plays. Return the maximum score that can be reached at any point.

### Function Contract

Let $n$ be the number of tokens.

**Inputs**

- `tokens`: a list of $n$ integers with $0 \le n \le 1000$ and `0 <= tokens[i] < 10000`.
- `power`: the initial nonnegative power, with `0 <= power < 10000`.

**Return value**

Return the greatest score achievable by playing each token at most once under the face-up and face-down rules.

### Examples

**Example 1**

- Input: `tokens = [100]`, `power = 50`
- Output: `0`

The token is too expensive to play face-up, and a zero score cannot pay for a face-down play.

**Example 2**

- Input: `tokens = [200, 100]`, `power = 150`
- Output: `1`

Play `100` face-up and stop.

**Example 3**

- Input: `tokens = [100, 200, 300, 400]`, `power = 200`
- Output: `2`

One optimal sequence plays `100` face-up, `400` face-down, then `200` and `300` face-up.
