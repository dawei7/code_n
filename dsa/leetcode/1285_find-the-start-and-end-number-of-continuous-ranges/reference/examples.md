## Examples

**Example 1**

- **Input:** `Logs = [[1],[2],[3],[7],[8],[10]]`

`Logs`:

| log_id |
|---:|
| 1 |
| 2 |
| 3 |
| 7 |
| 8 |
| 10 |

- **Output:** `[[1,3],[7,8],[10,10]]`

Result:

| start_id | end_id |
|---:|---:|
| 1 | 3 |
| 7 | 8 |
| 10 | 10 |

- **Explanation:** The result lists every range present in `Logs`. Identifiers `1` through `3` are present, while `4` through `6` are absent. Identifiers `7` and `8` form the next range, `9` is absent, and `10` forms a one-value range.
