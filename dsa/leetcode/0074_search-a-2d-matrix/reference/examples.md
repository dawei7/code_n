## Examples

**Example 1**

- Input: `matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3`
- Output: `true`

The target is marked in this independent rendering:

```text
 1 [3]  5  7
10 11  16 20
23 30  34 60
```

**Example 2**

- Input: `matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13`
- Output: `false`

The ordered matrix contains no value between `11` and `16`:

```text
 1  3   5  7
10 11  16 20    target: 13 (absent)
23 30  34 60
```
