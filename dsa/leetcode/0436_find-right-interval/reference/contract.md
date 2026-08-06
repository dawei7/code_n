## Function Contract

**Inputs**

- `intervals`: A list of two-element intervals `[start_i, end_i]` with unique start points.

**Return value**

Return one integer per input interval in the same order. Each value is the original index of the qualifying interval
with the smallest start, or `-1` when none exists.
