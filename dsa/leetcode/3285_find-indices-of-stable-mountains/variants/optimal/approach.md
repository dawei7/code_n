## General

**Test the predecessor, then emit its successor**

Index `0` cannot qualify because it has no preceding mountain. For each index from `1` through `n - 1`, compare `height[index - 1]` with `threshold`. Append the current index exactly when that predecessor is strictly greater.

This is a direct translation of the definition. Every appended index has the required predecessor property, and every stable index is visited and appended during its only check. Iterating in increasing order also produces a deterministic ascending result, even though any output order is accepted.

## Complexity detail

The scan performs one comparison for each of $n-1$ candidate indices, using $O(n)$ time and $O(1)$ auxiliary space beyond the required output list. The output itself may contain $n-1$ indices.

## Alternatives and edge cases

- **Inspect the current mountain:** Stability depends on `height[index - 1]`, not `height[index]`.
- **Use a non-strict comparison:** A predecessor equal to `threshold` does not qualify.
- **Sort the mountains:** Reordering destroys the predecessor relationship and changes indices.
- Mountain `0` is excluded regardless of the first height.
- The final height can never make another mountain stable because it has no successor.
- If every predecessor exceeds the threshold, the result is `[1, 2, ..., n - 1]`.
- If none exceeds it, return an empty list.
- Alternating high and low predecessors produce separated stable indices.
