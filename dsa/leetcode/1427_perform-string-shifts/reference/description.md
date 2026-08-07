## Description

You are given a string `s` containing lowercase English letters, and a matrix `shift`, where $\text{shift}[i] = [\text{direction}_{i}, \text{amount}_{i}]$:

- $\text{direction}_{i}$ can be `0` (for left shift) or `1` (for right shift).

- $\text{amount}_{i}$ is the amount by which string `s` is to be shifted.

- A left shift by 1 means remove the first character of `s` and append it to the end.

- Similarly, a right shift by 1 means remove the last character of `s` and add it to the beginning.

Return the final string after all operations.
### Function Contract

**Inputs**

- `s`: a nonempty string containing lowercase English letters.
- `shift`: a nonempty matrix whose row `shift[i]` is `[direction_i, amount_i]`.

For each operation, `direction_i = 0` means left and `direction_i = 1` means right. `amount_i` is the requested number of cyclic positions and may be zero.

**Return value**

Return the string obtained after applying all rows of `shift`. Every operation acts on the result of the preceding operation, and every shift preserves the string's length and character multiplicities.

### Examples
#### Example 1

- **Input:** `s = "abc", shift = [[0,1],[1,2]]`
- **Output:** `"cab"`
- **Explanation:**
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
#### Example 2

- **Input:** `s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]`
- **Output:** `"efgabcd"`
- **Explanation:**
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
### Constraints

- $1 \le \text{s.length} \le 100$

- `s` only contains lower case English letters.

- $1 \le \text{shift.length} \le 100$

- $\text{shift}[i].length = 2$

- $\text{direction}_{i}$_ is either `0` or `1`.

- $0 \le \text{amount}_{i} \le 100$