## Examples

**Example 1**

- **Input:** `root1 = ["+", "a", "+", null, null, "b", "c"]`, `root2 = ["+", "+", "a", "b", "c"]`
- **Output:** `true`
- **Explanation:** The trees represent `a + (b + c)` and `(b + c) + a`. Both contain variables `a`, `b`, and `c` each with count 1.

**Example 2**

- **Input:** `root1 = ["+", "a", "+", null, null, "b", "c"]`, `root2 = ["+", "+", "a", "b", "d"]`
- **Output:** `false`
- **Explanation:** The first expression contains `c`, while the second contains `d`.

**Example 3**

- **Input:** `root1 = ["+", "a", "a"]`, `root2 = ["+", "a", "b"]`
- **Output:** `false`
- **Explanation:** Repeated variables are coefficients; `a + a` is not equivalent to `a + b`.
