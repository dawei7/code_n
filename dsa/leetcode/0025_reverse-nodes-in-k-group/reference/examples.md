## Examples

**Example 1**

- Input: `head = [1, 2, 3, 4, 5], k = 2`
- Output: `[2, 1, 4, 3, 5]`

The source image is reproduced independently:

```text
(1 -> 2) -> (3 -> 4) -> 5    becomes    (2 -> 1) -> (4 -> 3) -> 5
```

**Example 2**

- Input: `head = [1, 2, 3, 4, 5], k = 3`
- Output: `[3, 2, 1, 4, 5]`

The complete three-node group reverses, while the final two nodes remain unchanged:

```text
(1 -> 2 -> 3) -> 4 -> 5    becomes    (3 -> 2 -> 1) -> 4 -> 5
```
