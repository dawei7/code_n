## Examples

**Example 1**

- Input: `blocks = [1], split = 1`
- Output: `1`
- Explanation: The initial worker builds the only block in one time unit.

**Example 2**

- Input: `blocks = [1,2], split = 5`
- Output: `7`
- Explanation: Split the initial worker into two workers in five time units, then assign one block to each worker. The elapsed time is `5 + max(1, 2) = 7`.

**Example 3**

- Input: `blocks = [1,2,3], split = 1`
- Output: `4`
- Explanation: First split the initial worker into two. Assign one worker to the last block, whose build time is `3`, and have the other worker split once more. The two newly available workers build the first two blocks. The resulting time is `1 + max(3, 1 + max(1, 2)) = 4`.
