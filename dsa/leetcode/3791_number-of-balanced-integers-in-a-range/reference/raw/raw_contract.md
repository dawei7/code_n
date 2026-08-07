## Function Contract

**Inputs**

- `low`: The inclusive lower endpoint of the range.
- `high`: The inclusive upper endpoint, with `high >= low`.

Position parity is determined from the actual leftmost digit of each integer; leading zeros are not part of its representation. One-digit values never qualify.

**Return value**

Return the count of integers `x` satisfying `low <= x <= high`, having at least two digits, and having equal odd-position and even-position digit sums.
