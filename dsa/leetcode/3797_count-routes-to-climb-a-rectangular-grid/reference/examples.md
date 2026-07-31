## Examples

**Example 1**

- Input: `grid = ["..","#."], d = 1`
- Output: `2`
- Explanation: Numbering visited cells in order, the two routes are:

```text
top     . 2
bottom  # 1
```

```text
top     3 2
bottom  # 1
```

The move from `(1, 1)` to `(0, 1)` has distance $\sqrt{(1-0)^2+(1-1)^2}=\sqrt{1}\leq d$. A direct move from `(1, 1)` to `(0, 0)` would instead have distance $\sqrt{2}>d$, so it is unavailable when `d = 1`.

**Example 2**

- Input: `grid = ["..","#."], d = 2`
- Output: `4`
- Explanation: The two routes from Example 1 remain valid. The larger distance also permits these two routes:

```text
top     2 .
bottom  # 1
```

```text
top     2 3
bottom  # 1
```

In particular, moving from `(1, 1)` to `(0, 0)` is now allowed because $\sqrt{2}\leq d$.

**Example 3**

- Input: `grid = ["#"], d = 750`
- Output: `0`
- Explanation: The only bottom-row cell is blocked, so no starting cell and therefore no route exists.

**Example 4**

- Input: `grid = [".."], d = 1`
- Output: `4`
- Explanation: Because the only row is both bottom and top, the four routes are the two one-cell choices and the two directed same-row moves:

```text
row  1 .
```

```text
row  . 1
```

```text
row  1 2
```

```text
row  2 1
```
