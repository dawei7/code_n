## Examples

**Example 1**

- Input: `grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]`
- Output: `4`
- Explanation: One first path is `(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (2,3) -> (3,3) -> (4,3)`. One second path is `(4,0) -> (4,1) -> (3,1) -> (2,1) -> (2,2) -> (2,3) -> (1,3) -> (0,3)`. Their shared cells are `(2,1)`, `(2,2)`, and `(2,3)`, whose values sum to $2+(-1)+3=4$.

The table independently preserves the path relationships shown in the source illustration. `P1` marks only the first path, `P2` marks only the second path, and `Both` marks their intersection.

| Row $\backslash$ column | 0 | 1 | 2 | 3 |
|---:|:---:|:---:|:---:|:---:|
| 0 | `1 · P1` | `2` | `0` | `-3 · P2` |
| 1 | `1 · P1` | `-2` | `1` | `0 · P2` |
| 2 | `-4 · P1` | `2 · Both` | `-1 · Both` | `3 · Both` |
| 3 | `3` | `-3 · P2` | `3` | `-2 · P1` |
| 4 | `-1 · P2` | `-5 · P2` | `0` | `1 · P1` |

**Example 2**

- Input: `grid = [[4,-2,-3],[-1,-3,-1],[-4,2,-1]]`
- Output: `3`
- Explanation: Choose the first path `(0,0) -> (1,0) -> (1,1) -> (1,2) -> (2,2)` and the second path `(2,0) -> (1,0) -> (0,0) -> (0,1) -> (0,2)`. The two paths share `(0,0)` and `(1,0)`, so the score is $4+(-1)=3$.

| Row $\backslash$ column | 0 | 1 | 2 |
|---:|:---:|:---:|:---:|
| 0 | `4 · Both` | `-2 · P2` | `-3 · P2` |
| 1 | `-1 · Both` | `-3 · P1` | `-1 · P1` |
| 2 | `-4 · P2` | `2` | `-1 · P1` |
