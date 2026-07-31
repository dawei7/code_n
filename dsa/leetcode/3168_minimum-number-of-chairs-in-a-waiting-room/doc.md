# Minimum Number of Chairs in a Waiting Room

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3168 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/) |

## Problem Description

### Goal

A waiting room starts empty. A string `s` records one event at each second. An `E` means that one person enters and immediately takes a chair, while an `L` means that one person leaves and makes their chair available again.

Determine the minimum number of chairs the room must contain so that every arriving person can sit immediately throughout this valid sequence of entries and exits. The room need not be empty after the final event.

### Function Contract

**Inputs**

- `s`: A valid sequence containing only the characters `E` and `L`.

Let $n = \lvert\texttt{s}\rvert$. The constraints satisfy $1 \le n \le 50$. Validity guarantees that no exit occurs when the waiting room is empty.

**Return value**

- The minimum number of chairs needed to serve every entry event.

### Examples

**Example 1**

- Input: `s = "EEEEEEE"`
- Output: `7`

Seven people enter without any intervening departure, so all seven need chairs simultaneously.

**Example 2**

- Input: `s = "ELELEEL"`
- Output: `2`

The occupancy alternates between zero and one until two consecutive entries raise it to two.

**Example 3**

- Input: `s = "ELEELEELLL"`
- Output: `3`

The greatest number of people present at the same time is three.
