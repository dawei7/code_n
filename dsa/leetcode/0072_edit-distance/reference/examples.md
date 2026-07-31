## Examples

**Example 1**

- Input: `word1 = "horse", word2 = "ros"`
- Output: `3`
- Explanation: One optimal sequence is `horse → rorse` by replacing `h` with `r`, then `rorse → rose` by deleting `r`, then `rose → ros` by deleting `e`.

**Example 2**

- Input: `word1 = "intention", word2 = "execution"`
- Output: `5`
- Explanation: One optimal sequence is `intention → inention` by deleting `t`, `inention → enention` by replacing `i` with `e`, `enention → exention` by replacing `n` with `x`, `exention → exection` by replacing `n` with `c`, and `exection → execution` by inserting `u`.
