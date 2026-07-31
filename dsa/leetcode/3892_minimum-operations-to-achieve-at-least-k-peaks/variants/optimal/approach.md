## General

**Turn each potential peak into a selection cost**

For every circular index $i$, let

$$
c_i=\max\left(0,\max(\texttt{nums[(i-1) mod n]},\texttt{nums[(i+1) mod n]})+1-\texttt{nums[i]}\right).
$$

This is the least number of increments needed to make $i$ a peak when its neighbors retain their original values. Increasing an unselected neighbor cannot help a chosen peak; it only preserves or raises the value that the peak must exceed. Thus, for any nonadjacent set of chosen peak indices, incrementing only those indices realizes the set with total cost equal to the sum of its $c_i$ values.

Two circularly adjacent indices cannot both be peaks, because each would have to be strictly greater than the other. A cycle with $n$ vertices therefore has at most $\lfloor n/2\rfloor$ peaks. Return $-1$ immediately when `k` exceeds that limit, and return $0$ when `k` is zero.

It is sufficient to minimize over sets of exactly `k` indices. Any outcome containing more than `k` peaks contains a nonadjacent subset of exactly `k` of them. Conversely, making any selected set of `k` nonadjacent indices into peaks already satisfies the requirement.

**Break the circular dependency at index zero**

Every legal selection belongs to exactly one of two boundary cases:

- Index $0$ is not selected. Choose `k` nonadjacent indices from the ordinary path $1$ through $n-1$.
- Index $0$ is selected. Pay $c_0$, exclude its two neighbors $1$ and $n-1$, and choose `k - 1` indices from the path $2$ through $n-2$.

Taking the cheaper feasible result covers every circular selection without allowing the first and last indices to be selected together.

**Solve each path with compressed dynamic programming**

For a path prefix and each count $j$, maintain two values:

- `skip[j]`: the minimum cost after selecting $j$ positions when the most recently processed position is not selected;
- `take[j]`: the minimum cost after selecting $j$ positions when the most recently processed position is selected.

At a new index $i$, selecting it is permitted only after a skipped predecessor, giving `new_take[j] = old_skip[j - 1] + c_i`. Skipping it accepts either previous state, giving `new_skip[j] = min(old_skip[j], old_take[j])`. Update counts in descending order so `old_skip[j - 1]` has not yet been overwritten; save the old `take[j]` before replacing it. Unreachable states retain an infinite sentinel.

These transitions consider both choices at every path position and forbid precisely the adjacent selections. Induction on the processed prefix therefore makes each state its stated minimum. The two boundary cases partition all legal cycle selections, and the local-cost argument proves each selected set's value is both attainable and necessary. Their minimum is consequently the least number of operations that can create at least `k` peaks.

## Complexity detail

There are $O(nk)$ reachable count states across the two path runs, and every state takes constant work, so the time complexity is $O(nk)$. The two compressed state arrays contain `k + 1` values each. Peak costs are computed on demand, giving $O(k)$ auxiliary space.

The benchmark defines size as the circular array length $n$ and sets $k=n/4$ on equal-valued arrays. The accepted method therefore performs $\Theta(nk)=\Theta(n^2)$ work along that scaling path. A correct dynamic program that, for every count and ending index, scans all earlier compatible ending indices performs $\Theta(n^2k)=\Theta(n^3)$ work on the same tiers.

## Alternatives and edge cases

- **Full two-dimensional table:** Storing every prefix/count state uses the same $O(nk)$ time but $O(nk)$ space; rolling state arrays preserve only the predecessor information needed by the recurrence.
- **Scan all earlier endpoints:** Defining a state by its last selected position and rechecking every compatible predecessor is correct but costs $O(n^2k)$ time.
- **Greedy by local cost:** The `k` individually cheapest positions may be adjacent, including indices $0$ and $n-1$, so sorting costs does not enforce a feasible peak set.
- **Zero requested peaks:** When `k = 0`, the original array already satisfies the requirement and the answer is zero.
- **Impossible count:** More than $\lfloor n/2\rfloor$ circular peaks cannot coexist, regardless of how many increments are available.
- **Circular boundary:** Indices $0$ and $n-1$ are adjacent. Treating the array as a single path can incorrectly select both.
- **Two-element array:** Both circular neighbor references of an index point to the other element. At most one peak is possible, and the same boundary split remains valid.
- **Negative values:** Signs do not change the method; only the difference from one more than the larger neighbor determines a peak's cost.
- **Strict inequality:** Raising a value merely to equal its larger neighbor is insufficient, so every nonzero local threshold includes `+ 1`.
