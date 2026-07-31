## General

An `n`-digit decimal representation can contribute at most $9n$ to its digit sum. Therefore `s > 9 * n` is impossible. When `s = 0`, placing zero in every available position naturally evaluates to the required integer `0`.

For a feasible positive sum, maximize the most significant digit first. Put `min(9, s)` in the leftmost position, subtract it from the remaining sum, and repeat for every later position. Once the remaining sum becomes zero, the later digits stay zero. Using all `n` positions is beneficial for every positive sum: those trailing zeros multiply the already positive prefix by powers of ten without changing its digit sum.

To see why the greedy choice is maximal, suppose a candidate leaves room in an earlier digit while a later digit is positive. Moving one unit from the later digit to the earlier digit preserves the total digit sum and increases the integer, because the earlier place value is larger. Repeating this exchange forces each earlier position to reach nine before any later position receives a unit. That is exactly the constructed sequence, so no other valid integer is larger.

## Complexity detail

The construction visits exactly `n` digit positions and performs constant work at each one, taking $O(n)$ time and $O(1)$ auxiliary space.

The legal source domain fixes $1\le n\le5$ and $0\le s\le100$, leaving only 505 input pairs and at most five loop iterations. The package therefore uses a bounded-domain certificate instead of pretending that meaningful runtime scaling tiers exist.

## Alternatives and edge cases

- **Enumerate every integer:** Checking all values through $10^n-1$ can find the same maximum, but it wastes up to 100,000 candidates and does not use the positional structure.
- **Dynamic programming over positions and sum:** A digit DP can optimize the result, but the exchange argument makes its state table unnecessary.
- **Impossible sum:** Return `-1` immediately when `s > 9 * n` because even all-nine digits are insufficient.
- **Zero sum:** The loop builds zero, which is the only non-negative integer whose digit sum is zero.
- **Positive sum below nine:** Put the entire sum in the first digit and use trailing zeros, such as `10000` for `n = 5, s = 1`.
- **Maximum feasible sum:** When `s = 9 * n`, every digit is nine.
