## General

**Only currently exposed workers are eligible**

In each session, candidates come from the first `candidates` remaining workers and the last `candidates` remaining workers. Hiring from one side exposes one new worker from that same side of the still-hidden middle.

A min-heap stores each exposed worker as `(cost,index)`. Python compares tuples lexicographically, so it chooses smaller cost first and smaller original index on a tie, exactly matching the rule.

**Handle overlapping candidate sides**

If `2*candidates >= n`, the first and last candidate regions cover every remaining worker from the beginning. After any hire, fewer workers remain, so all of them continue to be eligible. Each session simply chooses the globally cheapest remaining worker, breaking ties by index.

The exact shortcut sorts all costs and sums the first `k`. It does not include indices in the sort, but for total cost the tie-breaking choice among equal costs does not change the sum. Thus the shortcut returns the correct total.

**Initialize disjoint exposed regions**

When `2*candidates < n`, the left and right initial regions do not overlap. The source pushes indices 0 through `candidates-1` and `n-candidates` through `n-1` into one heap.

Pointers `l=candidates` and `r=n-candidates-1` delimit the hidden middle. `l` is the next unseen worker from the left, and `r` is the next unseen worker from the right.

Calling `heapify` after already using `heappush` is redundant but harmless: the list is already a heap, and heapifying preserves it.

**Hire and replenish the selected side**

Each of the `k` sessions pops the minimum tuple, adds its cost, and identifies which candidate side supplied it.

If `l>r`, no hidden worker remains. The heap already contains every remaining worker, so no replenishment occurs.

Otherwise, `i < l` means the popped original index came from the exposed left side. The next hidden left worker at `l` is pushed and `l` advances.

If `i >= l`, the popped worker belongs to the exposed right side. The worker at `r` is pushed and `r` decreases.

Why is this test reliable? While a hidden middle remains, all active left indices are smaller than `l`. Active right indices originated beyond `r` and are not smaller than `l`. The regions never overlap in this branch.

**Maintain the candidate-set invariant**

Before every pop, the heap contains exactly the first up to `candidates` remaining workers from the left and the last up to `candidates` remaining workers from the right, with no duplicate indices.

Initialization establishes this. Hiring removes one eligible worker. If hidden workers remain, adding the next worker from the same side restores that side's candidate count while leaving the other side unchanged. When the middle is exhausted, all remaining workers are already exposed and no addition is necessary.

The heap minimum therefore represents exactly the worker the rules demand in every session. Summing the popped costs gives the correct total.

**Trace the moving boundaries**

With `costs=[17,12,10,2,7,2,11,20,8]` and four candidates, the heap initially contains indices 0–3 and 5–8, while index 4 is hidden. The first minimum cost is 2 at index 3, chosen over index 5 because its index is smaller. Since it came from the left, index 4 becomes exposed. The next minimum is index 5 with cost 2; it came from the right, but no hidden worker remains. The third minimum is the exposed cost 7. Their total is 11.

Original indices are retained even though the statement discusses changing positions among remaining workers. Removing elements compresses conceptual positions, but taking boundary candidates corresponds exactly to advancing the original left and right pointers over unchosen workers.

## Complexity detail

Let $c=\texttt{candidates}$. In the disjoint branch, initialization handles $2c$ workers. The heap size stays $O(c)$. Each of $k$ sessions performs one pop and at most one push, each $O(\log c)$, for $O((c+k)\log c)$ time and $O(c)$ heap space.

In the overlap shortcut, sorting all $n$ costs takes $O(n\log n)$ time and $O(n)$ space in Python. Since $c\ge n/2$, this is compatible with the broad scale of $O((c+k)\log c)$, but the exact branch-specific cost is clearer.

The answer may sum $10^5$ hires at cost $10^5$, reaching $10^{10}$. Python integers are safe; other languages need 64-bit accumulation.

## Alternatives and edge cases

- **Two heaps:** Maintain separate left and right min-heaps, compare their tops, and replenish the chosen side. This is equivalent but requires explicit cross-heap tie handling by index.
- **Sort all workers unconditionally:** It ignores exposure rules when candidate regions do not cover the middle, so it is valid only in the overlap shortcut.
- **Repeated linear scans:** Searching exposed workers in every session costs $O(kc)$, which can be quadratic.
- **Candidate regions overlap:** The shortcut prevents inserting the same worker twice.
- **Equal costs:** Tuple ordering selects the smaller original index in the heap branch.
- **No hidden middle:** After `l>r`, popping continues without replenishment.
- **Hire every worker:** The heap eventually exposes and pops all indices, and the total becomes `sum(costs)`.
- **One candidate per side:** The heap compares only the current leftmost and rightmost remaining workers.
- **Tie behavior in shortcut:** Equal-cost worker order does not affect the requested total, even though the exact hired identities would follow indices.
- **Input preservation:** The heap branch does not mutate `costs`; the shortcut uses `sorted` rather than in-place sorting.
