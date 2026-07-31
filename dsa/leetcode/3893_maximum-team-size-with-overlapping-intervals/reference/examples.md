## Examples

**Example 1**

- Input: `startTime = [1,2,3], endTime = [4,5,6]`
- Output: `3`
- Explanation: Employee $0$ has interval $[1,4]$. It overlaps employee $1$'s interval $[2,5]$ and employee $2$'s interval $[3,6]$, so employee $0$ can interact with both other members and all three employees form a valid team.

**Example 2**

- Input: `startTime = [2,5,8], endTime = [3,7,9]`
- Output: `1`
- Explanation: The intervals $[2,3]$, $[5,7]$, and $[8,9]$ are pairwise disjoint. No employee can interact with another one, so any valid team contains only its single hub member and the maximum size is $1$.

**Example 3**

- Input: `startTime = [3,4,6], endTime = [8,5,7]`
- Output: `3`
- Explanation: Employee $0$ is available on $[3,8]$. This interval overlaps both $[4,5]$ and $[6,7]$, even though those two shorter intervals do not overlap each other. Employee $0$ can therefore serve as the hub of a valid three-person team.
