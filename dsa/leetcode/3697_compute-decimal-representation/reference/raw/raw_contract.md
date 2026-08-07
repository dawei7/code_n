## Function Contract

**Inputs**

- `n`: The positive integer to decompose.

Every returned value must have exactly one nonzero decimal digit and must equal $d\cdot10^p$ for some $d\in\{1,\ldots,9\}$ and integer $p\ge0$. The values must sum exactly to `n`, and their count must be minimal.

**Return value**

Return the minimum-cardinality list of base-10 components in descending order.
