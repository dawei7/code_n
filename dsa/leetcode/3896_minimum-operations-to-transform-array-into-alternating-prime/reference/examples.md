## Examples

**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `3`
- Explanation:
  - Index $0$ must contain a prime. Increment `nums[0] = 1` once to reach $2$.
  - Index $1$ must contain a non-prime. Increment `nums[1] = 2` twice to reach $4$.
  - The value at index $2$ is already prime.
  - The value at index $3$ is already non-prime.

  The total is $1+2=3$ operations.

**Example 2**

- Input: `nums = [5,6,7,8]`
- Output: `0`
- Explanation:
  - The elements at even indices $0$ and $2$ are already prime.
  - The elements at odd indices $1$ and $3$ are already non-prime.

  Every position already meets its requirement, so no operation is needed.

**Example 3**

- Input: `nums = [4,4]`
- Output: `1`
- Explanation:
  - Index $0$ must contain a prime. Increment `nums[0] = 4` once to reach $5$.
  - The value at index $1$ is already non-prime.

  The minimum total is $1$ operation.
