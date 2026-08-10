## General

Every tap defines a closed interval of the garden that it can water. The goal is the minimum number of intervals whose union covers `[0, n]`.

The exact Optimal solution converts taps into a “farthest reach by left endpoint” array and then performs the same greedy layer expansion used by Jump Game II. At each committed boundary, it chooses the interval available so far that reaches farthest right.

**Compressing intervals by their left endpoints**

Tap `i` with range `x` covers:

$$
[i-x,\;i+x].
$$

Only the garden portion matters, so its left endpoint is clamped with `max(0, i - x)`. The exact code does not clamp the right endpoint to `n`; allowing a value beyond `n` is harmless because reaching beyond the garden end is at least as good as reaching exactly it.

`last[l]` stores the maximum right endpoint among all taps whose clipped left endpoint is `l`.

If two taps begin at the same `l`, the one ending earlier is never preferable. It costs the same one opened tap and covers a subset of the farther interval. Keeping only the maximum endpoint loses no optimal solution.

**Meaning of the three greedy variables**

`pre` is the right boundary guaranteed by the number of taps already counted in `ans`.

`mx` is the farthest boundary reachable by opening one additional tap whose left endpoint has been scanned and is no greater than the current position.

`i` scans possible left endpoints from zero through `n - 1`.

Before deciding at a boundary, the code updates:

`mx = max(mx, last[i])`.

Thus, `mx` considers every interval that starts no later than `i`.

**Detecting a coverage gap**

If `mx <= i`, no available interval extends coverage strictly beyond position `i`. The garden has positive length remaining because the loop stops before `n`. A point immediately to the right of `i` cannot be watered by any already-scanned interval.

Could a later-starting interval repair this gap? No. Such an interval begins after `i` and cannot cover the uncovered region immediately after it. Therefore, returning $-1$ is correct.

The strict extension requirement also ignores zero-length tap intervals, which cannot help cover positive garden length.

**Committing a new tap at the current frontier**

When `pre == i`, the coverage obtained from already counted taps ends at the current scan position. To move farther, another tap must be opened.

Among every tap capable of starting by this frontier, `mx` is the greatest available right endpoint. The method increments `ans` and assigns `pre = mx`.

Choosing the farthest-reaching option is optimal. Every solution that continues beyond the old frontier must choose some interval starting no later than it. Replacing that choice with the interval reaching `mx` uses the same one tap and leaves coverage at least as far right. It cannot increase the number of taps needed later.

**Why the scan can postpone the choice**

Between the old frontier and `pre`, the current set of counted taps already guarantees coverage. The algorithm scans all interval starts in that region and keeps improving `mx`. It does not need to commit immediately when it sees a candidate.

Only upon reaching `pre` does it need the next interval. By then, it has seen every interval that can connect continuously from the existing coverage, so it can safely choose the one extending farthest.

**Example behavior**

For `n = 5` and `ranges = [3,4,1,1,0,0]`, the tap at position one has clipped left endpoint zero and right endpoint five. Preprocessing makes `last[0]` at least five.

At `i = 0`, `mx` becomes five, coverage can advance, and `pre == 0` causes one tap to be counted with new frontier five. All remaining scan positions lie before that frontier, so no additional tap is needed. The answer is one.

With every range zero, `last[0]` is zero. At `i = 0`, `mx <= i`, so the source correctly returns $-1$.

**Why the number of taps is minimum**

Every counted greedy step chooses one interval that overlaps or begins within current continuous coverage and extends the frontier to `mx`, so its constructed coverage has no gaps.

At each boundary, any feasible solution needs at least one additional interval. The greedy interval reaches at least as far as the interval used by any competing solution at that step. Inductively, after the same number of taps, greedy coverage is never shorter. Therefore, no solution can reach `n` with fewer taps than `ans`.

## Complexity detail

There are `n + 1` taps. Preprocessing visits each once and performs constant work, taking $O(n)$ time.

The greedy loop scans `n` positions once, also taking $O(n)$ time. Total time is $O(n)$.

`last` has `n + 1` entries, so auxiliary space is $O(n)$, matching the manifest. All other variables use constant space.

Right endpoints larger than `n` do not enlarge the array because they are stored only as integer values, not used as indices.

## Alternatives and edge cases

- **Sort all intervals then cover greedily:** The classic interval-cover algorithm works in $O(n\log n)$ time. Integer left endpoints let this source avoid sorting.
- **Dynamic programming:** Track the minimum taps needed to reach positions, but straightforward range updates can be slower than the linear greedy method.
- **Two taps with the same left endpoint:** Only the farther right endpoint matters; the shorter interval is dominated.
- **Tap reaches beyond `n`:** This is safe and signals that the garden end is already covered.
- **Zero-range taps:** They cannot extend `mx` and do not help cover positive length.
- **Gap at position `i`:** If `mx <= i`, no later interval can cover immediately after `i`, so failure is final.
- **One tap covers everything:** It is selected at the initial frontier, and `ans` remains one.
- **Intervals touching at endpoints:** Closed intervals can connect at the same point, and the `pre == i` frontier logic permits that continuation.
- **Loop stops at `n - 1`:** Once every point before `n` can extend coverage past it, endpoint `n` is covered; no tap needs to start at `n` to cover additional length.
- **Greedy choice timing:** It waits until the current committed frontier so all eligible starts have been considered.
