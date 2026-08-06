## Examples

**Example 1**

- Input: `room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3`
- Output: `Robot cleaned all rooms.`
- **Explanation:** Each grid entry is `0` for a blocked cell or `1` for an accessible cell. The robot starts at
  `(1, 3)`, which is one row below and three columns to the right of the top-left corner.

The source illustration conveys the same layout and starting position represented accessibly below. `S↑` is the
open starting cell and its initial upward orientation.

| Row \ Column | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | S↑ | 1 | 0 | 1 | 1 |
| 2 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Example 2**

- Input: `room = [[1]], row = 0, col = 0`
- Output: `Robot cleaned all rooms.`
