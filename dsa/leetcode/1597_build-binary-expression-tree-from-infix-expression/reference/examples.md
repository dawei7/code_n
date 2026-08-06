## Examples

**Example 1**

- **Input:** `s = "3*4-2*5"`
- **Output:** `[-, *, *, 3, 4, 2, 5]`
- **Explanation:** Tree rooted at `'-'`, with `3*4` as its left subtree and `2*5` as its right subtree.

**Example 2**

- **Input:** `s = "2-3/(5*2)+1"`
- **Output:** `[+, -, 1, 2, /, null, null, null, null, 3, *, null, null, 5, 2]`
- **Explanation:** Tree representing `(2 - (3 / (5 * 2))) + 1`.

**Example 3**

- **Input:** `s = "1+2+3+4+5"`
- **Output:** `[+, +, 5, +, 4, null, null, +, 3, null, null, +, 2, null, null, 1]`
- **Explanation:** Left-associated addition tree representing `((((1+2)+3)+4)+5)`.
