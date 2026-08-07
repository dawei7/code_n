## Function Contract

**Inputs**

- `nodes`: The app encoding in `next` order as `[value, random_index]` pairs, with a zero-based index or `null` in each second position.

**Return value**

Return an independently allocated copy with the same values and pointer relationships. The native LeetCode interface returns the copied `Node` head.
