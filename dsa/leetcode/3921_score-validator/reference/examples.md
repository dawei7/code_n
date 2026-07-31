## Examples

**Example 1**

- Input: `events = ["1","4","W","6","WD"]`
- Output: `[12,1]`
- **Explanation:** The state after each event is:

  | Event | Score | Counter |
  |---|---:|---:|
  | `"1"` | 1 | 0 |
  | `"4"` | 5 | 0 |
  | `"W"` | 5 | 1 |
  | `"6"` | 11 | 1 |
  | `"WD"` | 12 | 1 |

  The final pair is `[12, 1]`.

**Example 2**

- Input: `events = ["WD","NB","0","4","4"]`
- Output: `[10,0]`
- **Explanation:** Neither symbolic scoring event changes the counter, and `"0"` adds no points:

  | Event | Score | Counter |
  |---|---:|---:|
  | `"WD"` | 1 | 0 |
  | `"NB"` | 2 | 0 |
  | `"0"` | 2 | 0 |
  | `"4"` | 6 | 0 |
  | `"4"` | 10 | 0 |

  The final pair is `[10, 0]`.

**Example 3**

- Input: `events = ["W","W","W","W","W","W","W","W","W","W","W"]`
- Output: `[0,10]`
- **Explanation:** The tenth `"W"` raises the counter to `10`, so processing stops immediately and the final `"W"` is ignored. No event adds to the score.
