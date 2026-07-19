## General
**Count every shorter length immediately**

Every constructible number with fewer than $d$ digits is automatically smaller than `n`. For length $\ell$, each of the $\ell$ positions has $k$ choices, so begin with

$$
\sum_{\ell=1}^{d-1} k^\ell.
$$

**Match the boundary length from left to right**

Convert `n` to its decimal string. At position `i`, binary-search `digits` for how many available characters are smaller than `n[i]`. Choosing any such smaller character makes the remaining suffix unrestricted, adding `smaller * k ** remaining` constructible numbers.

If `n[i]` is unavailable, no constructible number can keep matching the prefix, so stop. If it is available, continue to the next position. When every position matches, add one for `n` itself.

Every shorter number is counted once by its length. Among $d$-digit numbers, consider the first position where a candidate differs from `n`. The prefix scan counts it exactly at that position when its digit is smaller, followed by every possible suffix; a larger digit is correctly excluded. The only candidate with no differing position is `n`, added exactly when all of its digits are available. These disjoint groups contain precisely all valid integers at most `n`.

## Complexity detail
The $d$ boundary positions each perform a binary search among $k$ digits, taking $O(d\log k)$ time. The running count and a constant number of indices use $O(1)$ auxiliary space; the decimal representation has at most ten characters under the fixed input bound.

## Alternatives and edge cases
- **Digit dynamic programming:** A tight-prefix DP generalizes to zero and repeated constraints, but carries unnecessary state for this zero-free digit set.
- **Enumerate constructible numbers:** Depth-first generation is correct but visits every candidate up to `n` and can grow exponentially with $d$.
- **Test every integer through `n`:** Checking decimal digits directly can take time proportional to `n` and ignores the combinatorial structure.
- **Single available digit:** There is at most one constructible number of each length, and the prefix comparison decides the boundary length.
- **All digits of `n` available:** Add one for `n` after counting numbers that first become smaller at an earlier position.
- **Missing boundary digit:** Stop immediately after adding choices smaller at that position; no equal prefix can continue.
- **`n` shorter than available examples:** Only lengths below $d$ and the valid prefix of length $d$ contribute.
- **Upper bound `1000000000`:** Although `n` has ten digits, its leading `"1"` is handled by the same prefix rule and no generated number may use zero.
