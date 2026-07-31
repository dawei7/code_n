## Examples

**Example 1**

- Input: `head = [1, 2, 3, 4, 5], left = 2, right = 4`
- Output: `[1, 4, 3, 2, 5]`

The independent rendering marks and reverses only positions `2` through `4`:

```text
1 → [2 → 3 → 4] → 5  -->  1 → [4 → 3 → 2] → 5
```

**Example 2**

- Input: `head = [5], left = 1, right = 1`
- Output: `[5]`
