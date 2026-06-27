# Movement of Robots

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2731 |
| Difficulty | Medium |
| Topics | Array, Brainteaser, Sorting, Prefix Sum |
| Official Link | [movement-of-robots](https://leetcode.com/problems/movement-of-robots/) |

## Problem Description & Examples
### Goal
Given the initial positions of $n$ robots on a 1D line, their initial directions ('L' for left, 'R' for right), and a duration $d$ in seconds, determine the sum of the pairwise absolute differences between the positions of all robots after $d$ seconds. 

When two robots collide, they instantly reverse their directions. Since the robots are identical and indistinguishable, a collision is equivalent to them passing through each other. Return the sum modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `nums`: `List[int]` - The initial 0-indexed coordinate positions of the robots.
- `s`: `str` - A string of length $n$ where `s[i]` is 'L' or 'R', representing the initial direction of the $i$-th robot.
- `d`: `int` - The number of seconds the robots move.

**Return value**

- `int` - The sum of pairwise absolute differences of the final positions of all robots, modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `nums = [-2, 0, 2]`, `s = "RLL"`, `d = 3`
- Output: `8`

**Example 2**

- Input: `nums = [1, 0]`, `s = "RL"`, `d = 2`
- Output: `5`

---

## Underlying Base Algorithm(s)
1. **Brainteaser (Collision Equivalence)**: When two identical robots collide and bounce off each other, their trajectories swap. Because the robots are indistinguishable, this is equivalent to them passing through each other without any collision. Thus, we can calculate the final position of each robot independently: if a robot starts at $x$ and moves right ('R'), its final position is $x + d$. If it moves left ('L'), its final position is $x - d$.
2. **Sorting**: Once the final positions are determined, we sort them to easily compute pairwise absolute differences.
3. **Prefix Sum / Mathematical Simplification**: For a sorted array $A$ of size $n$, the sum of all pairwise absolute differences $\sum_{i < j} (A[j] - A[i])$ can be computed in $O(n)$ time. Each element $A[i]$ (0-indexed) is subtracted in $n - 1 - i$ pairs and added in $i$ pairs. Thus, the total sum is:
   $$\sum_{i=0}^{n-1} A[i] \cdot (2i - n + 1)$$

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$ due to sorting the final positions of the $n$ robots. The position calculation and the pairwise sum calculation both take $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(n)$ to store the final positions of the robots.
