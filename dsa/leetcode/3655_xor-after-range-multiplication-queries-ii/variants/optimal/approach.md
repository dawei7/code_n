## General

Let $M=10^9+7$ and choose $B=\lfloor\sqrt n\rfloor$. Multiplication modulo $M$ is associative and commutative, so the final multiplier at an index does not depend on the order in which its applicable query factors are combined. This permits grouping queries by step.

**Apply large steps directly.** When `k > B`, one query visits at most $\lceil n/k\rceil=O(n/B)$ indices. Iterating its progression is already efficient, so update those entries immediately.

**Batch each small step.** Fix a step `k <= B`. Indices with the same remainder modulo `k` form an independent sequence. A query begins multiplying that sequence at `l` and stops just before the first progression position beyond `r`. Record factor `v` at `l` and factor $v^{-1}\bmod M$ at that first position after the query. Because every allowed multiplier is nonzero modulo the prime $M$, Fermat's theorem provides the inverse.

Sweep each residue sequence from left to right, maintaining the product of its multiplicative difference factors. Multiplying every encountered `nums[index]` by the running product applies all grouped queries of that step simultaneously. Process only step sizes that actually have queries, reuse one length-$n$ factor array per group, and cache inverses for repeated multipliers.

## Complexity detail

There are at most $B$ processed small step sizes, each requiring an $O(n)$ residue sweep. Their query events take $O(q\log M)$ worst-case time for modular inverses. Every large-step query performs $O(n/B)$ updates. With $B=\lfloor\sqrt n\rfloor$, total time is

$$
O\bigl((n+q)\sqrt n+q\log M\bigr).
$$

Grouped queries, the reusable factor array, inverse cache, and input storage require $O(n+q)$ auxiliary space.

The benchmark sets size $N=n=q$, consists entirely of full-range step-one queries, and uses tiers 32, 128, and 512 for a 16x span. The accepted small-step batch is $O(N\log M)$. Literal progression simulation performs $N$ updates for each of $N$ queries and is $O(N^2)$, so it must finish all tiers but fail scaling.

## Alternatives and edge cases

- **Direct simulation:** It is appropriate for the smaller companion problem but can require $10^{10}$ updates here.
- **One structure per step:** Permanently allocating an $n$-entry array for every small step consumes $O(n\sqrt n)$ memory; process groups sequentially instead.
- **First position after `r`:** Compute it along the same residue class as `l`; using `r + 1` directly is incorrect when the step is greater than one.
- **Repeated multipliers:** Cached modular inverses avoid recomputing the same exponentiation.
- **Large step with short range:** Direct traversal naturally performs only the update at `l` when no second progression index fits.
- **Multiplier one:** Its inverse is also one, so the difference sweep remains valid without special handling.
