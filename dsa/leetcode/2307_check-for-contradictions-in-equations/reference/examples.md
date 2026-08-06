## Examples

**Example 1**

- **Input:** `equations = [["a", "b"], ["b", "c"], ["a", "c"]], values = [3.0, 0.5, 1.5]`
- **Output:** `false`
- **Explanation:** $a/b = 3.0$ and $b/c = 0.5$ imply $a/c = 3.0 \times 0.5 = 1.5$, which matches $a/c = 1.5$. No contradiction.

**Example 2**

- **Input:** `equations = [["le", "et"], ["le", "code"], ["code", "et"]], values = [2.0, 5.0, 0.5]`
- **Output:** `true`
- **Explanation:** $\text{le}/\text{et} = 2.0$ and $\text{le}/\text{code} = 5.0$ imply $\text{code}/\text{et} = 2.0 / 5.0 = 0.4$. This contradicts the given $\text{code}/\text{et} = 0.5$, so return `true`.
