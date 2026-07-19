# Handshakes That Don't Cross

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1259 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/handshakes-that-dont-cross/) |

## Problem Description

### Goal

An even number of people sit around a circle. Every person must shake hands with exactly one other person, producing a perfect pairing. Draw each handshake as a straight segment between the two participants.

Count how many different complete pairing arrangements can be drawn without any two handshake segments crossing inside the circle. Return the count modulo $10^9+7$. People occupy distinct positions, so pairings that connect different position pairs are different arrangements even when they have the same geometric shape after rotation.

### Function Contract

**Inputs**

- `numPeople`: an even integer between `2` and `1000`.
- Let $p=\texttt{numPeople}/2$ be the number of handshake pairs.

**Return value**

- Return the number of noncrossing perfect pairings modulo $10^9+7$.

### Examples

**Example 1**

- Input: `numPeople = 2`
- Output: `1`

**Example 2**

- Input: `numPeople = 4`
- Output: `2`

**Example 3**

- Input: `numPeople = 6`
- Output: `5`
