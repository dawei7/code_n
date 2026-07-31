## General

**An increment belongs on a smallest factor**

Suppose two current factors satisfy $a\le b$. Assigning the next unit to $a$ changes their contribution to $(a+1)b$, while assigning it to $b$ produces $a(b+1)$. Their difference is $b-a\ge0$, so incrementing the smaller factor is never worse.

This exchange remains valid with every other non-negative factor held fixed. Therefore an optimal allocation can always choose a currently minimum value for its next operation.

**Maintain the changing minimum**

Build a min-heap from all values. Repeat `k` times: replace the heap minimum $x$ with $x+1$. Ties need no special handling because equal minima are interchangeable.

After all increments, multiply every heap value while reducing intermediate products modulo $1{,}000{,}000{,}007$. The modulo is applied only during this final multiplication; all greedy comparisons used the true factor values. Repeatedly applying the exchange result proves that the heap allocation attains a maximum product.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Heap construction takes $O(n)$ time, each of `k` replacements takes $O(\log n)$, and final multiplication takes $O(n)$. This is $O((n+k)\log n)$ time under the manifest's compact bound.

The heap contains $n$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Scan for the minimum each time:** This preserves the greedy choice but can take $O(nk)$ time.
- **Sort once:** A static ordering becomes stale as incremented values catch up with later values.
- **Batch level sorted groups:** Raising prefixes in batches can reduce dependence on `k`, but requires more intricate quotient and remainder handling.
- **Zero factors:** Increments naturally fill zeros first because any remaining zero keeps the product at zero.
- **Several equal minima:** Incrementing any one of them is equally good; the heap may choose arbitrarily.
- **One element:** Every useful operation goes to that only factor.
- **Modulo:** Maximizing residues instead of the true product is invalid.
- **At most `k`:** Using another increment never decreases a product of non-negative factors, so using all `k` is safe.
