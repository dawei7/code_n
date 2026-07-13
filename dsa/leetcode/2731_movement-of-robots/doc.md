# Movement of Robots

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2731 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Brainteaser, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [movement-of-robots](https://leetcode.com/problems/movement-of-robots/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/movement-of-robots/).

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

## Solution
### Approach
1. **Brainteaser (Collision Equivalence)**: When two identical robots collide and bounce off each other, their trajectories swap. Because the robots are indistinguishable, this is equivalent to them passing through each other without any collision. Thus, we can calculate the final position of each robot independently: if a robot starts at $x$ and moves right ('R'), its final position is $x + d$. If it moves left ('L'), its final position is $x - d$.
2. **Sorting**: Once the final positions are determined, we sort them to easily compute pairwise absolute differences.
3. **Prefix Sum / Mathematical Simplification**: For a sorted array $A$ of size $n$, the sum of all pairwise absolute differences $\sum_{i < j} (A[j] - A[i])$ can be computed in $O(n)$ time. Each element $A[i]$ (0-indexed) is subtracted in $n - 1 - i$ pairs and added in $i$ pairs. Thus, the total sum is:
   $$\sum_{i=0}^{n-1} A[i] \cdot (2i - n + 1)$$

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n \log n)$ due to sorting the final positions of the $n$ robots. The position calculation and the pairwise sum calculation both take $\mathcal{O}(n)$ time.
- **Space Complexity**: $\mathcal{O}(n)$ to store the final positions of the robots.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], s: str, d: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    # Calculate final positions as if robots pass through each other
    final_positions = []
    for i in range(n):
        if s[i] == 'R':
            final_positions.append(nums[i] + d)
        else:
            final_positions.append(nums[i] - d)

    # Sort the positions to compute pairwise absolute differences efficiently
    final_positions.sort()

    # Compute the sum of pairwise absolute differences
    total_sum = 0
    for i in range(n):
        total_sum += final_positions[i] * (2 * i - n + 1)

    return total_sum % MOD
```
</details>
