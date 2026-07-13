# Hand of Straights

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 846 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [hand-of-straights](https://leetcode.com/problems/hand-of-straights/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/hand-of-straights/).

### Goal
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `group_size`, and consists of `group_size` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i`-th card and an integer `group_size`, return `True` if she can rearrange the cards, or `False` otherwise.

### Function Contract
**Inputs**

- `hand`: List[int]
- `group_size`: int

**Return value**

bool - True if hand can be split into valid groups

### Examples
**Example 1**

- Input: `hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], group_size = 3`
- Output: `True`

**Example 2**

- Input: `hand = [1, 6, 2, 3, 7, 5], group_size = 3`
- Output: `True`

**Example 3**

- Input: `hand = [5, 16], group_size = 2`
- Output: `False`

---

## Solution
### Approach
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
