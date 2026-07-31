## General

When one is added to an integer $x$, its trailing one-bits become zeros and the zero immediately to their left becomes one. The expression `x | (x + 1)` therefore keeps all higher bits and makes that changed bit and every lower bit equal to one. Its result is always odd, so the even prime 2 cannot be produced.

Let an odd prime $p$ end in $k\geq1$ consecutive one-bits. A valid predecessor can be obtained by clearing one bit in that suffix: incrementing then restores the cleared position, while OR restores all lower suffix bits. The smallest predecessor results from clearing the highest bit in the suffix, whose value is $2^{k-1}$.

Adding one to $p$ carries through the suffix, so the lowest set bit of `p + 1` is $2^k$. Isolate it with `(p + 1) & -(p + 1)`, shift it right once, and XOR that bit out of $p$. This directly yields the minimum answer without trying any candidates, even when $p$ is close to $10^9$.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $M=\max(\texttt{nums})$. A constant number of operations is performed on each $O(\log M)$-bit integer, giving $O(n\log M)$ bit-operation time. The output requires $O(n)$ space, while auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Test every smaller number:** This can require $O(nM\log M)$ bit-operation time and is infeasible when a prime approaches $10^9$.
- **Scan all bit positions:** Locating the trailing one-run explicitly is correct in $O(n\log M)$ time but more verbose than isolating the carry bit.
- **Prime 2:** No consecutive non-negative pair has an even bitwise OR, so return `-1`.
- **All-one values:** For a prime such as 31, clearing the highest suffix bit produces the minimum value 15.
- **Large primes:** The arithmetic uses the value's bit width rather than its magnitude, which is the distinction from the smaller-domain version.
