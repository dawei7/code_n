## General

Treat every allowed word as a graph vertex. Two words share an edge when they differ in exactly one position. The problem asks for every shortest path from `beginWord` to `endWord`.

Enumerating arbitrary paths first would explore many long routes and cycles. The selected solution instead has two phases:

1. breadth-first search discovers minimum distances and stores every edge that can belong to a shortest path; and
2. depth-first backtracking follows those stored predecessor edges from the end word to the beginning.

**Why the end word must be in the dictionary**

Every sequence word after `beginWord`, including the final word, must belong to `wordList`. If `endWord` is absent from the set, no valid sequence exists and the method returns `[]` immediately.

`beginWord` is different: the contract explicitly says it need not be in the dictionary. `words.discard(beginWord)` removes it if present and safely does nothing otherwise. This prevents transformations from cycling back to the start.

**Generating graph neighbors without comparing every pair**

For current word `p`, the source converts it to mutable character list `s`. For each position, it tries every lowercase letter, joins the characters into candidate `t`, and later restores the original character.

Any generated candidate differs from `p` in at most one position. Trying the original letter produces `p` itself, but it is not in the remaining `words` set and does not create a forward edge.

Set membership filters generated strings to dictionary words. This avoids scanning all dictionary words and counting character differences for every current vertex.

**The BFS layer invariant**

`dist[beginWord] = 0`, and the queue initially contains only the beginning. At the start of each outer iteration, every queued word is at distance `step - 1`; after incrementing `step`, generated undiscovered neighbors belong at distance `step`.

The fixed `range(len(q), 0, -1)` processes exactly the current queue layer. Children appended during this loop wait for the next outer iteration.

This level boundary is essential. Once `endWord` is found, the algorithm must still finish every word in the current layer so it captures all other shortest predecessors of `endWord`.

**Why words are removed immediately yet multiple parents survive**

When a candidate `t` is still in `words`, this is its first discovery. The source:

- stores `p` in `prev[t]`;
- removes `t` from `words`;
- enqueues `t`; and
- records `dist[t] = step`.

Removing it immediately prevents duplicate queue entries and prevents later, deeper levels from creating non-shortest predecessor edges.

However, another parent in the same BFS layer may also transform to `t`. Because `t` is no longer in `words`, the normal discovery block would skip it. The earlier check `dist.get(t, 0) == step` detects that it was discovered at this exact depth and adds the additional parent to `prev[t]` before the set-membership `continue`.

Thus each word is enqueued once, but every predecessor at the minimum depth is retained.

**Why deeper and sideways edges are excluded**

If a candidate was discovered at an earlier distance, its recorded distance is less than `step`, so the same-depth predecessor check fails. It is also absent from `words`, so no edge is added.

Undiscovered words cannot be in the current layer because the queue owns that layer; their first discovery places them strictly one level below.

Every stored edge therefore goes from distance $d-1$ to distance $d$. Distances increase along forward edges, making the retained graph acyclic and ensuring every route through it has shortest-path layering.

**Stopping at the right time**

When `endWord` is first discovered, `found` becomes true. The inner loops continue processing the rest of the current BFS layer and all generated mutations, preserving every minimum-depth parent.

The next outer condition sees `found` and stops before expanding the end word's layer. Any later discovery would produce a longer sequence and must not be included.

**Backtracking from end to beginning**

`prev[word]` stores words one BFS level closer to `beginWord`. DFS starts with `path = [endWord]`.

For each predecessor, it appends the predecessor, recurses, and pops it afterward. When `cur == beginWord`, the working path is in reverse order, so `path[::-1]` creates one independent forward sequence and appends it to `ans`.

Predecessor sets may iterate in any order, which is acceptable because output sequence order is insignificant.

**Why all and only shortest sequences are returned**

Every stored predecessor edge changes one letter and connects adjacent BFS levels, so a backtracked route is valid and has the minimum discovered length.

During BFS, every dictionary neighbor reachable at the next depth is generated. First discovery records one parent, and the distance check records every other same-depth parent. Therefore every edge belonging to any shortest route is present.

DFS enumerates every combination of those predecessor choices that reaches `beginWord`. It cannot form a cycle because distance decreases at every recursive step. Hence every shortest sequence appears once as a sequence of predecessor choices, and no longer sequence appears.

**Tracing the `hit` to `cog` example**

The first layer discovers `hot`. The next layer discovers both `dot` and `lot`. From them, the following layer discovers `dog` and `log`.

Both `dog` and `log` generate `cog` at the same next `step`. The first removes and enqueues it; the second still passes the equal-distance check and becomes another predecessor.

Backtracking from `cog` follows `dog -> dot -> hot -> hit` and `log -> lot -> hot -> hit`, then reverses both working paths to return the two Reference sequences.

**Exact dependencies**

The source requires `List`, `defaultdict`, and `deque`, but imports none of them in the selected file. A standalone module needs the typing import plus `from collections import defaultdict, deque`.

The maximum dictionary size keeps recursive backtracking depth below about 501, within typical Python limits, while the number of output paths can still be large.

## Complexity detail

Let $W$ be the number of dictionary words, $L$ their common length, $E$ the number of stored predecessor edges, and $R$ the total number of word references across all returned sequences.

Each expanded word tries $26L$ mutations. In Python, slicing/list joining and hashing a length-$L$ candidate cost $O(L)$, giving $O(WL^2)$ worst-case neighbor-generation time. Backtracking and copying results costs $O(R)$. Total time is $O(WL^2+E+R)$, with edge insertions already bounded by generation work.

The word set, queue, and distance map use $O(W)$ references. `prev` uses $O(W+E)$ set/edge storage. The working path uses $O(W)$ in the loosest bound, and results use $O(R)$. Peak space including output is $O(W+E+R)$.

The manifest's $O(N+R)$ can be read only if $N$ denotes the full graph-building work and storage rather than merely the input word count. With explicit input parameters, candidate construction and potentially many predecessor edges must be acknowledged.

The constraint $L\le5$ makes alphabet mutation effectively small in practice, but it does not erase the reason for the detailed bound.

## Alternatives and edge cases

- **Bidirectional BFS plus DAG backtracking:** Expands the smaller frontier and may inspect far fewer words, but edge orientation must remain from begin to end.
- **Wildcard-pattern buckets:** Map patterns such as `h*t` to words and retrieve neighbors through shared buckets. It trades preprocessing memory for neighbor lookup.
- **Pairwise word comparison:** Check every dictionary pair for one-character difference. It is simple but can cost $O(W^2L)$.
- **Store complete paths in the BFS queue:** Easy to write but duplicates long prefixes and can consume enormous memory.
- **Remove words only after a whole level:** Naturally retains multiple parents but needs a per-level visited set. The selected distance check achieves the same goal with immediate removal.
- **Stop immediately on first `endWord`:** Incorrect because other parents in the same layer may lead to additional shortest sequences.
- **Missing end word:** Return `[]` before BFS.
- **Beginning absent from dictionary:** Fully supported.
- **One-letter words:** Mutation generation and layering work unchanged.
- **Duplicate dictionary words:** Excluded by contract; converting to a set would deduplicate them anyway.
- **Output order:** Predecessor sets make ordering nondeterministic, which the contract permits.
- **Path snapshots:** `path[::-1]` must create a new list before backtracking mutates `path`.
- **No longer paths:** Removing discovered words and stopping after the found layer prevent them.
- **Missing imports:** `List`, `defaultdict`, and `deque` must be supplied.
