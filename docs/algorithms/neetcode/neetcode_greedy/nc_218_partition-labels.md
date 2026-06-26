## Problem Description & Examples
### Goal
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return a list of integers representing the size of these parts.

### Function Contract
**Inputs**

- `s`: str

**Return value**

List[int] - partition sizes

### Examples
**Example 1**

- Input: `s = "ababcbacadefegdehijhklij"`
- Output: `[9, 7, 8]`

**Example 2**

- Input: `s = 'ynbi'`
- Output: `[1, 1, 1, 1]`

**Example 3**

- Input: `s = 'szy'`
- Output: `[1, 1, 1]`

---

## Underlying Base Algorithm(s)
- [Gas station](greedy_06_gas-station.md)
- [Jump game](greedy_07_jump-game.md)
- [Candy distribution](greedy_08_candy-distribution.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
