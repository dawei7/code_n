## Function Contract

**Input**

- `arr`: an integer array with length $n$.

**Return value**

Return the number of positions whose value `x` has `x + 1` present anywhere in `arr`.

The test is based on presence, not one-to-one pairing. A single occurrence of `x + 1` can make every occurrence of `x` qualify, while extra copies of `x + 1` do not increase the contribution of one `x`.
