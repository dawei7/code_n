# Minimum Number Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2974 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-game/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` with even length and begin with
an empty array `arr`. Alice and Bob repeatedly play one round until `nums` is
empty.

In each round, Alice first removes a minimum element from `nums`, then Bob
removes the new minimum. Bob appends his removed value to `arr` first, followed
by Alice's value.

Return the final contents of `arr` after all rounds.

### Function Contract

**Inputs**

- `nums`: an even-length array of positive integers used by the game

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $2\le N\le100$,
$1\le\texttt{nums[i]}\le100$, and even $N$.

**Return value**

The array formed by appending Bob's removal and then Alice's removal in every
round.

### Examples

#### Example 1

- **Input:** `nums = [5,4,2,3]`
- **Output:** `[3,2,5,4]`
- **Explanation:** The removed pairs are `(2,3)` and `(4,5)`, each appended in reverse player order.

#### Example 2

- **Input:** `nums = [2,5]`
- **Output:** `[5,2]`
- **Explanation:** Alice removes `2`, Bob removes `5`, and Bob appends first.
