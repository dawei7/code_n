## General
**Count values before choosing value triples**

Because every array value is in the fixed range from $0$ through $100$, first build a frequency array. Then enumerate value triples $x\le y\le z$ rather than index triples. Once $x$ and $y$ are chosen, `z = target - x - y` is forced; ignore it unless $y\le z\le100$.

**Convert each value pattern into index choices**

The number of index triples depends on which values are equal:

- If $x=y=z$, choose three indices from the same frequency: $\binom{c_x}{3}$.
- If $x=y<z$, choose two occurrences of $x$ and one of $z$: $\binom{c_x}{2}c_z$.
- If $x<y=z$, use $c_x\binom{c_y}{2}$.
- If all three values differ, use $c_xc_yc_z$.

Add these contributions modulo $10^9+7$. Every valid index triple has exactly one nondecreasing value triple, and each combination formula counts precisely the ways to select its distinct indices. Conversely, each selected combination supplies three array positions with the requested sum; sorting their indices gives exactly one order $i<j<k$. Therefore the cases partition the answer without overlap.

## Complexity detail
Building frequencies takes $O(n)$ time. Enumerating $x$ and $y$ uses $O(V^2)$ pairs, while $z$ is computed directly, giving $O(n+V^2)$ total time. The frequency array uses $O(V)$ space. Here $V=101$ is fixed by the input domain, so both value-range terms are bounded constants.

## Alternatives and edge cases
- **Index-pair counting:** Maintaining earlier frequencies while enumerating every later pair counts triples in $O(n^2)$ time and $O(V)$ space.
- **Sort plus two pointers:** Fixing one index and scanning the remaining suffix can also handle duplicate runs correctly in $O(n^2)$ time.
- **Naive three loops:** Enumerating every index triple costs $O(n^3)$.
- **Three equal values:** Use a combination, not $c_x^3$, because one array index cannot be selected more than once.
- **Two equal values:** The repeated value may be either the smaller pair or the larger pair; these require different formulas.
- **Missing forced value:** A zero frequency naturally contributes nothing.
- **Modulo arithmetic:** Apply the modulus during accumulation because multiplicities can make the exact count large.
