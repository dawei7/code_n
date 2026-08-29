## General

**A valid group uses one common pay-per-quality rate**

Payment must be proportional to quality. Therefore, for a chosen group there is one rate `R` such that worker `i` is paid:

$$
R\cdot quality[i].
$$

To meet that worker's minimum wage:

$$
R\cdot quality[i]\ge wage[i],
$$

so:

$$
R\ge\frac{wage[i]}{quality[i]}.
$$

For a fixed group, the smallest legal common rate is the maximum wage-to-quality ratio among its members.

The group's minimum total cost is consequently:

$$
\left(\max_{i\text{ in group}}\frac{wage[i]}{quality[i]}\right)
\cdot\left(\sum_{i\text{ in group}}quality[i]\right).
$$

This formula separates the problem into choosing a maximum rate and minimizing total quality under that rate.

**Sort workers by required rate**

The list `t` contains `(quality,wage)` pairs sorted by `w/q` increasingly.

When processing current worker `(q,w)`, all workers seen so far have required ratio no greater than current:

$$
R=\frac{w}{q}.
$$

Any `k`-worker group drawn from this prefix and including a worker with this maximum ratio can legally be paid at rate `R`.

For this fixed rate, minimizing total cost means choosing the `k` smallest qualities available, because `R` is positive and cost is `R\cdot\sum quality`.

**Maintain the smallest qualities with a max-heap**

Python's heap is a min-heap, so the source pushes `-q`. The smallest negative value represents the largest positive quality.

`tot` stores the sum of qualities currently in the heap.

For each sorted worker:

1. add their quality to `tot`;
2. push `-q`;
3. when heap size reaches `k`, evaluate this group;
4. remove the largest quality to leave the best `k-1` qualities for future rates.

**Why evaluate before removing**

At the moment `len(h) == k`, the heap contains the `k` smallest relevant qualities among workers available for the current threshold, subject to the incremental invariant.

The current candidate cost is:

`(w / q) * tot`.

The source takes the minimum over all such candidates.

After evaluation:

`tot += heappop(h)`.

`heappop` returns a negative quality. Adding it subtracts the corresponding positive largest quality from `tot`. The heap returns to size `k-1`.

This prepares for the next worker: adding one new quality creates a size-`k` candidate containing the best possible qualities among the expanded prefix.

**Why the heap contains the right qualities**

Inductively, before a new worker is inserted, the heap contains the smallest `k-1` qualities from the previously processed prefix.

After adding the current quality, it contains `k` candidates. Evaluating their sum gives the minimum possible quality sum for a size-`k` selection that is available at this threshold. Removing the largest restores the smallest `k-1` qualities among the new prefix.

Thus, the invariant continues.

**Why every optimal group is considered**

Take an optimal group and let worker `r` have its largest required ratio. When the sorted scan reaches `r`, every member of that group is in the processed prefix, and current rate equals the group's minimum legal rate.

The heap's `k` qualities have sum no larger than that optimal group's quality sum. Therefore, the candidate evaluated at this threshold is no more expensive. Since every evaluated candidate is itself a legal group, taking the global minimum yields exactly the optimum.

**Trace the first example**

Workers have:

- quality 20, wage 50, ratio 2.5;
- quality 5, wage 30, ratio 6;
- quality 10, wage 70, ratio 7.

For `k=2`:

- At ratio 6, qualities 20 and 5 sum to 25, candidate cost 150. The heap then removes quality 20, retaining 5.
- At ratio 7, add quality 10, giving sum 15 and cost 105.

Paying at rate 7 gives worker quality 10 a wage 70 and worker quality 5 a wage 35, satisfying both minimums with total 105.

## Complexity detail

Let `n` be the number of workers. Sorting by ratio takes `O(n\log n)` time.

Each worker is pushed once. From the point the heap reaches size `k`, one item is popped per iteration. Heap operations cost `O(\log k)`, giving `O(n\log k)` additional time. Sorting dominates, so total time is `O(n\log n)`.

The sorted pair list uses `O(n)` space. The heap holds at most `k` qualities, and all scalar state is constant. Total auxiliary space is `O(n)`.

Ratio calculations use floating-point division, consistent with the accepted numerical tolerance.

## Alternatives and edge cases

- **Enumerate every group:** There are $\binom{n}{k}$ possibilities, which is infeasible.

- **Choose workers with smallest wages:** Minimum wage alone ignores proportionality; required ratios and qualities jointly determine cost.

- **Choose smallest qualities globally:** A low-quality worker may require a very high pay rate that makes the group expensive.

- **`k=1`:** Each worker is evaluated at their own ratio with their own quality, giving exactly their minimum wage; the smallest is returned.

- **`k=n`:** The only group contains everyone, paid at the maximum ratio.

- **Equal ratios:** Their relative sort order does not matter; the heap considers quality combinations at the same rate.

- **Large quality removed:** The max-heap discards it because it contributes most to cost at all later nondecreasing rates.

- **Current worker may be popped after evaluation:** That is fine; its ratio threshold was already considered, and future groups need not include it.

- **Exactly `k` heap size:** The source evaluates then immediately restores size `k-1`, so it never grows beyond `k`.

- **Minimum wage guarantee:** Paying at the current maximum ratio satisfies every selected prefix worker.

- **Input immutability:** Sorted zipped pairs are new; quality and wage arrays remain unchanged.
