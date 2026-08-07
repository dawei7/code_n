## Function Contract

**Inputs**

- `d`: the single decimal digit whose occurrences are counted.
- `low`: the inclusive lower bound of the positive-integer range.
- `high`: the inclusive upper bound of the positive-integer range.

Every integer in the closed interval from `low` through `high` is interpreted using its ordinary base-ten representation. Both endpoints contribute, repeated appearances within one representation contribute separately, and omitted leading zeros do not contribute.

**Return value**

- The total number of written occurrences of `d` across all integers in the inclusive range.
