# Best Poker Hand

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2347 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/best-poker-hand/) |

## Problem Description

### Goal

Five cards are described by parallel arrays `ranks` and `suits`; card $i$ has
rank `ranks[i]` and suit `suits[i]`. No two cards have the same rank-and-suit
combination. Classify the strongest hand available from these cards among the
four categories defined below.

From strongest to weakest, `"Flush"` means all five suits agree,
`"Three of a Kind"` means at least three ranks agree, `"Pair"` means at least
two ranks agree, and `"High Card"` is always available from one card. Return
the exact case-sensitive name of the strongest category that applies.

### Function Contract

**Inputs**

- `ranks`: Exactly five integers, each from 1 through 13.
- `suits`: Exactly five characters, each from `'a'` through `'d'`.

The rank and suit at each shared index form one card, and all five cards are
distinct.

**Return value**

One of `"Flush"`, `"Three of a Kind"`, `"Pair"`, or `"High Card"`.

### Examples

**Example 1**

- Input: `ranks = [13,2,3,1,9]`, `suits = ["a","a","a","a","a"]`
- Output: `"Flush"`
- Explanation: Every card has suit `"a"`.

**Example 2**

- Input: `ranks = [4,4,2,4,4]`, `suits = ["d","a","a","b","c"]`
- Output: `"Three of a Kind"`
- Explanation: Rank 4 occurs four times, which includes at least three cards.

**Example 3**

- Input: `ranks = [10,10,2,12,9]`, `suits = ["a","b","c","a","d"]`
- Output: `"Pair"`
- Explanation: Rank 10 occurs twice, while no stronger category applies.
