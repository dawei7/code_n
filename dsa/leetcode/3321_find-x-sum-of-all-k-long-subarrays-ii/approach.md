## General

**Maintain one ranked key per distinct window value.** For current frequency $c$ and value $v$, ranking uses pair $(c,v)$: higher frequency wins, and a larger value wins a frequency tie. A selected value contributes $cv$ because every one of its occurrences remains in the x-sum.

The source maintains `cnt` plus two `SortedList` collections. `l` holds the best $x$ positive-frequency pairs when balanced; `r` holds the rest. `s` is the contribution sum over `l`. This is an ordered-set solution, not the “two versioned lazy heaps” claimed by the manifest summary.

**Remove stale keys around every counter update.** Since frequency is part of the key, a counter change cannot update a tuple in place. Helper `remove(v)` constructs the old pair and removes it from `l` or `r`. If selected, its old contribution is subtracted from `s`.

After modifying `cnt[v]`, `add(v)` skips zero counts. A positive pair better than `l[0]` tentatively joins `l` and adds its contribution; otherwise it joins `r`. During initial window construction `l` is empty, so pairs collect in `r` until the first rebalance.

**Restore the top-$x$ boundary at each complete window.** If `l` has fewer than $x$ entries, `r.pop()` moves the strongest remaining pair into it. If `l` has more than $x$, `l.pop(0)` moves the weakest selected pair out. Contributions are added or subtracted at the same time.

Frequency updates can disturb size only around the changed values. A selected value that weakens is removed, after which the best `r` candidate fills its place. An unselected value that strengthens beyond `l[0]` enters `l` and forces the weakest selected key out. After the loops, `l` contains the lexicographically largest $\min(x,D)$ pairs, where $D$ is window distinct count.

**Record and slide.** At right index $i$, start `j=i-k+1` identifies the completed window. Once balanced, `ans[j]=s` is its x-sum. The outgoing value `nums[j]` is then removed under its old frequency, decremented, and reinserted under its new positive frequency. The next iteration similarly updates the incoming value.

Only one tuple exists for each positive-frequency value. Individual copies are represented by the tuple's count, which keeps ordered-set size bounded by window distinct count rather than $k$ occurrences.

**Tie-breaking is automatic.** Sorted tuple order compares count first and value second. Thus pair $(2,9)$ outranks $(2,4)$, while any count-three pair outranks both. The selected contribution still uses count times value, not the tuple interpreted as some other score.

**Why fewer than $x$ distinct values works.** Rebalancing moves every pair from `r` when `l` cannot reach $x$. Then `s` contains the contribution of every distinct value, which equals the ordinary window sum. No separate branch is required.
Before each answer, all current positive-frequency values appear exactly once across `l\cup r`; `l` has the required bounded size; every member of `l` ranks no lower than every member of `r`; and `s` equals the selected weighted sum. Update helpers preserve membership and contribution accuracy, while boundary moves restore size and rank. Induction over windows proves every answer.

The source assumes `SortedList` and `Counter` imports are provided. `SortedList` is not part of Python's standard library.

## Complexity detail

Each input occurrence triggers a constant number of ordered-list operations for entering and leaving the window. Each costs $O(\log D)\subseteq O(\log k)$. Boundary movement is amortized constant per changed key, so total time is $O(n\log k)$.

The ordered lists contain $O(k)$ current distinct keys. However, `cnt` never deletes zero-count entries, so across values up to $10^9$ it may retain every distinct value ever seen, using $O(n)$ space. The output also uses $O(n-k+1)$. The manifest's $O(n)$ space is therefore accurate for the exact source, though its claimed lazy-heap structure is not.

## Alternatives and edge cases

- **Recount and sort every window:** It costs $O((n-k+1)k\log k)$ and is too slow for $n=10^5$.
- **Two lazy heaps:** Versioned heap entries can emulate the partition but require stale-entry cleanup; that is not what this source uses.
- **Balanced search tree with explicit swaps:** The editorial's large/small ordered-set helper expresses the same invariant more explicitly.
- **Fewer than $x$ distinct values:** All pairs are selected and `s` becomes the complete window sum.
- **Equal frequencies:** Larger values have larger tuple keys and are retained first.
- **A value count drops to zero:** Its old tuple is removed and no new tuple is added.
- **`x = 1`:** Only the strongest tuple contributes.
- **`x = k`:** Every distinct value fits in the selected set because a window has at most $k$ distinct values.
- **Very large values:** Python multiplication and sums do not overflow; fixed-width translations need 64-bit results.
- **Zero-count dictionary keys:** They do not enter ordered sets but cause `cnt` to grow to $O(n)$ distinct historical values.
- **Incoming equals outgoing:** Sequential removal and addition preserve the final frequency and the next answer remains correct.
- **External package:** The runtime must provide `sortedcontainers.SortedList` or an equivalent imported class.
- **Manifest discrepancy:** The complexity matches, but the protected implementation uses two sorted lists, not two versioned lazy heaps.
