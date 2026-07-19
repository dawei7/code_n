# Reveal Cards In Increasing Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 950 |
| Difficulty | Medium |
| Topics | Array, Queue, Sorting, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/reveal-cards-in-increasing-order/) |

## Problem Description

### Goal

You are given a `deck` of cards, each carrying a unique integer, and may choose any initial ordering. All cards initially face down. Repeatedly reveal and remove the top card; if cards remain, move the next top card to the bottom; then repeat until the deck is empty.

Return an initial ordering for which the revealed values are in increasing order. The first element of the returned list represents the top of the deck.

### Function Contract

Let $n$ be the number of cards in `deck`.

**Inputs**

- `deck`: a list of $n$ unique integers, where $1 \le n \le 1000$ and `1 <= deck[i] <= 1000000`.

**Return value**

Return a permutation of `deck` whose reveal-and-rotate process exposes the card values in increasing order.

### Examples

**Example 1**

- Input: `deck = [17,13,11,2,3,5,7]`
- Output: `[2,13,3,11,5,17,7]`
- Explanation: Revealing and rotating this ordering exposes `2,3,5,7,11,13,17`.

**Example 2**

- Input: `deck = [1,1000]`
- Output: `[1,1000]`
