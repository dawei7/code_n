## Examples

**Example 1**

- **Input:** `root = [3, 5, 4, 2, null, 1, 1, 1, 0], result = true`
- **Output:** `2`
- **Explanation:** The tree encodes an AND expression at the root. Flipping 2 leaves allows the root to evaluate to `true`.

**Example 2**

- **Input:** `root = [0], result = false`
- **Output:** `0`
- **Explanation:** The single leaf node already has value `0` (false), matching `result = false`, so 0 flips are needed.
