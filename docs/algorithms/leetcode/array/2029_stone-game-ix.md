# Stone Game IX

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2029 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Counting, Game Theory |
| Official Link | [stone-game-ix](https://leetcode.com/problems/stone-game-ix/) |

## Problem Description & Examples
### Goal
Players remove stones with integer values. A player loses immediately if the running sum becomes divisible by `3`; determine whether Alice can force a win.

### Function Contract
**Inputs**

- `stones`: stone values.

**Return value**

Return `True` if Alice wins with optimal play, otherwise `False`.

### Examples
**Example 1**

- Input: `stones = [2,1]`
- Output: `True`

**Example 2**

- Input: `stones = [2]`
- Output: `False`

**Example 3**

- Input: `stones = [5,1,2,4,3]`
- Output: `False`

---

## Underlying Base Algorithm(s)
Only values modulo `3` matter. Count residues `0`, `1`, and `2`. Zero-residue stones mainly flip turn parity without changing the sum. The winning condition depends on whether both residue `1` and `2` are available and how imbalanced their counts are after accounting for zero parity.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
