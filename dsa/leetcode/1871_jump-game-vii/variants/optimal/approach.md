## General

**Define reachability for every index.** `f[i]` is true exactly when index `i` can be reached from index zero using valid jumps and landing only on zero characters. The starting state is `f[0] = True`, guaranteed valid by `s[0] = "0"`.

For destination `i`, a previous index `j` can jump there when:

`i - maxJump <= j <= i - minJump`.

After clipping below zero, the valid predecessor interval is

`l = max(0, i - maxJump)` through `r = i - minJump`.

If `s[i]` is one, landing is forbidden and `f[i]` remains false. If it is zero, `f[i]` is true when at least one reachable predecessor lies in that interval.

**Why checking every predecessor directly is too slow.** A wide jump range could contain `O(n)` indices for each destination, causing `O(n^2)` work. The solution stores prefix sums of Boolean reachability so it can ask whether an entire interval contains any true value in constant time.

**Meaning of the prefix array.** `pre` has length `n + 1` and follows the exclusive-prefix convention:

`pre[t] = number of reachable indices from 0 through t - 1`.

Since index zero is reachable, `pre[1] = 1`. For later indices, `pre[i + 1] = pre[i] + f[i]`. Python adds Boolean values as zero or one.

The number of reachable predecessors in inclusive interval `[l, r]` is:

`pre[r + 1] - pre[l]`.

It is positive exactly when at least one valid jump source exists.

**Handle an interval that has not begun.** For early `i`, `r = i - minJump` may be negative. The condition `l <= r` rejects such an empty interval before relying on its prefix sum. Python’s short-circuit `and` prevents the subtraction from being used as a reachability claim when no predecessor index is valid.

**Process left to right.** Every predecessor of `i` is smaller than `i` because jumps are positive. Thus all relevant `f[j]` and prefix values are finalized before `f[i]` is computed.

**Trace `s = "011010"` with jumps two through three.** Index one has no valid predecessor and is also blocked. Index two is blocked. At index three, predecessor range zero through one contains reachable index zero and `s[3]` is zero, so it becomes reachable. At index five, predecessor range two through three contains reachable index three and the final character is zero, so the destination becomes reachable.

**Blocked positions remain counted correctly.** When `s[i] == "1"`, the code skips the reachability assignment, leaving `f[i]` false. The prefix update adds zero, so blocked positions never become jump sources.

**Exclusive prefix indexing avoids off-by-one ambiguity.** `pre[l]` excludes index `l`, while `pre[r + 1]` includes everything through index `r`. Their difference therefore includes both jump-range endpoints exactly once. For a one-position predecessor range with `l = r`, the difference reduces to one Boolean state, as it should.

The array has one extra slot so even a query ending at index `n - 1` can use prefix position `n` safely. That extra sentinel-style slot stores a cumulative count, not a reachability state of a nonexistent character.
Assume `f` is correct for every index before `i`. If `s[i]` is one, false is required. Otherwise, the jump rule says `i` is reachable exactly when some reachable earlier index lies in `[l, r]`. The prefix difference is positive exactly under that condition, so the computed `f[i]` is correct. Starting from the valid base index zero, induction covers the string. Returning `f[-1]` therefore answers whether the last index is reachable.

## Complexity detail

The loop visits each of `n` indices once. Every state uses constant arithmetic and prefix lookups, so total time is `O(n)`.

Arrays `f` and `pre` use `O(n)` space. A sliding count of reachable predecessors could reduce storage, but the exact source retains both arrays.

## Alternatives and edge cases

- **Breadth-first search:** Enqueue reachable indices and expand jump ranges, but naive repeated range scanning can become quadratic without a frontier optimization.
- **Sliding reachable-count window:** Maintain the number of true predecessors currently within jump distance to achieve `O(n)` time with less state.
- **Direct dynamic programming scan:** Testing every predecessor interval explicitly costs `O(n^2)` in the worst case.
- **Last character one:** It is never reachable, so the method returns false.
- **Earliest reachable destination:** No positive index below `minJump` can have a valid predecessor.
- **Exact boundary jumps:** Both `minJump` and `maxJump` endpoints are included by the interval formula.
- **Clipping below zero:** `max(0, ...)` prevents negative predecessor indices.
- **Empty predecessor interval:** `l <= r` must hold before any destination can become reachable.
- **Blocked source candidates:** Their `f` values are false and contribute zero to prefix counts.
- **Starting index:** `f[0]` and `pre[1]` encode the guaranteed reachable zero.
- **Boolean arithmetic:** Adding `f[i]` to `pre` treats true as one and false as zero.
- **Output state:** Only reachability of the final index matters, but intermediate states are necessary to support later jumps.
- **Single predecessor interval:** When `l = r`, one reachable source is enough and the prefix difference tests exactly that source.
- **Multiple reachable predecessors:** The transition needs only a positive count, not their identities or the path used to reach them.
- **Unreachable zero character:** A zero landing cell can still remain false when its predecessor interval contains no reachable state.
- **Extra prefix slot:** `pre` has length `n + 1` so exclusive endpoints never require a special final-index branch.
