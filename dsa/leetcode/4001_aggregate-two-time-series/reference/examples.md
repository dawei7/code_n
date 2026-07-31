## Examples

**Example 1**

- Input: `series1 = [[1,3],[4,1]], series2 = [[2,2],[5,2]]`
- Output: `[[1,5],[2,3],[4,3],[5,2]]`
- **Explanation:** The next available values at every timestamp in the union are shown below.

| Timestamp | `series1` | `series2` | `summedValue` |
|---:|---:|---:|---:|
| 1 | 3 | 2 | 5 |
| 2 | 1 | 2 | 3 |
| 4 | 1 | 2 | 3 |
| 5 | 0 | 2 | 2 |

Thus the aggregated series is `[[1,5],[2,3],[4,3],[5,2]]`.

**Example 2**

- Input: `series1 = [[1,5],[3,1]], series2 = [[2,2]]`
- Output: `[[1,7],[2,3],[3,1]]`
- **Explanation:** Each missing value again comes from the next entry in that same series.

| Timestamp | `series1` | `series2` | `summedValue` |
|---:|---:|---:|---:|
| 1 | 5 | 2 | 7 |
| 2 | 1 | 2 | 3 |
| 3 | 1 | 0 | 1 |

Therefore the result is `[[1,7],[2,3],[3,1]]`.

**Example 3**

- Input: `series1 = [[1,5]], series2 = [[1000000000,2]]`
- Output: `[[1,7],[1000000000,2]]`
- **Explanation:** At timestamp 1, `series2` contributes its next available value, 2, from timestamp 1000000000. At timestamp 1000000000, `series1` has no later entry and contributes zero. Only these two timestamps appear because the output includes timestamps present in at least one input series.
