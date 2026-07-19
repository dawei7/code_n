## General
**Determine the only possible missing sum**

All $M + N$ observations must total `mean * (M + N)`. Subtract the sum of
`rolls` to obtain the required missing sum $R$. Since every missing die is
between $1$ and $6$, a reconstruction exists exactly when
$N \le R \le 6N$.

**Distribute the sum evenly**

For a feasible $R$, compute `quotient, remainder = divmod(R, N)`. Use
`remainder` values equal to `quotient + 1` and the other
`N - remainder` values equal to `quotient`. Their sum is
`quotient * N + remainder = R`.

The feasibility bounds ensure the quotient-based values remain legal die
faces: the smaller value is at least `1`, and when the quotient is `6` the
remainder must be zero. The constructed list has exactly $N$ entries and sum
$R$, so combining it with the observed sum produces the required total and
therefore the exact stated average.

## Complexity detail
Summing the $M$ observed rolls takes $O(M)$ time, and materializing the $N$
missing rolls takes $O(N)$ time. The returned list occupies $O(N)$ space;
apart from that required output, the calculation uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Incremental distribution:** Start every missing roll at `1` and distribute
  the remaining amount with at most five additions per position. This is also
  linear but requires more mutation.
- **Repeated list concatenation:** Appending via `answer = answer + [value]`
  rebuilds the growing prefix and can take $O(N^2)$ time.
- A required sum below $N$ is impossible because every die contributes at
  least one.
- A required sum above $6N$ is impossible because no die exceeds six.
- The boundary sums $N$ and $6N$ produce all-one and all-six answers.
- Output ordering is irrelevant; any valid distribution must be accepted.
