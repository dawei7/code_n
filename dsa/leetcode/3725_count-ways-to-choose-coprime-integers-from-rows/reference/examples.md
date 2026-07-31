## Examples

**Example 1**

- Input: `mat = [[1,2],[3,4]]`
- Output: `3`
- Explanation: All four ways to choose one value from each row are:

| First-row choice | Second-row choice | GCD of chosen values |
|---:|---:|---:|
| 1 | 3 | 1 |
| 1 | 4 | 1 |
| 2 | 3 | 1 |
| 2 | 4 | 2 |

Three combinations have GCD `1`, so the answer is `3`.

**Example 2**

- Input: `mat = [[2,2],[2,2]]`
- Output: `0`
- Explanation: Every positional combination chooses two values equal to `2`, making the overall GCD `2`. None qualifies, so the answer is `0`.
