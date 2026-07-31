## Examples

**Example 1**

- Input: `m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]`
- Output: `[1,1,2,3]`
- Explanation: The grid starts entirely as water. Adding `(0,0)` creates one island. Adding `(0,1)` joins that island, so the count remains one. Adding `(1,2)` creates a second island. Adding `(2,1)` creates a third island.

```text
initial      add (0,0)    add (0,1)    add (1,2)    add (2,1)
. . .        # . .        # # .        # # .        # # .
. . .   ->   . . .   ->   . . .   ->   . . #   ->   . . #
. . .        . . .        . . .        . . .        . # .

islands:       1            1            2            3
```

**Example 2**

- Input: `m = 1, n = 1, positions = [[0,0]]`
- Output: `[1]`
