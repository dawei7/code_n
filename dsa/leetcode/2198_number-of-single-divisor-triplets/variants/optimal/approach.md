## General

**Compress indices into value frequencies**

Testing every triple of indices would ignore the strongest constraint: although the array can contain $10^5$ entries, it has at most $100$ distinct values. Build a frequency table, then enumerate nondecreasing value triples $a \le b \le c$ from the values that actually occur.

For each value triple, compute $s=a+b+c$ and evaluate the three positional conditions $s\bmod a=0$, $s\bmod b=0$, and $s\bmod c=0$. Keep the triple only when exactly one condition is true. These are positional tests even when values are equal. Thus, if $a=b$ and $a$ divides $s$, two of the three conditions are already true.

**Recover the number of ordered index triplets**

Let $f_x$ be the frequency of value $x$. Once a sorted value triple qualifies, its contribution is:

- $6f_af_bf_c$ when all values differ;
- $3f_a(f_a-1)f_c$ when $a=b<c$;
- $3f_af_b(f_b-1)$ when $a<b=c$; or
- $f_a(f_a-1)(f_a-2)$ when $a=b=c$.

These expressions select distinct occurrences and include every ordering of their indices. For example, when $a=b<c$, there are $\binom{f_a}{2}f_c$ unordered selections, and each has $3!=6$ orders, giving $3f_a(f_a-1)f_c$.

Every ordered triplet of distinct indices has exactly one nondecreasing value triple, so it is counted by exactly one enumeration state. The divisibility filter is identical to the definition, and the multiplicity formula counts precisely all index orders that realize those values. Summing the qualifying contributions therefore gives the required answer.

## Complexity detail

Building the frequency table costs $O(n)$. Enumerating nondecreasing triples of the $U$ present values costs $O(U^3)$, with constant work per triple. The total time is $O(n+U^3)$; here $U\le100$.

The frequency table and list of present values use $O(U)$ auxiliary space.

## Alternatives and edge cases

- **Three index loops:** Directly testing every distinct-index triple is simple and correct, but requires $O(n^3)$ time and is infeasible at the maximum length.
- **Three full-domain loops:** Iterating all ordered triples from `1` through `100` also works, but repeats the six value orders and requires more delicate falling-frequency bookkeeping.
- **Repeated values:** Equal selected values belong to distinct indices, and divisibility by that value succeeds separately at each selected position.
- **Value one:** Every sum is divisible by `1`; a triplet with multiple selected ones therefore has multiple successful divisibility tests and cannot qualify.
- **Ordered result:** A qualifying set of three distinct indices contributes all six permutations, even when two or three selected values are equal.
