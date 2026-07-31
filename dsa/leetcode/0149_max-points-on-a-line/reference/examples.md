## Examples

**Example 1**

- Input: `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `3`

```text
y
3 |       ●
2 |    ●
1 | ●
  +----------- x
    1  2  3
```

**Example 2**

- Input: `points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]`
- Output: `4`

```text
y
4 | ●
3 |    ●        ●
2 |       ●
1 | ●        ●
  +----------------- x
    1  2  3  4  5

The four points descending from (1, 4) through (4, 1) share one line.
```
