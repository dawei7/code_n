## General
**Characterize numbers with three divisors**

If

$$
n=\prod_i p_i^{e_i}
$$

is the prime factorization of $n$, then its number of positive divisors is
$\prod_i(e_i+1)$. This product equals 3 only when there is exactly one prime
factor and its exponent is 2. Therefore $n$ has exactly three divisors if and
only if $n=p^2$ for some prime $p$; those divisors are $1,p,p^2$.

**Check the square root and its primality**

Compute the integer square root $r=\lfloor\sqrt n\rfloor$. If $r^2\ne n$,
then `n` is not a perfect square and cannot qualify. The value 1 must also be
rejected because it is not prime.

For a remaining perfect square, test whether $r$ has any divisor from 2
through $\lfloor\sqrt r\rfloor$. Finding one makes $r$ composite and the answer
false. Finding none proves $r$ prime, so `n` is its prime square and has
exactly three divisors.

## Complexity detail
The primality loop checks up to $\sqrt r$ candidates. Since $r=\sqrt N$, this
is $O(\sqrt[4]{N})$ time. Integer square-root calculation and loop variables
use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Count every divisor:** Test all integers from 1 through `n` and count exact
  divisions. It follows the definition but costs $O(N)$ time.
- **Enumerate divisor pairs:** Scan through $\lfloor\sqrt N\rfloor$ and add one
  or two divisors per factor pair. This is correct in $O(\sqrt N)$ time but
  does more work than testing the prime-square characterization.
- `n = 1` is a perfect square but has only one divisor.
- The square of 2 is the smallest qualifying value.
- Squares of composite numbers have more than three divisors.
- A prime number itself has two divisors, not three.
- Non-square values can be rejected before any primality loop.
