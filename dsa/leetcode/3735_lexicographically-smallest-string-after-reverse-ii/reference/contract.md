## Function Contract

**Inputs**

- `s`: The lowercase string on which one prefix or suffix reversal must be performed.

Both reversal endpoints are inclusive within the selected prefix or suffix. Choosing `k = 1` is legal and leaves the visible string unchanged, while still satisfying the exactly-one-operation requirement.

**Return value**

Return the smallest result in lexicographic order among all `2n` legal prefix- and suffix-reversal choices.
