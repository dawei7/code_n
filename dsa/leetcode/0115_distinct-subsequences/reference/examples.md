## Examples

**Example 1**

- Input: `s = "rabbbit", t = "rabbit"`
- Output: `3`
- Explanation: There are three ways to select `rabbit` from `s`. The table lists the selected one-based positions; the resulting characters are `rabbit` in every row.

| Selection | Positions in `s` |
|---|---|
| 1 | `1, 2, 3, 4, 6, 7` |
| 2 | `1, 2, 4, 5, 6, 7` |
| 3 | `1, 2, 3, 5, 6, 7` |

**Example 2**

- Input: `s = "babgbag", t = "bag"`
- Output: `5`
- Explanation: Five distinct choices of positions generate `bag`:

| Selection | Positions in `s` |
|---|---|
| 1 | `1, 2, 4` |
| 2 | `1, 2, 7` |
| 3 | `1, 6, 7` |
| 4 | `3, 6, 7` |
| 5 | `5, 6, 7` |
