## General

**Translate common prefixes into trie counts**

Insert every word into one trie. For each non-root node, store how many word indices pass through it and its depth. A node at depth $d$ represents one prefix of length $d$; that prefix can be selected from `k` distinct indices exactly when the node count is at least `k`.

Count, for every depth, how many trie nodes currently meet that threshold. Before any removal, a depth is globally valid when this count is positive. A `previous_valid` array records the greatest globally valid depth no larger than each index, so an invalid depth can be skipped in constant time.

**Only one kind of node can disappear**

Removing a word decreases counts only along that word's trie path. A path node can cross from valid to invalid only when its original count is exactly `k`. Even then, its depth disappears globally only if it was the sole valid node at that depth. Therefore a depth is disabled for removal index `i` precisely when the path for `words[i]` contains a node satisfying both conditions:

- its count is exactly `k`; and
- it is the only node with count at least `k` at its depth.

Mark such depths with the current word index. Starting from the deepest globally valid depth, follow `previous_valid` links while the candidate carries that mark. The first unmarked candidate is the answer; reaching depth zero means no positive-length prefix survives.

**Why no possible prefix is missed**

Any node off the removed word's path keeps its count. Any path node whose count exceeds `k` remains valid after losing one word. Finally, if a threshold node disappears but another valid node exists at the same depth, that other prefix still supplies a legal choice of `k` strings. These exhaust all cases, so exactly the marked depths—and no others—are unavailable for that removal.

The downward search cannot make the total work superlinear. Every skipped candidate is a marked depth on the current word's path, and each word path is already bounded by that word's length.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

Building and traversing the trie touches each input character a constant number of times. The trie has at most $S+1$ nodes, depth summaries use at most the maximum word length, and all downward candidate jumps across one word are bounded by that word's path length. The total expected time is $O(S)$ because child transitions use hash maps, and the auxiliary space is $O(S)$.

When removing one word leaves fewer than `k` strings, the method returns the all-zero result immediately.

## Alternatives and edge cases

- **Rebuild after every removal:** directly recomputing all prefix frequencies is simple but takes $O(nS)$ time in the worst case.
- **Segment tree over depths:** temporarily disabling fragile depths supports each update and restoration in $O(\log L)$ time, producing $O(S\log L)$ time where $L$ is the maximum word length; predecessor links remove that logarithmic factor.
- **Independent recomputation with sorted strings:** longest-common-prefix queries can use lexicographic adjacency, but maintaining the best group after every deletion is substantially more involved.
- **Exactly `k` word indices:** duplicate strings at different indices contribute separately to trie counts and remain valid separate choices.
- **`k = 1`:** the answer after a removal is the longest remaining word, which the same threshold logic handles.
- **Insufficient remainder:** if $n-1<k$, every answer is zero regardless of the strings.
- **Empty common prefix:** depth zero is the fallback when no positive-depth node retains a count of at least `k`.
