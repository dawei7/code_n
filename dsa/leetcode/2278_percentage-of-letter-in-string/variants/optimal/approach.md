## General

**Count exact character matches**

Scan `s` once and count positions whose character equals `letter`. Every
position contributes either one match or none, so the final counter is exactly
the numerator's occurrence count.

**Use integer division to implement round-down semantics**

Multiply the match count by 100 before dividing by the nonzero string length.
For nonnegative integers, `matches * 100 // len(s)` equals

$$
\left\lfloor\frac{100\cdot\text{matches}}{\lvert s\rvert}\right\rfloor.
$$

This performs the specified round down directly and avoids floating-point
representation or a separate rounding operation.

Because the scan counts every and only matching position, substituting its
result into the percentage formula gives the exact real percentage before
flooring. Integer division then returns precisely the required whole percent.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Counting examines all $n$ characters once, so
time is $O(n)$. The counter and arithmetic values use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Floating-point division plus floor:** This can produce the same result, but integer arithmetic states the required truncation directly and avoids precision concerns.
- **Round to nearest integer:** Standard rounding is incorrect because every fractional percentage must be rounded down.
- **Repeated prefix counts:** Recounting each growing prefix eventually obtains the right total but takes $O(n^2)$ time.
- **No occurrence:** A zero numerator returns 0.
- **Every character matches:** The numerator equals the denominator, so the result is 100.
- **One-character string:** The only possible results are 0 and 100.
- **Non-integral percentage:** Values such as one match in three positions return 33, not 34.
- **Multiply before dividing:** Computing `matches // len(s) * 100` would incorrectly return zero for every proper fraction.
