## Examples

**Example 1**

- Input: `n = 5, k = 3`
- Output: `3`
- **Explanation:** All length-three positive sequences with sum 5 are listed below in the same order as the source example.

| Sequence | Product | Parity |
|---|---|---|
| `[1,1,3]` | `1 * 1 * 3 = 3` | Odd |
| `[1,2,2]` | `1 * 2 * 2 = 4` | Even |
| `[2,1,2]` | `2 * 1 * 2 = 4` | Even |
| `[2,2,1]` | `2 * 2 * 1 = 4` | Even |
| `[1,3,1]` | `1 * 3 * 1 = 3` | Odd |
| `[3,1,1]` | `3 * 1 * 1 = 3` | Odd |

Exactly three rows have an even product, so the answer is 3.

**Example 2**

- Input: `n = 3, k = 2`
- Output: `2`
- **Explanation:** The complete set of length-two positive sequences with sum 3 is:

| Sequence | Product | Parity |
|---|---|---|
| `[1,2]` | `1 * 2 = 2` | Even |
| `[2,1]` | `2 * 1 = 2` | Even |

Both products are even, giving two valid sequences.

**Example 3**

- Input: `n = 5, k = 5`
- Output: `0`
- **Explanation:** Positivity and the required sum force the sole sequence `[1,1,1,1,1]`. Its product is odd, so no valid sequence exists.
