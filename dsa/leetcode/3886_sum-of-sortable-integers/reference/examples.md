## Examples

**Example 1**

- Input: `nums = [3,1,2]`
- Output: `3`
- Explanation: The divisors of $3$ are $1$ and $3$. Blocks of length $1$ cannot change the array, so $k=1$ fails. With $k=3$, rotating `[3,1,2]` once produces `[1,2,3]`. Thus only $3$ is sortable, and the sum is $3$.

**Example 2**

- Input: `nums = [7,6,5]`
- Output: `0`
- Explanation: Again the possible lengths are $1$ and $3$. Singleton blocks leave the descending array unchanged, while no cyclic rotation of `[7,6,5]` is non-decreasing. Neither divisor is sortable.

**Example 3**

- Input: `nums = [5,8]`
- Output: `3`
- Explanation: The array is already non-decreasing, so both divisors $1$ and $2$ are sortable without any rotation. Their sum is $1+2=3$.
