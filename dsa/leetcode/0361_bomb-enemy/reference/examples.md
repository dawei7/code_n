## Examples

**Example 1**

- Input: `grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]`
- Output: `3`

The first source illustration is represented below with `B` marking a best bomb position and `x` marking the three eliminated enemies. The wall prevents the blast from reaching the enemy to its right.

```text
before             bomb at row 1, column 1
0 E 0 0            0 x 0 0
E 0 W E      ->    x B W E
0 E 0 0            0 x 0 0
```

**Example 2**

- Input: `grid = [["W","W","W"],["0","0","0"],["E","E","E"]]`
- Output: `1`

The second source illustration shows that any bomb in the middle row can reach only the enemy directly beneath it.

```text
W W W               W W W
0 0 0       ->      B 0 0
E E E               x E E
```
