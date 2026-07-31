## Description

You begin at index `0` of a 0-indexed integer array `nums` with length $n$.

The value `nums[i]` is the greatest permitted length of a forward jump from index `i`. From `i`, you may choose a jump length $j$ satisfying both

$$
0 \le j \le \texttt{nums[i]}
$$

and


$$
i + j < n.
$$

Return the minimum number of jumps required to reach index $n - 1$. Every test case guarantees that the final index is reachable.
