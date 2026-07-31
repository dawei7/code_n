## Function Contract

**Inputs**

- `points`: An array of Cartesian coordinates, with each entry containing exactly `[x_i, y_i]`.

Every point must be assigned to one of exactly two non-empty groups. Pair order does not matter, and only pairs whose two endpoints are in the same group contribute to that split's minimum.

**Return value**

Return the maximum, over all valid two-group assignments, of the minimum intra-group Manhattan distance. Apply the special value from the Note when neither group contains a pair.
