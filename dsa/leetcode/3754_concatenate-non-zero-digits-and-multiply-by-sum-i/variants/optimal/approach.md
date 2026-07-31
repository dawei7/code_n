## General

Process the decimal representation of `n` from left to right. Maintain the concatenated value and the sum of retained digits.

When the current digit is zero, skip it. For a nonzero digit $d$, appending it to the decimal concatenation changes `x` to `10 * x + d`; add $d$ to the digit sum at the same time. This update preserves the original order because digits are appended exactly when encountered.

After the scan, the two accumulators contain precisely the values defined by the statement, so their product is the answer. If `n = 0`, the scan retains nothing and both accumulators remain zero, satisfying the explicit empty-concatenation rule.

## Complexity detail

Let $D$ be the decimal digit count of `n`. Converting and scanning the representation takes $O(D)$ time, and storing that representation uses $O(D)$ auxiliary space. Under the source bound $n\le10^9$, $D\le10$.

## Alternatives and edge cases

- **Arithmetic digit extraction:** Repeated division and remainder avoids string conversion but obtains digits right to left, so retained digits must be stored or reconstructed carefully.
- **Filter then parse:** Building a filtered string and separately summing it is correct, but performs additional passes over the same bounded digits.
- **Input zero:** There are no nonzero digits, so `x = 0`, `sum = 0`, and the result is `0`.
- **Internal and repeated zeros:** Every zero is omitted without changing the relative order of the surrounding nonzero digits.
- **No zero digits:** Then `x == n`, and the result is `n` multiplied by its ordinary digit sum.
- **Trailing zeros:** They contribute neither a digit nor a place in `x`; for example, `1000` becomes `1`, not `1000`.
