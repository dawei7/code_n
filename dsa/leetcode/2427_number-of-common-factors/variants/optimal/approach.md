## General

**Reduce two divisibility tests to one.** A positive integer divides both `a` and `b` exactly when it divides their greatest common divisor $g$. Compute $g=\gcd(a,b)$ first; the answer is then the number of positive divisors of $g$.

**Count complementary divisor pairs.** Test candidates $d$ starting at 1 while $d^2\le g$. Whenever $d$ divides $g$, both $d$ and $g/d$ are divisors. Add two for this pair unless $d^2=g$, in which case the square root is one divisor and must be counted only once.

Every divisor below $\sqrt g$ is paired with a distinct divisor above $\sqrt g$, and a perfect square has exactly one unpaired middle divisor. The loop therefore counts every divisor of $g$ once and only once.

## Complexity detail

Euclid's algorithm computes the greatest common divisor in $O(\log \min(a,b))$ time. The divisor loop performs $\lfloor\sqrt g\rfloor$ iterations, so the combined bound is $O(\sqrt g)$ for positive integer inputs. Only a fixed number of integers is stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Scan through the smaller input:** Testing every integer from 1 through `min(a, b)` is correct but takes $O(\min(a,b))$ time.
- **Prime factorization:** If $g=\prod p_i^{e_i}$, the divisor count is $\prod(e_i+1)$; trial factorization has a similar square-root bound but more bookkeeping.
- **Coprime inputs:** Their greatest common divisor is 1, which has exactly one positive divisor.
- **One input is 1:** The answer is always 1.
- **Equal inputs:** Count every divisor of that shared value.
- **Perfect-square greatest common divisor:** Its square-root divisor must not be double-counted.
- **One input divides the other:** The answer is the divisor count of the smaller input.
