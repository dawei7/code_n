# Stone Game VI

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1686 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting, Heap (Priority Queue), Game Theory |
| Official Link | [stone-game-vi](https://leetcode.com/problems/stone-game-vi/) |

## Problem Description & Examples
### Goal
Alice and Bob take turns choosing stones. Stone `i` is worth `aliceValues[i]` to Alice and `bobValues[i]` to Bob. Both play optimally, Alice moves first, and the winner is decided by total personal score.

### Function Contract
**Inputs**

- `aliceValues`: Alice's value for each stone.
- `bobValues`: Bob's value for each stone.

**Return value**

Return `1` if Alice wins, `-1` if Bob wins, or `0` if they tie.

### Examples
**Example 1**

- Input: `aliceValues = [1,3], bobValues = [2,1]`
- Output: `1`

**Example 2**

- Input: `aliceValues = [1,2], bobValues = [3,1]`
- Output: `0`

**Example 3**

- Input: `aliceValues = [2,4,3], bobValues = [1,6,7]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Sort stones by the combined value `aliceValues[i] + bobValues[i]` descending. A stone with the largest combined value is the most important to claim because taking it both gains current-player value and denies opponent value. Alternate picks from that order and compare the final scores.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
