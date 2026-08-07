## Function Contract

**Inputs**

- `n`: The number of bulb positions in the line.
- `brightness`: The minimum number of distinct positions that must be illuminated at every active time.
- `intervals`: Inclusive integer-time intervals `[start, end]` during which the requirement applies.

Let $m$ be the number of intervals.

**Return value**

Return the minimum sum of on-bulb time units needed over the union of all intervals.
