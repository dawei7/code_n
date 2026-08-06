## Description

A 0-indexed array `nums` describes $n$ positions, and the walk begins at index $0$. A forward jump from $i$ to $j$, where $i < j$, is allowed in either of two cases:
1. `nums[i] <= nums[j]`, and every value strictly between $i$ and $j$ is strictly less than `nums[i]` (`nums[k] < nums[i]` for all $i < k < j$).
2. `nums[i] > nums[j]`, and every value strictly between $i$ and $j$ is greater than or equal to `nums[i]` (`nums[k] >= nums[i]` for all $i < k < j$).

The parallel array `costs` gives the price of landing at each position: jumping to $j$ adds `costs[j]`, while the starting position at index $0$ has no charge.

Choose valid forward jumps that reach index $n-1$ and return the minimum total landing cost.
