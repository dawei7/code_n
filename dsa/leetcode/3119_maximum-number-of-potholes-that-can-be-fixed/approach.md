## General

**Each repair belongs inside one pothole run.** Smooth-road characters split `road` into maximal consecutive runs of `x`. One operation repairing $q$ consecutive potholes costs $q+1$: $q$ units for repaired holes plus a fixed overhead of one.

There is no benefit to combine across a smooth position because the repaired potholes would no longer be consecutive. Within one run of length $L$, repairing $q\le L$ potholes can be done as one operation costing $q+1$.

The optimization is therefore to choose repair lengths from available runs. Longer one-operation repairs are more efficient because the one-unit overhead is shared by more fixed potholes.

**Count run lengths without storing their positions.** The source appends a final smooth marker with `road += "."`. This sentinel forces a run reaching the original string's end to be recorded by the same logic as every other run.

`cnt[L]` stores how many maximal runs currently offer repair capacity of length $L$. Variable `k` counts the current run while scanning. On `x` it increases; on a smooth character, a positive `k` increments `cnt[k]` and resets.

The array has size equal to the sentinel-extended road length, so every possible run length has an index.

**Consider longest repair opportunities first.** The second loop descends from the largest possible `k` to one. For run length `k`, one complete repair costs `k + 1`. The number affordable is `budget // (k + 1)`, but no more than `cnt[k]` runs exist. Thus:

`t = min(budget // (k + 1), cnt[k])`.

The source adds `t * k` repaired potholes and subtracts `t * (k + 1)` budget.

**Why longest first is optimal.** Every chosen operation pays the same one-unit overhead in addition to one unit per repaired pothole. For equal total repaired holes, using fewer operations is never more expensive. Taking repair capacity from a longer run allows more holes to share one overhead.

If a plan repairs $a$ holes from a shorter run while leaving at least $a$ or more useful capacity in a longer run, moving that repair to the longer run preserves cost and feasibility. More generally, descending length maximizes repaired holes for each overhead the budget is forced to pay.

**Downgrade unused runs instead of discarding them.** The most subtle line is:

`cnt[k - 1] += cnt[k] - t`.

An unselected run of length `k` is not useless. With less budget, the algorithm might repair only `k-1` consecutive holes from it for cost `k`. Therefore, every unused length-$k$ run becomes one length-$(k-1)$ opportunity for the next iteration.

If still unaffordable, it cascades to smaller lengths again. This compactly represents every possible partial repair without expanding one candidate per run and per length.

For example, a run of five can contribute opportunities of length five, then four, then three as the descending loop proceeds, but only until one option is selected. Once selected among `t`, that run is removed from the remainder count and never reused.

**Trace `"..xxxxx"` with budget four.** One run of length five is counted. Repairing all five costs six, so `t=0` and the run downgrades to length four. Four costs five, still too much, so it downgrades to three. Three costs four, so it is selected, adds three to `ans`, and exhausts the budget.

**Stopping at zero budget.** If `budget == 0` after a purchase, no repair is possible because even one pothole costs two. The source breaks. If budget remains one, it continues through the loop but cannot select any positive length, correctly leaving the answer unchanged.
At the start of length `k`, `cnt[k]` represents original runs not yet selected that can support at least `k` consecutive repaired potholes. Selecting as many length-$k$ operations as affordable is optimal by the shared-overhead exchange. Every unselected run remains exactly one feasible capacity at length `k-1`. Induction down to one covers every legal partial-repair choice, and `ans` is maximal.

## Complexity detail

Scanning the sentinel-extended road costs $O(n)$. The count array has length $n+1$, and the descending loop visits every possible length once. All work per length is constant, so the exact source takes $O(n)$ time.

The `cnt` array uses $O(n)$ space, and appending the sentinel creates a new Python string of length $n+1$. Auxiliary space is therefore $O(n)$.

This differs from the local manifest, which describes extracting and sorting $r$ run lengths for $O(n+r\log r)$ time and $O(r)$ space. `solution.py` uses counting by every possible length and no sort.

## Alternatives and edge cases

- **Sort run lengths descending:** Greedily consider full or partial repairs from longest runs. It matches the manifest but needs careful handling of a final partial run.
- **Priority queue:** Repeatedly choose the largest remaining repair capacity and reduce it, but the counting cascade is simpler and linear.
- **No potholes:** Every count is zero and the answer remains zero.
- **One long run:** It may be repaired fully or partially according to budget.
- **Many single potholes:** Each costs two because no operation can cross smooth road.
- **Budget one:** No pothole can be fixed.
- **Budget exactly `k+1`:** One length-$k$ opportunity is affordable.
- **Run at string end:** The appended dot records it.
- **Partial repair location:** Any consecutive subsection of the run with the chosen length is feasible; positions do not affect the count.
- **Unused long run:** Downgrading preserves its smaller repair possibilities.
- **Selected run:** It is excluded from `cnt[k]-t` and cannot be selected again.
- **Smooth separators:** Prevent one operation from combining adjacent runs.
- **Fixed overhead:** It is the reason long operations dominate short ones.
- **Input binding:** `road += "."` creates a new local string; the caller's immutable string is unchanged.
- **Source/manifest mismatch:** Exact time and space are both linear in road length, not run-sort bounds.
