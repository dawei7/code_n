## General

The competitive source uses bidirectional breadth-first search. One frontier starts at `beginWord`, another at `endWord`, and the method repeatedly expands the smaller frontier until the two searches touch.

It needs only the shortest sequence length, so it stores frontier sets rather than parent edges or complete paths.

**Required end-word membership**

`words = set(wordList)` holds dictionary vertices that have not been removed. If `endWord` is absent, the method immediately returns zero because every sequence word after the beginning must belong to the dictionary.

The ending frontier is safe to seed only after this check. `beginWord` need not be in the dictionary and is seeded independently.

**What the two frontiers represent**

`left` is the frontier selected for the next expansion. `right` is the current frontier reached from the opposite endpoint.

The variable names are operational, not permanently directional. After an expansion, the sets may be swapped so `left` is always the smaller one. The algorithm does not reconstruct a directed path, so no direction flag is needed.

Each frontier contains words at one fixed distance from its endpoint. The total number of expanded layers from both sides determines `ladder`.

**Why `ladder` starts at two**

Before any expansion, the shortest possible valid transformation under `beginWord != endWord` would contain two words: the two endpoints connected by one change.

During the first expansion, if a generated neighbor belongs to the opposite frontier, the source returns two. Every completed expansion that does not meet adds one more word to the possible combined sequence, so `ladder` is incremented once.

It does not matter which side is expanded: moving either frontier outward by one edge increases the eventual combined path length by one word.

**Removing an expanded frontier**

`words -= left` marks all current frontier words visited before generating neighbors.

This prevents a mutation from returning to the same or an older layer and prevents repeated expansions. It also removes `beginWord` if the dictionary happened to contain it.

The opposite `right` frontier remains in `words`, which is important because generated candidates must pass `new_word in words` before the source tests `new_word in right`.

**Generating the next frontier**

For each word, a generator substitutes every lowercase letter at every position. Slicing and concatenation produce candidate `new_word`.

Candidates outside the remaining dictionary are skipped. If a candidate belongs to `right`, the searches have met and the current `ladder` is returned.

Otherwise the candidate enters `new_left`, a set. The set deduplicates a word reachable from multiple parents; only its distance matters.

Trying the original character creates the current word, but current frontier words were removed from `words`, so no self-loop survives.

**Why expanding the smaller frontier helps**

With branching factor $b$, expanding $d$ levels from one end can inspect on the order of $b^d$ states. Reaching toward the middle from both sides can reduce practical search toward roughly $b^{d/2}$ from each side.

The code swaps when the newly formed `left` is larger than `right`. Every expansion is still a complete BFS layer, so shortest-path ordering is preserved.

This is a performance optimization, not a change in correctness. Expanding either side would eventually find the same minimum combined distance.

**Why the first frontier meeting is shortest**

Both sides advance one entire BFS layer at a time. Before a meeting, all paths using fewer combined expansions have already been ruled out.

A generated candidate in `right` connects the current expanded depth to the exact opposite frontier depth. Any undiscovered connection would require at least as many total edges.

Therefore the first meeting yields the minimum sequence length, and no path reconstruction or further layer processing is required.

**Tracing the main example**

The beginning side first discovers `hot`. Depending on frontier sizes, the algorithm may then expand from `cog` and discover `dog` and `log`.

Further smaller-side expansions eventually generate a word present in the opposite frontier, such as connecting `dot` with `dog` or `lot` with `log`.

The accumulated `ladder` is five, counting `hit`, three intermediate positions along a shortest route, and `cog`.

**No-route behavior**

If the expanded side produces no unseen dictionary neighbors, `left` becomes empty. The loop terminates and returns zero.

The opposite frontier need not be explicitly checked in the loop condition because an empty expanding frontier already proves the searches cannot connect through unseen words.

**Active source**

The file also contains `Solution2`, a one-direction BFS. The selected first `Solution` uses frontier sets and imports `ascii_lowercase` correctly.

It stores no parents, so it cannot return actual sequences; that matches the length-only contract.

## Complexity detail

Let $W$ be dictionary size and $L$ word length. In the worst case, the two searches collectively expand $O(W)$ distinct words. Each tries $26L$ candidates, and Python slicing, concatenation, and hashing cost $O(L)$ per candidate. Worst-case time is $O(WL^2)$.

Bidirectional search often explores far fewer words in practice, reflected by the source header's branch-factor estimate $O(b^{d/2})$, but worst-case input asymptotics remain bounded by all reachable dictionary words.

`words`, `left`, `right`, and `new_left` together store $O(W)$ string references. Generated candidates use $O(L)$ transient space. Counting referenced string contents gives the coarser $O(WL)$ view; additional container slots are $O(W)$.

The manifest's $O(N)$ bounds treat word length and alphabet size as constants. The explicit form is more informative for Python string construction.

## Alternatives and edge cases

- **One-direction BFS:** Simpler and still shortest, but may expand a much larger frontier before reaching the end.
- **Wildcard pattern preprocessing:** Build mappings from erased-character patterns to words, then use them for both frontier searches.
- **Direct dictionary comparisons:** Avoids generated strings but can require $O(W^2L)$ work.
- **Parent DAG reconstruction:** Necessary for returning all paths, but wasteful when only length is requested.
- **End absent from dictionary:** Immediate zero.
- **Direct adjacency:** First expansion returns two.
- **Disconnected dictionary:** The expanding frontier eventually empties.
- **Begin in dictionary:** Removed with the first expanded frontier.
- **Multiple parents:** Frontier sets deduplicate them because only distance matters.
- **Swap direction:** Safe because the graph is undirected and only total length is needed.
- **Do not remove `right`:** Its members must remain detectable as meeting candidates.
- **Same-character substitutions:** Filtered because the current frontier was removed.
- **Unique word list:** Set conversion retains all vertices.
- **Output count:** `ladder` counts both endpoints, not just changes.
- **Active versus alternative:** `Solution2` does not affect the bidirectional method's space or behavior.
