## Examples

**Example 1**

- Input: `root = [4, 2, 5, 1, 3]`
- Output: `[1, 2, 3, 4, 5]`
- Explanation: The transformed structure uses `right` for the solid successor relationships and `left` for the
  dashed predecessor relationships shown in the source figures.

The returned head is node `1`; one complete traversal through successor links reads:

| Start | Successor traversal | Wraparound |
|---:|---|---|
| 1 | `1 -> 2 -> 3 -> 4 -> 5` | `5 -> 1` |

The complete predecessor/successor relationship table is:

| Node | Predecessor through `left` | Successor through `right` |
|---:|---:|---:|
| 1 | 5 | 2 |
| 2 | 1 | 3 |
| 3 | 2 | 4 |
| 4 | 3 | 5 |
| 5 | 4 | 1 |

**Example 2**

- Input: `root = [2, 1, 3]`
- Output: `[1, 2, 3]`
