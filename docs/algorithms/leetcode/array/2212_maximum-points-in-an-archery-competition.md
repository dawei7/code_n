# Maximum Points in an Archery Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2212 |
| Difficulty | Medium |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Official Link | [maximum-points-in-an-archery-competition](https://leetcode.com/problems/maximum-points-in-an-archery-competition/) |

## Problem Description & Examples
### Goal
Distribute Bob's arrows among scoring sections `0` through `11`. Bob wins section `i` and earns `i` points only by placing more arrows there than Alice; otherwise Alice wins it. Return any allocation maximizing Bob's score, using every arrow.

### Function Contract
**Inputs**

- `numArrows`: Bob's total number of arrows.
- `aliceArrows`: Alice's arrow counts for the twelve sections.

**Return value**

Any length-12 allocation for Bob that uses exactly `numArrows` and achieves his maximum score.

### Examples
**Example 1**

- Input: `numArrows = 9`, `aliceArrows = [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]`
- Output: `[0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1]`

**Example 2**

- Input: `numArrows = 3`, `aliceArrows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Output: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]`

**Example 3**

- Input: `numArrows = 1`, `aliceArrows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Output: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`

---

## Underlying Base Algorithm(s)
Enumerate all subsets of the twelve sections. Winning section `i` costs `aliceArrows[i] + 1` arrows and gains `i` points. Keep the affordable subset with the highest score, assign its required arrows, and place all unused arrows in any section, commonly section zero, without reducing the score.

---

## Complexity Analysis
- **Time Complexity**: `O(12 * 2^12)`
- **Space Complexity**: `O(12)` excluding enumeration state
