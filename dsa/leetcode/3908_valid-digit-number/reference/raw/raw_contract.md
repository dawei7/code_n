## Function Contract

**Inputs**

- `n`: A nonnegative integer whose decimal digits are inspected.
- `x`: One decimal digit from `0` through `9`.

The decimal representation has no leading zeros. In particular, the representation of `0` is the one-character sequence `0`. An occurrence at the first position satisfies the containment condition but simultaneously violates the leading-digit condition.

**Return value**

Return `true` when the decimal representation of `n` contains `x` at least once and its first digit is not `x`. Return `false` in every other case.
