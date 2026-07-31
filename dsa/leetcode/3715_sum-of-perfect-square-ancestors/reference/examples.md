## Examples

**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2]], nums = [2, 8, 2]`
- Output: `3`
- Explanation:

| `i` | Ancestors | `nums[i] * nums[ancestor]` | Square check | $t_i$ |
|---:|---|---|---|---:|
| 1 | `[0]` | `nums[1] * nums[0] = 8 * 2 = 16` | `16` is a perfect square. | 1 |
| 2 | `[1, 0]` | `nums[2] * nums[1] = 2 * 8 = 16`<br>`nums[2] * nums[0] = 2 * 2 = 4` | Both `16` and `4` are perfect squares. | 2 |

Across the non-root nodes, the total is `1 + 2 = 3`.

**Example 2**

- Input: `n = 3, edges = [[0, 1], [0, 2]], nums = [1, 2, 4]`
- Output: `1`
- Explanation:

| `i` | Ancestors | `nums[i] * nums[ancestor]` | Square check | $t_i$ |
|---:|---|---|---|---:|
| 1 | `[0]` | `nums[1] * nums[0] = 2 * 1 = 2` | `2` is not a perfect square. | 0 |
| 2 | `[0]` | `nums[2] * nums[0] = 4 * 1 = 4` | `4` is a perfect square. | 1 |

The sum of valid ancestor counts is `1`.

**Example 3**

- Input: `n = 4, edges = [[0, 1], [0, 2], [1, 3]], nums = [1, 2, 9, 4]`
- Output: `2`
- Explanation:

| `i` | Ancestors | `nums[i] * nums[ancestor]` | Square check | $t_i$ |
|---:|---|---|---|---:|
| 1 | `[0]` | `nums[1] * nums[0] = 2 * 1 = 2` | `2` is not a perfect square. | 0 |
| 2 | `[0]` | `nums[2] * nums[0] = 9 * 1 = 9` | `9` is a perfect square. | 1 |
| 3 | `[1, 0]` | `nums[3] * nums[1] = 4 * 2 = 8`<br>`nums[3] * nums[0] = 4 * 1 = 4` | Only `4` is a perfect square. | 1 |

Therefore the total is `0 + 1 + 1 = 2`.
