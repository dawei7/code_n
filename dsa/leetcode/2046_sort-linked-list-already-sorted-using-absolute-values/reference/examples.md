## Examples

**Example 1**

- **Input:** `head = [0, 2, -5, 5, 10, -10]`
- **Output:** `[-10, -5, 0, 2, 5, 10]`
- **Explanation:** Traversed magnitudes are 0, 2, 5, 5, 10, 10. Moving negative values (-10, -5) to the front produces sorted signed order `[-10, -5, 0, 2, 5, 10]`.

**Example 2**

- **Input:** `head = [0, 1, 2]`
- **Output:** `[0, 1, 2]`
- **Explanation:** All values are non-negative, so the list is already in non-decreasing signed order.

**Example 3**

- **Input:** `head = [1]`
- **Output:** `[1]`
- **Explanation:** A single-element list is already sorted.
