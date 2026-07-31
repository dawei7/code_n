## Examples

**Example 1**

- Input: `heights = [2, 1, 5, 6, 2, 3]`
- Output: `10`
- Explanation: Every bar has width `1`. In the independent diagram, `▓` marks the largest rectangle: it spans the two bars of heights `5` and `6` up to height `5`, for area $2 \times 5 = 10$.

```text
      █
    ▓ ▓
    ▓ ▓
    ▓ ▓   █
█   ▓ ▓ █ █
█ █ ▓ ▓ █ █
```

**Example 2**

- Input: `heights = [2, 4]`
- Output: `4`

```text
  █
  █
█ █
█ █
```
