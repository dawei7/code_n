## General

**View each element as an interval of reachable target values.** One operation can change value $v$ by any integer from $-k$ through $k$. Therefore that index can become any integer target in closed interval $[v-k,v+k]$. The problem asks for a target coordinate covered by as many element intervals as possible, subject to the number of elements that actually need changes.

`cnt[x]` records how many elements already equal target $x$. Those copies need no effective modification to contribute to its frequency.

**Build a sparse difference map for interval overlap.** For each interval, `d[v-k] += 1` starts one unit of coverage, and `d[v+k+1] -= 1` ends it immediately after the inclusive integer right endpoint. Sorting event coordinates and accumulating `s += t` makes `s` equal the number of original elements that can be transformed into the current coordinate.

The `+1` at the right boundary is essential for integer coordinates: target $v+k$ is reachable and remains covered.

**Force original values to become sweep candidates.** `d[v] += 0` does not change coverage, but it inserts coordinate $v$ into the event map. This matters because the attainable answer at a target that already exists can exceed a neighboring nonexisting target: its unchanged copies do not consume the operation budget.

Between consecutive event coordinates, overlap `s` is constant and `cnt[x]` is zero unless an original value was explicitly inserted. Checking the event boundaries plus all original coordinates therefore covers every distinct value of the objective.

**Combine reachability with the operation budget.** At target $x$, at most `s` total elements are reachable. Of these, `cnt[x]` already equal $x$ and can remain unchanged. At most `numOperations` additional indices can be changed into $x$. Thus maximum achievable frequency is

$$
\min\bigl(s,\ \texttt{cnt}[x]+\texttt{numOperations}\bigr).
$$

The source evaluates this formula at every sparse candidate and retains the maximum.

**Why “exactly” the given number of operations behaves like “at most.”** Any unused required operation can select a previously unselected index and add zero, which lies in $[-k,k]$. Such a no-op does not alter the achieved frequency. Therefore only the number of useful nonzero changes is bounded above by `numOperations`.

**Trace how a plateau is represented.** Suppose one element has value five and $k=2$. Its interval contributes a start event at three and an end event at eight, so the running coverage includes integer targets three through seven. The map stores no entries at four or six unless another interval boundary or original value creates them. That omission is safe: the coverage cannot change inside this gap. The forced event at five is nevertheless essential because `cnt[5]` may raise the operation-budget cap there.

There are two different limitations in the formula, and neither subsumes the other. When many intervals cover $x$ but few operations are available, `cnt[x] + numOperations` is the bottleneck. When the operation budget is large but only a few intervals cover $x$, `s` is the bottleneck. Taking the minimum expresses both restrictions exactly rather than estimating either one.
Interval overlap counts precisely which elements can reach a chosen target in one permitted operation. Existing target copies are free, and every other included copy consumes one distinct-index operation, yielding the cap formula. Conversely, choose up to the cap's number of reachable nonexisting copies and apply their exact differences; all lie within range. Remaining mandatory operations can add zero. Sparse sweep candidates include an optimum because coverage changes only at events and existing-value bonuses only at forced coordinates.

For `k=0`, every interval is a single point. Overlap at $x$ equals `cnt[x]`, so the formula returns the original maximum frequency regardless of operation budget.

The exact source already uses the sparse event method associated with the larger version II, rather than enumerating the bounded coordinate range described in the version-I editorial.

## Complexity detail

Each of $n$ values creates at most three dictionary coordinates, so there are $O(n)$ events. Building maps costs expected $O(n)$ time. Sorting event items costs $O(n\log n)$, and the sweep is linear. Total time is $O(n\log n)$.

`cnt` and `d` hold $O(n)$ keys, giving $O(n)$ auxiliary space. The input is not sorted or modified.

## Alternatives and edge cases

- **Sort and binary-search each target:** Count values in $[x-k,x+k]$ for candidate targets. It can also achieve $O(n\log n)$ but requires careful candidate enumeration.
- **Dense coordinate difference array:** Version I's $10^5$ bounds permit it, but sparse events avoid coordinate-sized allocation and also work for version II.
- **Target absent from input:** `cnt[x]=0`, so frequency is capped by the operation count.
- **Target already frequent:** Existing copies do not consume operations and add to the cap.
- **`numOperations = 0`:** The formula reduces to original frequencies at forced coordinates.
- **`k = 0`:** No value can change, though required operations can add zero.
- **Inclusive right endpoint:** Event removal occurs at `v+k+1`, not `v+k`.
- **Duplicate input values:** Their intervals and counts accumulate independently.
- **Exactly versus at most:** Zero additions absorb unused operations.
- **Negative event coordinates:** Values are positive, but `v-k` may be negative; dictionary sorting handles it normally.
- **No coordinate enumeration:** Runtime depends on $n$, not the numeric span.
- **Forced zero event:** `d[v] += 0` is a deliberate candidate insertion, not dead code.
- **Input preservation:** Only dictionaries are built; `nums` remains unchanged.
