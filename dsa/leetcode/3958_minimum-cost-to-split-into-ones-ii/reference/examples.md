## Examples

**Example 1**

- Input: `n = 3`
- Output: `3`

- **Explanation:** One optimal sequence first separates `3` into `1` and `2`, then separates the remaining `2` into two ones:

| `x` | `a` | `b` | `a + b` | `a * b` | Cost |
|---:|---:|---:|---:|---:|---:|
| 3 | 1 | 2 | 3 | 2 | 2 |
| 2 | 1 | 1 | 2 | 1 | 1 |

The accumulated cost is `2 + 1 = 3`.

**Example 2**

- Input: `n = 4`
- Output: `6`

- **Explanation:** An optimal first operation splits `4` into two pieces of value `2`. Each of those pieces is then split into two ones:

| `x` | `a` | `b` | `a + b` | `a * b` | Cost |
|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 4 | 4 | 4 |
| 2 | 1 | 1 | 2 | 1 | 1 |

The second row's operation is performed for both pieces of value `2`, so the total is `4 + 1 + 1 = 6`.
