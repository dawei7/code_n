## Examples

**Example 1**

- Input: `root = [5,3,8,2,4,7,1]`
- Output: `5`
- **Explanation:** The four leaves with values `2`, `4`, `7`, and `1` are dominant. The node valued `8` is also dominant because `8` is the maximum of its subtree `[8,7,1]`. No other node qualifies, so the total is `5`.

The source diagram's complete tree and dominance facts are represented accessibly below.

| Level-order index | Value | Children | Subtree maximum | Dominant? |
|---:|---:|---|---:|---|
| 0 | 5 | indices 1 and 2 | 8 | No |
| 1 | 3 | indices 3 and 4 | 4 | No |
| 2 | 8 | indices 5 and 6 | 8 | Yes |
| 3 | 2 | none | 2 | Yes |
| 4 | 4 | none | 4 | Yes |
| 5 | 7 | none | 7 | Yes |
| 6 | 1 | none | 1 | Yes |

**Example 2**

- Input: `root = [1,2,3,1,2]`
- Output: `4`
- **Explanation:** The leaf nodes with values `1`, `2`, and `3` are dominant. The internal node valued `2` is also dominant because it is the maximum of its subtree `[2,1,2]`. Therefore, the answer is `4`.

This table independently preserves the second source diagram, including the two distinct nodes whose value is `2`.

| Level-order index | Value | Children | Subtree maximum | Dominant? |
|---:|---:|---|---:|---|
| 0 | 1 | indices 1 and 2 | 3 | No |
| 1 | 2 | indices 3 and 4 | 2 | Yes |
| 2 | 3 | none | 3 | Yes |
| 3 | 1 | none | 1 | Yes |
| 4 | 2 | none | 2 | Yes |
