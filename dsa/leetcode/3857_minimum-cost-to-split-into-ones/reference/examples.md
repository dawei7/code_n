## Examples

**Example 1**

- Input: `n = 3`
- Output: `3`
- Explanation: One optimal sequence uses the following operations.

| `x` | `a` | `b` | `a + b` | `a * b` | Cost |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 2 | 3 | 2 | 2 |
| 2 | 1 | 1 | 2 | 1 | 1 |

The minimum total is `2 + 1 = 3`.

**Example 2**

- Input: `n = 4`
- Output: `6`
- Explanation: One optimal sequence uses the following operations.

| `x` | `a` | `b` | `a + b` | `a * b` | Cost |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 4 | 4 | 4 |
| 2 | 1 | 1 | 2 | 1 | 1 |
| 2 | 1 | 1 | 2 | 1 | 1 |

The minimum total is `4 + 1 + 1 = 6`.
