# Remove Colored Pieces if Both Neighbors are the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2038 |
| Difficulty | Medium |
| Topics | Math, String, Greedy, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) |

## Problem Description

### Goal

A line contains pieces colored either `"A"` or `"B"`, represented in order by
the string `colors`. Alice and Bob alternate turns, with Alice moving first.
Alice may remove only an `"A"` piece whose immediate left and right neighbors
are both `"A"`; Bob has the corresponding rule for `"B"`.

Neither player may remove a piece at an edge of the current line. A player who
has no legal removal on their turn loses immediately. Assuming both players
play optimally, return whether Alice wins.

### Function Contract

Let $N$ be the length of `colors`.

**Inputs**

- `colors`: a string of only `"A"` and `"B"`, with
  $1 \le N \le 10^5$.

**Return value**

- `true` if Alice wins under optimal play; otherwise `false`.

### Examples

**Example 1**

- Input: `colors = "AAABABB"`
- Output: `true`
- Explanation: Alice removes the middle piece from the initial `"AAA"` run,
  after which Bob has no legal move.

**Example 2**

- Input: `colors = "AA"`
- Output: `false`
- Explanation: Neither piece has two neighbors, so Alice loses immediately.

**Example 3**

- Input: `colors = "ABBBBBBBAAA"`
- Output: `false`
- Explanation: Alice has one available removal, while Bob has more than one.
