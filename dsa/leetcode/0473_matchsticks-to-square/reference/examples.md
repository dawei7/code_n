## Examples

**Example 1**

- Input: `matchsticks = [1, 1, 2, 2, 2]`
- Output: `true`
- Explanation: A square of side length 2 is possible. Three sides each use one length-2 stick, while the remaining
  side joins the two length-1 sticks.

| Side | Matchsticks used | Total length |
|---|---|---:|
| Top | `2` | 2 |
| Right | `2` | 2 |
| Bottom | `2` | 2 |
| Left | `1 + 1` | 2 |

**Example 2**

- Input: `matchsticks = [3, 3, 3, 3, 4]`
- Output: `false`
- Explanation: No assignment of all five sticks produces four sides with one common length.
