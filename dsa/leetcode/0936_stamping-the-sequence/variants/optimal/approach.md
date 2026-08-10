## General

**Why solving the process backward is easier**

In the forward direction, every stamp overwrites all `m` positions beneath it. A character written by an early move may later be replaced, so choosing the next stamp is hard to judge locally.

The final target gives much more information. Imagine undoing stamps from `target` back to a string of question marks. A reverse stamp at start `i` erases the whole window `target[i:i + m]`. It is currently legal when every still-visible character in that window agrees with the corresponding character of `stamp`. Positions already erased to `?` impose no restriction because, in the forward direction, an earlier stamp may write anything there before a later stamp overwrites it.

The algorithm implements this reverse process without repeatedly rebuilding strings.

**A dependency count for every possible window**

There are `n - m + 1` legal stamp starts. For each start `i`, the code initially sets `indeg[i] = m` and compares all `m` stamp characters with the aligned target characters.

Whenever `target[i + j] == stamp[j]`, that position already agrees, so the code decrements `indeg[i]`. After the comparison finishes, `indeg[i]` equals the number of mismatching positions in window `i`.

A window with `indeg[i] == 0` matches the stamp exactly and can be erased immediately in the backward process, so its start is placed in queue `q`.

The name `indeg` reflects that mismatches behave like unresolved prerequisites. It is not the ordinary indegree of a graph vertex formed directly from stamp windows. A window becomes available once all of its mismatching positions have previously been erased.

**The reverse dependency graph**

For each target position `p`, `g[p]` stores every window that currently mismatches the stamp at `p`. The initialization adds start `i` to `g[i + j]` precisely when `target[i + j] != stamp[j]`.

Why record only mismatches? A matching position never blocks that window, even while visible. A mismatching position blocks it until some already-available reverse stamp erases it. When position `p` becomes erased, every window listed in `g[p]` loses one unresolved mismatch, so its `indeg` decreases by one.

This graph lets the algorithm notify only the windows affected by a newly erased position. It avoids rescanning all windows after every reverse stamp.

**Processing an available reverse stamp**

When start `i` is removed from the queue, the algorithm appends `i` to `ans`. At this moment all its original mismatches have been erased, so every remaining visible character in its length-`m` window matches `stamp`. The reverse stamp is legal.

The loop then visits each covered target position `i + j`. If `vis[i + j]` is false, this is the first time that position becomes erased. The code:

1. marks it visited;
2. looks at every dependent window `k` in `g[i + j]`;
3. decrements `indeg[k]`;
4. enqueues `k` if that count has just reached zero.

The `vis` check is essential because overlapping reverse stamps may cover the same position. An erased character should satisfy each dependency only once. Without the check, the same position could decrement counts repeatedly and make a still-blocked window appear available.

A window is enqueued only when its nonnegative count first reaches zero. Later erasures cannot make it reach zero again, so every window is processed at most once.

**Why every target position must be erased**

After the queue is exhausted, `all(vis)` asks whether the reverse process erased every target character. If any position remains visible, no processed window covered it, and the chain of legal reverse stamps could not reduce the target to all question marks. The algorithm returns an empty list.

If every position is visited, the recorded reverse stamps form a valid erasure sequence. Their number is at most the number of windows, `n - m + 1`, because no window is processed twice. This is at most `n` and therefore safely within the allowed `10 * n` forward moves.

**Why the answer must be reversed**

The entries were recorded in undo order. Suppose reverse window `a` is erased first and reverse window `b` becomes possible afterward. In the actual construction, `b` must be stamped first and `a` later, so `a` can overwrite the appropriate characters and produce the final target.

Returning `ans[::-1]` converts the valid reverse chronology into forward stamping chronology.

To see the logic on overlapping windows, consider `stamp = "abc"` and `target = "ababc"`. Window zero is initially blocked by its last aligned character, whereas window two exactly matches and is available. Reverse-erasing window two turns the suffix into wildcards, which removes window zero's blocker. The reverse order is `[2, 0]`, so the forward order is `[0, 2]`.

**Why the algorithm is correct**

Every queued window is a legal reverse move: its initial matching positions agree already, and each initial mismatch has triggered a decrement only after that position was erased. Erasing the full window is therefore consistent with some forward overwrite.

Whenever a reverse move erases a position, the graph updates all and only windows blocked by that position. Thus any window whose blockers all disappear eventually reaches zero and enters the queue. The search does not overlook an available move.

If all positions are erased, reversing the legal undo sequence produces a forward sequence from all question marks to `target`. Later forward stamps correspond to earlier reverse erasures and restore any characters overwritten by earlier forward moves. Conversely, if the algorithm stops with visible positions, there is no available window among the dependencies reachable from an exact match, so its constructed reverse process cannot cover the target. The required output for this algorithm is then empty.

## Complexity detail

Let `m` be the stamp length and `n` the target length.

Initialization examines every character of each of the `n - m + 1` windows, costing `O(nm)` time. The graph stores at most one mismatch edge for each window-position comparison, so it has `O(nm)` edges.

Every window enters the queue at most once. Processing it scans `m` covered positions, totaling `O(nm)` across all windows. Each graph edge is followed once, when its target position is first marked visited. The complete time complexity is therefore `O(nm)`.

The graph `g` can store `O(nm)` window references. The dependency array, visited array, queue, and answer use `O(n)` additional space. The total auxiliary space complexity is `O(nm)`.

## Alternatives and edge cases

- **Repeatedly scan every window:** Find any currently erasable window, erase it, and restart scanning. This is easier to derive but may revisit the same comparisons many times, producing a substantially slower worst case.
- **Store sets of matching and mismatching positions:** A direct backward simulation can maintain a todo set per window. It expresses the concept clearly, but hash-set overhead is larger than the integer counts and reverse adjacency lists used here.
- **Forward greedy stamping:** A locally matching placement can overwrite characters needed later, and question marks provide no final-character guidance at the beginning. Backward erasure exposes dependencies much more cleanly.
- **Stamp equals target:** The only window has dependency count zero, is processed, marks every position, and returns start `0`.
- **No initially matching window:** The queue begins empty. No character can be erased, so `all(vis)` is false and the method correctly returns an empty list.
- **Overlapping windows:** Overlap is the mechanism that unlocks initially mismatching windows. `vis` prevents one erased position from satisfying the same dependencies more than once.
- **Matching characters inside a later window:** Such positions are not placed in `g` because they never block the window. They are still marked visited when that window itself is processed.
- **Stamp length one:** Each matching target position creates its own zero-dependency window. All positions must equal the one stamp character for the full target to be covered.
- **Target length equals stamp length:** There is one possible window. It succeeds only when it matches exactly; no overlapping move exists to erase a mismatch first.
- **Multiple valid answers:** Queue order selects one valid dependency order. The problem permits any sequence within the move limit, so uniqueness is unnecessary.
- **Move limit:** The answer contains at most one occurrence of each legal window start, hence no more than `n` moves, which is stronger than the allowed `10 * n`.
