## Function Contract

**Inputs**

- `n`: The positive integer that begins as the only current part.

Every operation chooses a part `x > 1` and positive integers `a` and `b` satisfying `a + b = x`. It replaces `x` by those two parts and adds `a * b` to the running cost.

The process finishes only when its multiset of parts contains `n` copies of `1` and nothing else.

**Return value**

Return the minimum possible sum of all operation costs over a complete sequence of splits.
