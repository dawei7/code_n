## General
**Store the latest start for every target prefix**

Let `starts[j]` be the largest source index at which a subsequence matching `s2[0:j + 1]` can start among source characters processed so far. A larger valid start is preferable for a fixed ending position because it produces a shorter window. An unavailable prefix has start `-1`.

**Extend prefixes without reusing one source character**

Process `s1` from left to right. For each source character, scan target positions from $m - 1$ down to zero. If it matches `s2[j]`, set `starts[0]` to the current source index when $j = 0$; otherwise copy `starts[j - 1]` into `starts[j]` when that shorter prefix is available. Descending order is essential: it prevents the same source character from first updating one target prefix and then immediately extending that new state again.

**Evaluate every completed subsequence**

Whenever `starts[m - 1]` is available at source index `i`, the interval from that start through `i` contains the entire target in order. Because each prefix state keeps its latest possible start, this is the shortest qualifying window ending at `i`. Compare its length with the best window found so far.

**Why the global answer and tie rule follow**

Every possible right endpoint is processed. At each endpoint the dynamic state identifies its shortest valid start, so no longer window ending there can improve the answer. Taking the strict minimum over all endpoints yields the global shortest length. Equal-length windows encountered later necessarily start later, so updating only for a strictly shorter window preserves the leftmost minimum.

## Complexity detail
With `n = len(s1)` and `m = len(s2)`, each source character considers all `m` target positions, for $O(nm)$ time. The prefix-start array has `m` entries, for $O(m)$ auxiliary space.

## Alternatives and edge cases
- **Forward match then backward contraction:** scan forward until the target is matched, walk backward to make that endpoint's window minimal, and resume after its start; it uses $O(1)$ space and has the same $O(nm)$ worst-case bound.
- **Full dynamic-programming table:** retain the best start for every source and target prefix pair; it is direct but uses $O(nm)$ space when only the previous target-prefix states are needed.
- **Try every source start:** scan the remaining suffix for a full target match from each candidate start; it can take $O(n^2)$ time even when the target is short.
- **Frequency-based minimum window:** ordinary minimum-window-substring counts ignore character order and therefore do not enforce a subsequence.
- **No complete state:** return the empty string when the last target-prefix state never becomes available.
- **Repeated characters:** update target positions right-to-left so one source occurrence cannot satisfy multiple target positions.
- **Equal-length windows:** retain the first one to satisfy the leftmost requirement.
- **Target longer than source:** no complete state can form, so the answer is empty.
