## General

**Use the Erdős–Gallai characterization.** Sort the degrees into non-increasing order $d_1\ge d_2\ge\cdots\ge d_n$. A sequence is graphical exactly when its total sum is even and, for every $t$ from 1 through $n$,

$$
\sum_{i=1}^{t}d_i
\le
t(t-1)+\sum_{i=t+1}^{n}\min(d_i,t).
$$

The left side is the number of incident edge ends demanded by the first $t$ vertices. They can supply at most $t(t-1)$ ends among themselves, while each remaining vertex can supply at most the smaller of its degree and $t$ connections into that prefix. The theorem states that these necessary conditions, together with even total degree, are also sufficient.

**Evaluate each suffix efficiently.** Build prefix sums of the sorted degrees. For a fixed $t$, binary-search the first suffix position whose degree is less than $t$. Degrees before that split each contribute `t`; degrees after it contribute their actual sum from the prefix table. This evaluates one inequality in $O(\log n)$ rather than scanning the suffix.

Return false immediately for an odd total or a violated inequality. If every check passes, the sequence is graphical.

## Complexity detail

Sorting takes $O(n\log n)$ time. The $n$ binary searches add another $O(n\log n)$; prefix construction is linear. The sorted list, negated search keys, and prefix sums use $O(n)$ auxiliary space.

The benchmark sets size $N=n$, uses the graphical complete-graph sequence `[N - 1] * N`, and provides tiers 32, 128, and 512 for a 16x span. Erdős–Gallai takes $O(N\log N)$. Repeated-sort Havel–Hakimi performs $N$ reductions and sorts after each one, taking at least quadratic time on this input, so it must finish every tier but fail scaling.

## Alternatives and edge cases

- **Havel–Hakimi:** Repeatedly connect the highest-degree vertex to the next highest degrees. It is constructive and correct, but a straightforward repeated sort is substantially slower.
- **Try graph edge subsets:** Enumerating possible simple graphs is exponential in $n^2$.
- **Odd degree sum:** The handshaking lemma rules the sequence out immediately.
- **All zeros:** The edgeless graph realizes the sequence.
- **Single vertex:** Only degree zero is legal under the supplied bounds and is graphical.
- **Maximum degrees:** A sequence of $n$ copies of `n - 1` is the complete graph and must pass.
