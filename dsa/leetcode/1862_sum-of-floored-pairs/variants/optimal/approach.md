## General
**Aggregate equal values**

Build `frequency[x]`, the number of occurrences of value $x$, and a prefix
count over the value domain. The answer depends on values and multiplicities,
so equal array elements never need to be processed separately.

**Group numerators by one quotient**

Fix a denominator value $d$ that occurs in the array. For a positive integer
$q$, every numerator $x$ in

$$
qd \le x \le (q+1)d-1
$$

satisfies $\lfloor x/d\rfloor=q$. Prefix counts return the number of input
values in this interval in constant time. Multiply that count by $q$ and by
`frequency[d]`, since every occurrence of $d$ forms the same pairs.

Enumerate the intervals by taking lower bounds $d,2d,3d,\ldots$ through $U$.
Values below $d$ contribute zero and can be skipped. These intervals partition
all positive numerator values, so every ordered pair is counted once with
exactly its floor quotient. Reduce the accumulated total modulo $10^9+7$.

## Complexity detail
Counting values and building prefix counts take $O(n+U)$ time. Denominator $d$
visits $\lfloor U/d\rfloor$ ranges, and summing this harmonic series over all
$d$ is $O(U\log U)$. The frequency and prefix arrays use $O(U)$ space.

## Alternatives and edge cases
- **Enumerate index pairs:** directly evaluating every ordered pair is simple
  but takes $O(n^2)$ time.
- **Sort and binary-search quotient boundaries:** this avoids a full value
  prefix array but adds repeated logarithmic searches and is harder to
  aggregate cleanly.
- Equal indices are included; each such pair contributes one.
- Duplicate values contribute through their full multiplicity on both the
  numerator and denominator sides.
- Apply the modulo to the total, not to individual floor divisions.
