## General

**Each pile offers prefix choices**

Taking $x$ coins from one pile necessarily takes its first $x$ entries. The pile therefore offers one option for every legal prefix length, with a value obtained by accumulating a running prefix sum. Choosing coins from different piles becomes a grouped exact-count knapsack problem.

**Record the best value for each exact count**

Maintain `best[t]` as the maximum value obtainable by taking exactly $t$ coins from the piles already processed. Initially only `best[0] = 0` is reachable. For the next pile, copy the zero-from-this-pile choices, then enumerate its prefixes. Combining a prefix of length $x$ and value $v$ with every reachable old count $t$ proposes `best[t] + v` for the new count $t+x$.

Transitions must read from the previous pile's array, not partially updated states, because a pile prefix may be selected only once. After all piles, `best[k]` is the answer.

Every legal selection chooses exactly one prefix length from each pile. The transition enumerates that prefix when its pile is processed and combines it with the optimal representation of all earlier choices. Conversely, every transition represents legal top removals. Induction over piles therefore makes each state optimal for its exact count.

## Complexity detail

Let $C$ be the total number of coins. At most $\min(k,\lvert p\rvert)$ prefixes of pile $p$ are combined with at most $k$ counts, so time is $O(kC)$.

The rolling dynamic-programming arrays use $O(k)$ space.

## Alternatives and edge cases

- **Recursive allocation search:** Trying every distribution of `k` coins among piles repeats overlapping subproblems and can be exponential.
- **Two-dimensional dynamic programming:** Storing a row per pile is correct but uses $O(nk)$ space when only the preceding row is needed.
- **Take the currently largest top coin:** A small top coin may unlock a much larger buried coin, so local greedy choice can be suboptimal.
- **Take zero from a pile:** Copying the old state preserves this necessary option.
- **Pile longer than `k`:** Prefixes beyond `k` can never participate in an exactly-`k` answer.
- **Take every coin:** When $k=C$, the only legal value is the sum of all piles.
- **Buried value:** A deep high-value coin contributes only together with every coin above it.
