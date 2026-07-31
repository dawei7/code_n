## Examples

**Example 1**

- Input: `operations = ["TicTacToe","move","move","move","move","move","move","move"], arguments = [[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]`
- Output: `[null,0,0,0,0,0,0,1]`
- Explanation: Let player `1` use `X` and player `2` use `O`. The complete board sequence is:

```text
move(0,0,1) -> 0    move(0,2,2) -> 0    move(2,2,1) -> 0
X . .                X . O                X . O
. . .                . . .                . . .
. . .                . . .                . . X

move(1,1,2) -> 0    move(2,0,1) -> 0    move(1,0,2) -> 0
X . O                X . O                X . O
. O .                . O .                O O .
. . X                X . X                X . X

move(2,1,1) -> 1
X . O
O O .
X X X    player 1 wins
```
