## General

**A trie node represents one candidate common prefix.** Every node below the root corresponds to the characters along its root-to-node path. `counts[node]` records how many input words pass through that node, so the represented prefix is shared by at least $k$ strings exactly when

`counts[node] >= k`.

The source first handles the unavoidable size case. If removing one word leaves fewer than $k$ words, no selection of $k$ distinct indices exists, so every answer is zero.

Otherwise, it builds one trie for all words. While inserting a word, it creates missing child nodes, stores each node's depth, and increments the count at every prefix node visited. The root count is unused because an empty prefix is represented by answer length zero.

**Summarize which prefix lengths are globally possible.** `valid_at_depth[d]` counts trie nodes at depth $d$ whose counts are at least $k$. If this number is positive, some $k$ original words share a prefix of length $d$.

`previous_valid[d]` stores the deepest valid depth no greater than $d$. The scan maintains `latest`, updating it whenever `valid_at_depth[d] > 0`. Thus it supports a fast jump from an invalidated depth to the next lower depth that was globally valid before removal.

`deepest = previous_valid[maximum_depth]` is the longest common-prefix length attainable by any $k$ words before removing anything.

**Understand exactly when one removal invalidates a trie node.** Removing word $w$ decrements counts only along $w$'s trie path. A node not on that path is unchanged. A path node with old count greater than $k$ remains at least $k$. Therefore, a node becomes invalid if and only if:

- $w$ passes through it; and
- its old count is exactly $k$.

Even if that one node becomes invalid, depth $d$ may still remain usable through another valid trie node at the same depth. The entire depth disappears only when `valid_at_depth[d] == 1`.

The condition

`counts[node] == k and valid_at_depth[depth] == 1`

therefore identifies a depth uniquely disabled by removing the current word.

**Record disabled depths without rebuilding counts per removal.** Array `disabled_by` stores a word index. As the source walks one word's trie path, it assigns `disabled_by[depth] = word_index` for every uniquely vulnerable depth on that path.

The array is not cleared between words, which is safe. If a depth has one unique valid node of count exactly $k$, exactly those $k$ words passing through it can disable it. When processing one of them, the entry is overwritten with that current index immediately before its answer is computed. A word outside that node's path does not overwrite it, but the stored index belongs to some other word, so comparison with the current index is false. The marker is therefore accurate for the word being answered without per-word cleanup.

**Jump down only through globally valid depths.** Start each answer at `deepest`. If `disabled_by[candidate] == word_index`, that depth vanished after this removal. The assignment

`candidate = previous_valid[candidate - 1]`

jumps directly to the greatest lower depth that had any valid prefix before removal. That depth may also be uniquely disabled by the same word, so the while loop repeats. The first candidate not marked for this word still has at least one node with count at least $k$ after removal and is the answer.

For the example with three copies of `run` and two copies of `jump` at $k=2$, the depth-four node for `jump` has count exactly two and is the only valid node at depth four. Removing either `jump` disables depth four, so the algorithm falls back to depth three, where `run` remains valid. Removing a `run` leaves the two `jump` words intact, so depth four remains the answer.

**Why the method finds the optimum for every removal.** Trie count semantics establish a one-to-one correspondence between valid nodes and prefixes shared by at least $k$ remaining strings. The vulnerability test identifies exactly which globally valid depths lose their last qualifying node when a particular word is removed. All other valid depths remain achievable. Starting from the global maximum and jumping down through only the depths disabled by that word therefore returns the greatest achievable length after its removal.

There is no need to know which $k$ strings are selected. A node count proves that enough distinct word indices share its prefix.

**Why the total per-word work remains linear in all characters.** Each word path is traversed once to set vulnerability markers. Its fallback loop can skip only depths marked with that same word index, and those marks were created on its path, plus one final nonmarked check. Thus the total number of fallback iterations across words is bounded by the total input character count rather than $n$ times the maximum depth.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

Trie construction visits every character once and creates at most $S$ nonroot nodes. Scanning nodes to build `valid_at_depth` costs $O(S)$. The depth summary costs at most the maximum word length, which is no more than $S$. Walking every word path again costs $O(S)$, and the amortized fallback iterations are also $O(S)$. Total time is $O(S)$.

Trie child dictionaries, counts, depths, and all depth arrays use $O(S)$ space. The output uses $O(n)$, which is within $O(S)$ because every word has at least one character. These bounds match the manifest.

## Alternatives and edge cases

- **Rebuild a trie after each removal:** This repeats $O(S)$ work for every word and can become quadratic.
- **Temporarily decrement path counts per word:** It can work, but repeatedly searching the deepest valid node needs an additional global structure; vulnerability preprocessing avoids mutations.
- **Track only the deepest node:** Removing one word may invalidate it while another node at the same depth remains valid, so counts per depth are essential.
- **Node count greater than \(k\):** Removing one passing word leaves at least $k$, so the node is never disabled.
- **Several valid nodes at one depth:** Losing one does not eliminate that prefix length.
- **Exactly one valid node with count \(k\):** Every word through it uniquely disables that depth.
- **Removed word outside the unique node:** Its removal does not affect that node, and the stale marker contains a different word index.
- **Fewer than \(k\) remaining words:** The early return produces all zeros before building the trie.
- **No positive common prefix:** `deepest` is zero, and the fallback loop is skipped.
- **Duplicate words:** Each distinct array index increments counts independently, which is exactly what selection by distinct indices requires.
- **Very long single word:** Depth arrays scale with its length, still within total character count $S$.
- **No per-word cleanup:** Immediate overwrite and index comparison make `disabled_by` safely reusable.
