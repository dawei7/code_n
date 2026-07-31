## Examples

**Example 1**

```text
y
4   A────────────┐
    │            │
2   │      B─────┼─────────────────┐
0   A──────┼─────┘                 │
-1         B───────────────────────┘
    -3     0     3                 9   x

A: 6 × 4 = 24, B: 9 × 3 = 27, overlap: 3 × 2 = 6
union: 24 + 27 - 6 = 45
```

- Input: `ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2`
- Output: `45`

**Example 2**

- Input: `ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2`
- Output: `16`
