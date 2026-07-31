## General

Let

$$
U=\sum_{[l,r,k,v]\in\texttt{queries}}
\left(\left\lfloor\frac{r-l}{k}\right\rfloor+1\right)
$$

be the total number of required element updates.

**Follow each arithmetic progression exactly.** For query `[l, r, k, v]`, iterate with the language equivalent of `range(l, r + 1, k)`. Multiply only those visited entries by `v` and immediately reduce modulo $10^9+7$. Mutating `nums` in query order directly preserves every dependency between overlapping queries.

No range data structure is needed for this version's bounds: $n$ and the query count are each at most 1000, and direct progression traversal does exactly one constant-time operation for every mandated update. Once all queries finish, scan the final array once and accumulate its XOR.

## Complexity detail

The query phase takes $O(U)$ time, and the final XOR takes $O(n)$, for total time $O(n+U)$. Updates are performed in place and the XOR uses one accumulator, so auxiliary space is $O(1)$.

The benchmark sets size $N=n=q$, uses step `k = N` so every query performs one update, and provides tiers 32, 128, and 512 for a 16x span. The accepted progression iteration is $O(N)$. A correct dense method that scans every index from `l` through `r` and tests its congruence for each query takes $O(N^2)$ and must finish all tiers but fail scaling.

## Alternatives and edge cases

- **Dense range scan:** Testing `(index - l) % k == 0` is correct, but wastes work on indices the query never visits.
- **Residue-class range structures:** More advanced batching is useful for larger variants, but adds complexity without improving this version's legal worst-case bound enough to justify it.
- **Step larger than range width:** Only index `l` is updated.
- **Overlapping queries:** Apply each multiplication to the current value, not the original value.
- **Multiplier one:** The visited elements stay unchanged, but the query remains semantically valid.
- **Modulo timing:** Reduce after every multiplication as specified; do not postpone it until the end.
