## Examples

**Example 1**

- Input: `grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]`
- Output: `16`
- **Explanation:** The source image marks the island's `16` exposed unit edges. The accessible table below reproduces the same grid; each land entry shows how many of that cell's sides are exposed.

| Row $\backslash$ column | 0 | 1 | 2 | 3 |
|---:|:---:|:---:|:---:|:---:|
| 0 | Water | Land (3) | Water | Water |
| 1 | Land (3) | Land (0) | Land (3) | Water |
| 2 | Water | Land (2) | Water | Water |
| 3 | Land (3) | Land (2) | Water | Water |

The exposed-side counts sum to $3 + 3 + 0 + 3 + 2 + 3 + 2 = 16$.

**Example 2**

- Input: `grid = [[1]]`
- Output: `4`

**Example 3**

- Input: `grid = [[1,0]]`
- Output: `4`
