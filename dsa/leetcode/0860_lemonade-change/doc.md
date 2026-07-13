# Lemonade Change

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 860 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [lemonade-change](https://leetcode.com/problems/lemonade-change/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/lemonade-change/).

### Goal
At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time. Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that they pay `$5`.

Note that you do not have any change in hand at first.

Return `True` if you can provide every customer with the correct change, or `False` otherwise.

### Function Contract
**Inputs**

- `bills`: List[int]

**Return value**

bool - True if change can be provided for everyone

### Examples
**Example 1**

- Input: `bills = [5, 5, 5, 10, 20]`
- Output: `True`

**Example 2**

- Input: `bills = [5, 5, 10]`
- Output: `True`

**Example 3**

- Input: `bills = [10, 5]`
- Output: `False`

---

## Solution
### Approach
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
