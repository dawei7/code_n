## Examples

**Example 1**

- Input: `head = [1, 4, 3, 2, 5, 2], x = 3`
- Output: `[1, 2, 2, 4, 3, 5]`

The independent rendering separates values below `3` while keeping both groups stable:

```text
1 → 4 → 3 → 2 → 5 → 2  -->  1 → 2 → 2 | 4 → 3 → 5
```

**Example 2**

- Input: `head = [2, 1], x = 2`
- Output: `[1, 2]`
