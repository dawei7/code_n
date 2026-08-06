## Examples

**Example 1**

- **Input:** `poly1 = [[1,1]], poly2 = [[1,0]]`
- **Output:** `[[1,1],[1,0]]`
- **Explanation:** $x + 1 = x + 1$.

**Example 2**

- **Input:** `poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]`
- **Output:** `[[5,2],[2,0]]`
- **Explanation:** $(2x^2 + 4x + 3) + (3x^2 - 4x - 1) = 5x^2 + 2$. The $x^1$ terms cancel out.

**Example 3**

- **Input:** `poly1 = [[1,2]], poly2 = [[-1,2]]`
- **Output:** `[]`
- **Explanation:** $x^2 + (-x^2) = 0$, producing an empty list for the zero polynomial.
