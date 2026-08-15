# Minimum Number of Keypresses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2268 |
| Difficulty | Medium |
| Topics | Hash Table, String, Greedy, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-keypresses/) |

## Problem Description

### Goal

A configurable keypad has nine buttons numbered from `1` through `9`. All 26
lowercase English letters must be assigned to the buttons. Every letter is
assigned to exactly one button, and each button holds at most three letters.

The first letter assigned to a button costs one press, the second costs two
presses, and the third costs three presses. The assignment and the order of
letters on each button are fixed before the given string is typed.

Given a lowercase string `s`, choose a valid keypad layout that minimizes the
total number of presses required to type every character of `s`, and return
that minimum total.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$.

The length satisfies $1\le n\le10^5$.

**Return value**

Return the smallest possible sum of keypresses over all valid assignments of
the 26 letters to the nine buttons.

### Examples

#### Example 1

- **Input:** `s = "apple"`
- **Output:** `5`

The four used letters can all occupy one-press positions, so each of the five
characters costs one press.

#### Example 2

- **Input:** `s = "abcdefghijkl"`
- **Output:** `15`

Nine letters use one-press positions and the remaining three use two-press
positions, for $9+3\cdot2=15$ presses.
