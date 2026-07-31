# Winner of the Linked List Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3062 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/winner-of-the-linked-list-game/) |

## Problem Description

### Goal

Two teams, named Even and Odd, play a game on a singly linked list whose length is even. The nodes are indexed from zero. Every node at an even index contains an even integer, while every node at an odd index contains an odd integer.

Process the list as consecutive two-node groups: indices $0$ and $1$, then $2$ and $3$, and so on. Within each group, the team associated with the node holding the larger value earns one point. Thus, Even scores when the even-indexed value is larger, and Odd scores when the odd-indexed value is larger.

Determine which team has more points after every pair has been considered. Return `"Even"` or `"Odd"` for the winning team, or `"Tie"` when their scores are equal.

### Function Contract

**Inputs**

- `head`: The first node of a singly linked list containing $n$ integers.

The list length is even and satisfies $2 \le n \le 100$. Node values lie from $1$ through $100$. Values at even indices are even, and values at odd indices are odd.

**Return value**

Return `"Even"` if the Even team earns more points, `"Odd"` if the Odd team earns more points, or `"Tie"` if both teams earn the same number of points.

### Examples

**Example 1**

- Input: `head = [2, 1]`
- Output: `"Even"`
- Explanation: The even-indexed value `2` is larger than the odd-indexed value `1`, so Even wins the only point.

**Example 2**

- Input: `head = [2, 5, 4, 7, 20, 5]`
- Output: `"Odd"`
- Explanation: Odd wins the first two pairs, while Even wins the last pair, giving Odd the higher score.

**Example 3**

- Input: `head = [4, 5, 2, 1]`
- Output: `"Tie"`
- Explanation: Odd wins the first pair and Even wins the second.
