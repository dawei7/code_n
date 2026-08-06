## Examples

**Example 1**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]`
- Output: `"lul"`
- **Explanation:** Two shortest routes each travel six empty spaces. Rolling left, up, and left produces `"lul"`,
  while rolling up and left produces `"ul"`. Because `l` precedes `u` lexicographically, `"lul"` is the required
  answer.

The first source diagram is represented below. `B` marks the ball, `H` the hole, `0` another empty space, and `1` a
wall.

| Row \ Column | 0 | 1 | 2 | 3 | 4 |
|---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | H | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 1 | 0 | 0 | 1 |
| 4 | 0 | 1 | 0 | B | 0 |

**Example 2**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [3,0]`
- Output: `"impossible"`
- **Explanation:** No legal sequence of rolls can make the ball enter the hole.

The second source diagram uses the same maze and ball but places `H` at `(3, 0)`.

| Row \ Column | 0 | 1 | 2 | 3 | 4 |
|---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 0 | 0 |
| 3 | H | 1 | 0 | 0 | 1 |
| 4 | 0 | 1 | 0 | B | 0 |

**Example 3**

- Input: `maze = [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]], ball = [0,4], hole = [3,5]`
- Output: `"dldr"`
