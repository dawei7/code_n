## Examples

**Example 1**

- Input: `head = [1, 2, 3, 4, 5], k = 2`
- Output: `[4, 5, 1, 2, 3]`

The independent diagram shows the same two-place right rotation:

```text
1 → 2 → 3 → 4 → 5
            ╰──────→ 4 → 5 → 1 → 2 → 3
```

**Example 2**

- Input: `head = [0, 1, 2], k = 4`
- Output: `[2, 0, 1]`

Four rotations are equivalent to one rotation for a three-node list:

```text
0 → 1 → 2  --right by 4-->  2 → 0 → 1
```
