## Examples

**Example 1**

- Input: `n = 3, edges = [[0,1,1],[1,2,1],[0,2,1]]`
- Output: `2`
- Explanation: The first two weight-$1$ edges form a path and create no cycle, so both are added. The final proposal would close the triangle shown below. Its three weights sum to $1+1+1=3$, which is odd, so that dashed edge is rejected.

```text
0 -------- 1 -------- 2
     1           1
 \ . . . . . . . . /
      proposed 1
```

**Example 2**

- Input: `n = 3, edges = [[0,1,1],[1,2,1],[0,2,0]]`
- Output: `3`
- Explanation: The first two proposals are again accepted because they form a path. This time the closing edge has weight $0$, so the triangle's total is $1+1+0=2$. The cycle is even-weighted and all three edges are retained.

```text
0 -------- 1 -------- 2
     1           1
 \_________________/
          0
```
