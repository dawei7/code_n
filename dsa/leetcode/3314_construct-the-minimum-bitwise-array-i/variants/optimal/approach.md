## General

Consider the binary form of a candidate $x$. Adding one changes its trailing run of one-bits to zeros and sets the zero immediately to their left. Consequently, `x | (x + 1)` keeps all higher bits of $x$ and turns that lowest zero plus every lower position into ones. Every value produced by this operation is odd, so the only legal even prime, 2, has no answer.

For an odd prime $p$, suppose its binary representation ends in $k\geq1$ consecutive one-bits. Any valid $x$ is obtained by clearing one of those trailing one-bits in $p$: the increment restores that bit, and the OR restores all lower bits. To minimize $x$, clear the most significant bit within that trailing run, which has value $2^{k-1}$.

The lowest set bit of `p + 1` is $2^k$, because the increment carries through all $k$ trailing ones. Halving that isolated bit gives $2^{k-1}$, and XOR clears it from $p$. Thus the candidate is computed directly as `p ^ (((p + 1) & -(p + 1)) >> 1)`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $M=\max(\texttt{nums})$. Each element uses a constant number of arithmetic and bitwise operations on $O(\log M)$-bit integers, for $O(n\log M)$ bit-operation time. The returned array uses $O(n)$ space; aside from that output, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try every smaller integer:** Testing candidates from zero upward is source-faithful but costs $O(nM\log M)$ bit-operation time in the worst case.
- **Scan bit positions:** Finding the first zero above the trailing one-run and clearing the preceding bit takes $O(n\log M)$ time but is more verbose than isolating the bit arithmetically.
- **Prime 2:** OR-ing consecutive non-negative integers always produces an odd value, so its answer is `-1`.
- **A long suffix of ones:** For values such as 31, clearing the highest trailing one produces 15, which is smaller than clearing any lower one.
- **A single trailing one:** When $p\equiv1\pmod4$, the answer is simply $p-1$.
