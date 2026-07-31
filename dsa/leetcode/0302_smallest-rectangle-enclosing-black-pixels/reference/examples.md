## Examples

**Example 1**

- Input: `image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2`
- Output: `6`

The black component occupies rows `0..2` and columns `1..2`, so its enclosing rectangle has height `3` and width `2`:

```text
image       enclosing rectangle
. . # .       [ . # ]
. # # .       [ # # ]
. # . .       [ # . ]

area = 3 * 2 = 6
```

**Example 2**

- Input: `image = [["1"]], x = 0, y = 0`
- Output: `1`
