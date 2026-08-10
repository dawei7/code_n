## General

Let the three labeled children receive $x$, $y$, and $z$ candies. We count integer triples satisfying

$$
x+y+z=n,\qquad 0\le x,y,z\le\texttt{limit}.
$$

Because the children are distinct, changing which child receives an amount creates a different distribution.

**Reject totals above the combined capacity**

The three children can hold at most `3 * limit` candies. If `n > 3 * limit`, no distribution exists and the source immediately returns zero.

This guard also simplifies the later inclusion–exclusion formula. After it passes, all three children cannot simultaneously exceed the limit, because that would require at least $3(\texttt{limit}+1)>3\texttt{limit}\ge n$ candies.

**Count all unrestricted nonnegative triples**

Ignore the upper bounds temporarily. The stars-and-bars formula counts solutions to $x+y+z=n$ as

$$
\binom{n+2}{2}.
$$

One interpretation places two separators among $n$ candies plus separator positions. The source initializes

`ans = comb(n + 2, 2)`.

This includes valid distributions and distributions where one or more children exceed `limit`.

**Subtract distributions where one child is too large**

Fix a child and require that child to receive at least `limit + 1` candies. Give those candies first. The remaining

$$
n-(\texttt{limit}+1)
$$

candies may be distributed without upper bounds, giving

$$
\binom{n-\texttt{limit}+1}{2}
$$

solutions for that chosen child. There are three choices of child, so the source subtracts

`3 * comb(n - limit + 1, 2)`.

This term exists only when `n > limit`. The guard prevents calling `comb` with an invalid small first argument and reflects that no child can exceed the limit when the total itself is at most the limit.

**Add back distributions where two children are too large**

Subtracting the three bad sets removes a distribution twice if two children each receive at least `limit + 1`: it belongs to both single-child bad sets. Inclusion–exclusion adds it back once.

Choose the two excessive children in $\binom{3}{2}=3$ ways. Giving both `limit + 1` candies leaves

$$
n-2(\texttt{limit}+1)
$$

to distribute, yielding

$$
\binom{n-2\texttt{limit}}{2}
$$

solutions per pair. The source adds `3 * comb(n - 2 * limit, 2)` when

`n - 2 >= 2 * limit`,

which is exactly $n\ge2(\texttt{limit}+1)$.

**Why there is no subtract-three term**

The full inclusion–exclusion formula normally subtracts cases where all three children exceed the limit. But such a case needs at least $3(\texttt{limit}+1)$ candies. The initial guard has already returned zero whenever $n>3\texttt{limit}$. For every execution reaching the formula, $n\le3\texttt{limit}<3(\texttt{limit}+1)$, so the triple intersection is empty.

The computed result therefore contains every bounded distribution exactly once: unrestricted count, minus each one-child violation, plus each double-subtracted two-child violation.

## Complexity detail

The method evaluates a fixed number of comparisons, multiplications, additions, subtractions, and binomial coefficients with second argument two. Under the usual arithmetic-operation model, time complexity is $O(1)$ and auxiliary space is $O(1)$.

Python's `math.comb` handles the large exact integers required by the version-III bounds. If bit complexity is counted, arithmetic cost grows with the number of bits in $n$, but there is still no loop dependent on $n$ or `limit`.

## Alternatives and edge cases

- **Enumerate the first child's amount:** For every $x$, count the legal range for $y$. This takes $O(\min(n,\texttt{limit}))$ time and is unnecessary for values up to $10^8$.
- **Three nested loops:** It directly checks all triples but is far too slow and repeats the sum constraint.
- **Dynamic programming:** Counting bounded compositions with a table is general but excessive for exactly three children and large $n$.
- **Total equals capacity:** When `n == 3 * limit`, exactly `(limit, limit, limit)` is valid; the formula returns one.
- **Limit at least total:** No child can violate the bound, so the unrestricted $\binom{n+2}{2}$ count remains.
- **Children may receive zero:** Stars and bars counts nonnegative solutions, correctly including empty shares.
- **Labeled children:** `(1,2,2)`, `(2,1,2)`, and `(2,2,1)` are distinct.
- **Boundary of one violation:** At `n == limit + 1`, the single-excess term begins with exactly one allocation for a fixed excessive child.
- **Boundary of two violations:** The pair term begins only at `n == 2(limit + 1)`, matching the source condition.
- **No modulo:** The contract asks for the exact count, and Python returns the full integer.
- **Why `comb(q, 2)` appears:** Three nonnegative shares require two separators, so every residual stars-and-bars term always chooses two positions. With fixed second argument, it equals `q * (q - 1) // 2`.
- **One excessive child versus a named set:** Multiplication by three chooses which child owns the violation. It does not assume the three bad sets are disjoint; their overlaps are exactly why the pair term is added.
- **Large equal parameters:** Even when $n$ and `limit` approach $10^8$, the formula evaluates the same fixed number of terms and never iterates over candy units.
- **Guard order matters:** Returning for `n > 3 * limit` before the shortened formula is what makes the omitted triple-intersection term provably zero.
