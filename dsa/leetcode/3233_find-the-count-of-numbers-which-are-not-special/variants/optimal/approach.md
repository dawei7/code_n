## General

**Characterize special numbers.** A special value has exactly three positive divisors after including the number itself. If $x=\prod p_i^{a_i}$, its divisor count is $\prod(a_i+1)$. This product equals the prime number $3$ only when $x=p^2$ for one prime $p$. Therefore the special values are exactly the squares of primes.

**Sieve only possible roots.** No special value at most `r` can have a prime root greater than $m=\lfloor\sqrt{\texttt{r}}\rfloor$. Use the Sieve of Eratosthenes to mark all primes from $2$ through $m$.

A prime root $p$ contributes a special value in the interval exactly when $l\le p^2\le r$. The smallest eligible root is $\lfloor\sqrt{l-1}\rfloor+1$, which avoids floating-point rounding and handles a square lower endpoint correctly. Count marked primes from that root through $m$, then subtract this count from $r-l+1$.

The divisor characterization proves that every subtracted value is special and that no other special value is missed. Squaring is one-to-one on positive roots, so each eligible prime is subtracted exactly once.

## Complexity detail

Let $m=\lfloor\sqrt{\texttt{r}}\rfloor$. Building the sieve takes $O(m\log\log m)$ time and scanning the eligible roots takes $O(m)$ time, for $O(\sqrt r\log\log\sqrt r)$ overall. The primality array uses $O(\sqrt r)$ auxiliary space.

## Alternatives and edge cases

- **Test every interval value's divisors:** This depends on the potentially billion-element interval and is far too slow.
- **Trial-divide every possible root:** It finds the same prime squares but takes up to $O(m\sqrt m)$ time.
- **Treat every perfect square as special:** A composite root has more than three total divisors, so values such as $16=4^2$ are not special.
- `1` is not special because it has no proper divisors.
- A singleton interval containing a prime square returns zero.
- A square lower endpoint must be included, which is why the lower root uses $\sqrt{l-1}$.
- The integer square root avoids precision errors near $10^9$.
- If no prime square lies in the interval, the full interval length is returned.
