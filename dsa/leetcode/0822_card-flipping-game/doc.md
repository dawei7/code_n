# Card Flipping Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 822 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/card-flipping-game/) |

## Problem Description

### Goal

You are given two zero-indexed arrays `fronts` and `backs` describing cards on a table. Card `i` initially shows positive integer `fronts[i]` face up and has `backs[i]` face down. You may flip any number of cards, including none.

After the flips, an integer is good when it is face down on at least one card and is not face up on any card. Return the minimum possible good integer obtainable by choosing which cards to flip. If no integer can satisfy both conditions, return `0`.

### Function Contract

**Inputs**

- `fronts`: the positive integers initially facing up
- `backs`: the positive integers initially facing down, with `len(backs) = len(fronts)`

**Return value**

- The smallest integer that can be made good by flipping cards, or `0` when no good integer exists

### Examples

**Example 1**

- Input: `fronts = [1, 2, 4, 4, 7], backs = [1, 3, 4, 1, 3]`
- Output: `2`
- Explanation: Flip the second card so `2` is down and no card shows `2` face up.

**Example 2**

- Input: `fronts = [1], backs = [1]`
- Output: `0`
- Explanation: The same value remains face up regardless of this card's orientation.

**Example 3**

- Input: `fronts = [1], backs = [2]`
- Output: `1`
- Explanation: Flipping the card places `1` face down and `2` face up.
