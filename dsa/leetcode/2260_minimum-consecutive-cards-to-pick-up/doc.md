# Minimum Consecutive Cards to Pick Up

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2260 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) |

## Problem Description

### Goal

The array `cards` lists card values in their current order. Two cards form a
matching pair when their values are equal.

Choose one contiguous portion of the array to pick up. It must contain at
least two occurrences of some value, and its length is the number of cards
picked up, including both matching endpoints and every card between them.
Return the minimum possible length of such a consecutive portion. If every
card value is distinct and no matching pair can be included, return `-1`.

### Function Contract

**Inputs**

- `cards`: An array of $n$ integers, where $1\le n\le10^5$ and $0\le\texttt{cards[i]}\le10^6$.

**Return value**

Return the minimum value of $j-i+1$ over all pairs $i<j$ satisfying
$\texttt{cards[i]}=\texttt{cards[j]}$, or `-1` when no such pair exists.

### Examples

**Example 1**

- Input: `cards = [3,4,2,3,4,7]`
- Output: `4`

**Example 2**

- Input: `cards = [1,0,5,3]`
- Output: `-1`

**Example 3**

- Input: `cards = [8,8]`
- Output: `2`
