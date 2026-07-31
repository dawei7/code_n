## Examples

**Example 1**

- Input: `s = "ab1z9"`
- Output: `3`
- Explanation: The represented mirror pairs have these frequencies and contributions:

| `c` | `m` | `freq(c)` | `freq(m)` | `\|freq(c) - freq(m)\|` |
|---|---|---:|---:|---:|
| `a` | `z` | 1 | 1 | 0 |
| `b` | `y` | 1 | 0 | 1 |
| `1` | `8` | 1 | 0 | 1 |
| `9` | `0` | 1 | 0 | 1 |

Thus the total is `0 + 1 + 1 + 1 = 3`.

**Example 2**

- Input: `s = "4m7n"`
- Output: `2`
- Explanation: The relevant pairs are:

| `c` | `m` | `freq(c)` | `freq(m)` | `\|freq(c) - freq(m)\|` |
|---|---|---:|---:|---:|
| `4` | `5` | 1 | 0 | 1 |
| `m` | `n` | 1 | 1 | 0 |
| `7` | `2` | 1 | 0 | 1 |

Their contributions sum to `1 + 0 + 1 = 2`.

**Example 3**

- Input: `s = "byby"`
- Output: `0`
- Explanation: Only one mirror pair is represented:

| `c` | `m` | `freq(c)` | `freq(m)` | `\|freq(c) - freq(m)\|` |
|---|---|---:|---:|---:|
| `b` | `y` | 2 | 2 | 0 |

The two frequencies agree, so the result is `0`.
