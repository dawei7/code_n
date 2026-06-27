# Robot Collisions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2751 |
| Difficulty | Hard |
| Topics | Array, Stack, Sorting, Simulation |
| Official Link | [robot-collisions](https://leetcode.com/problems/robot-collisions/) |

## Problem Description & Examples
### Goal
Given a set of robots positioned on a 1D line, each moving in a specific direction ('L' or 'R') at the same speed, determine the health of the survivors after all possible collisions occur. When two robots collide, the one with lower health is removed, and the one with higher health loses 1 unit of health. If they have equal health, both are removed. Collisions only happen when a robot moving right encounters a robot moving left.

### Function Contract
**Inputs**

- `positions`: A list of integers representing the starting coordinate of each robot.
- `healths`: A list of integers representing the initial health of each robot.
- `directions`: A string where each character ('L' or 'R') denotes the movement direction of the robot at the corresponding index.

**Return value**

- A list of integers representing the health of the surviving robots, ordered by their original input index.

### Examples
**Example 1**

- Input: `positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"`
- Output: `[2,17,9,15,10]`

**Example 2**

- Input: `positions = [3,5,2,6], healths = [10,10,10,10], directions = "RLRL"`
- Output: `[10,10]`

**Example 3**

- Input: `positions = [1,2,5,6], healths = [10,10,10,10], directions = "RLRL"`
- Output: `[]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Stack-based Simulation** combined with **Sorting**. Since robots only collide if they are moving toward each other, we first sort the robots by their initial positions. We then iterate through the sorted robots, using a stack to keep track of robots moving to the right ('R') that have not yet collided. When we encounter a robot moving to the left ('L'), we check the stack for potential collisions with 'R' robots, resolving them based on health values until the 'L' robot is destroyed, the stack is empty, or the 'L' robot survives and continues moving left.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of robots. The sorting step dominates the complexity, while the stack-based simulation processes each robot at most twice (once pushed, once popped).
- **Space Complexity**: `O(N)` to store the sorted robot data and the stack of survivors.
