## Examples

**Example 1**

- Input: `nums = [1,2,2]`
- Output: `1`
- Explanation: Begin with `[1, 2, 2]`. Increasing `nums[1]` once produces `[1, 3, 2]`, whose middle position is special. One special index is the achievable maximum for this length, and zero operations cannot attain it, so the minimum is $1$.

**Example 2**

- Input: `nums = [2,1,1,3]`
- Output: `2`
- Explanation: Starting from `[2, 1, 1, 3]`, apply both operations at index $1$ to obtain `[2, 3, 1, 3]`. Index $1$ is then special. The two interior positions are adjacent, so at most one of them can be special; this construction reaches that maximum with a minimum cost of $2$.

**Example 3**

- Input: `nums = [5,2,1,4,3]`
- Output: `4`
- Explanation: Apply four operations at index $1$. The array becomes `[5, 6, 1, 4, 3]`, in which indices $1$ and $3$ are special. Two is the maximum possible number of special indices, and the least cost of attaining it is $4$.
