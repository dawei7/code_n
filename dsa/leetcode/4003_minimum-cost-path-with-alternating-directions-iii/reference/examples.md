## Examples

**Example 1**

- Input: `m = 2, n = 2, penalty = [[5, 3], [1, 4]]`
- Output: `8`
- **Explanation:** Move down during the first, odd second and pay the entrance cost $2$ for cell $(2,1)$. On the second, even second, move right. Right is not a permitted even-second direction, so this action pays both the destination cost $4$ and the source penalty `penalty[1][0] = 1`. Including the starting cost, the total is $1+2+4+1=8$.

**Example 2**

- Input: `m = 2, n = 2, penalty = [[0, 7], [3, 2]]`
- Output: `7`
- **Explanation:** Wait in cell $(1,1)$ during the first second; its penalty is zero. Move right during the second second, paying entrance cost $2$ and the zero source penalty because right is contrary to the even-second direction rule. Then move down during the third, odd second and pay entrance cost $4$. The total is $1+0+2+0+4=7$.

**Example 3**

- Input: `m = 2, n = 3, penalty = [[8, 0, 9], [7, 4, 1]]`
- Output: `12`
- **Explanation:** Move right during the first second for entrance cost $2$. Move right again during the second second: this violates the even-second direction rule, but the extra charge is `penalty[0][1] = 0`, so only entrance cost $3$ is added. Finally move down during the third, odd second for entrance cost $6$. The minimum total is $1+2+3+0+6=12$.
