## Examples

**Example 1**

- Input: `nums = [2,6,4]`
- Output: `2`

- **Explanation:** Construct the derived array one position at a time:

| `i` | `nums[i]` | $M_i$ | `prefixGcd[i]` |
|---:|---:|---:|---:|
| 0 | 2 | 2 | 2 |
| 1 | 6 | 6 | 6 |
| 2 | 4 | 6 | 2 |

Thus `prefixGcd = [2,6,2]`, which becomes `[2,2,6]` after sorting. The smallest and largest values form the only pair, and `gcd(2,6) = 2`. The middle `2` remains unpaired, so the returned sum is `2`.

**Example 2**

- Input: `nums = [3,6,2,8]`
- Output: `5`

- **Explanation:** The prefix construction is:

| `i` | `nums[i]` | $M_i$ | `prefixGcd[i]` |
|---:|---:|---:|---:|
| 0 | 3 | 3 | 3 |
| 1 | 6 | 6 | 6 |
| 2 | 2 | 6 | 2 |
| 3 | 8 | 8 | 8 |

Here `prefixGcd = [3,6,2,8]`, and sorting produces `[2,3,6,8]`. The extreme pairs are `(2,8)` and `(3,6)`. Their contributions are `gcd(2,8) = 2` and `gcd(3,6) = 3`, so the total is `2 + 3 = 5`.
