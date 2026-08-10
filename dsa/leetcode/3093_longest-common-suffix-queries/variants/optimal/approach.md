## General

**A suffix becomes a prefix after reversal.** Comparing a query with every container word would repeat the same character checks many times. A trie shares common prefixes, but this problem asks about common suffixes. The exact source gets the same benefit by reading every word from right to left. Words ending in `"bcd"` then all follow the trie path `d -> c -> b`.

The implementation uses `w[::-1]` in each insertion and query loop. Conceptually, each trie depth represents one more character of a suffix:

- the root represents the empty suffix;
- a child at depth one represents a one-character suffix;
- a node at depth $d$ represents the exact suffix spelled by its root-to-node path in reverse-reading order.

**Each node stores the best container candidate for its suffix.** A trie path alone tells how many suffix characters match, but the answer also has two tie-breakers: prefer the shortest container word, then the earliest index. Every `Trie` node therefore stores:

- `length`: the length of the shortest inserted word passing through the node;
- `idx`: the index of that word in `wordsContainer`.

When a word is inserted, the source first considers the root and then every node reached while walking its reversed characters. The word passes through exactly the nodes for all of its suffixes, so it is a candidate at each of them.

The update condition is only `node.length > len(w)`. A strictly shorter word replaces the stored candidate. An equal-length word does not. Because container words are inserted in increasing index order, the first equal-length candidate is already the earliest one, so leaving it unchanged implements the second tie-break without an explicit index comparison.

**Why the root must also have an answer.** Two strings always share at least the empty suffix. If a query's final character does not appear as a root child, no nonempty suffix is common with any container word. The required fallback is then the globally shortest container word, with earliest-index tie-breaking. Updating the root during every insertion stores exactly this candidate.

**Fixed children make each step direct.** Every node owns a 26-element `children` list. For lowercase character `c`, the index is:

`ord(c) - ord("a")`.

If that child does not yet exist during insertion, the source creates a new `Trie` node. During query traversal, a missing child means the current suffix cannot be extended by the next character, so the loop stops immediately.

**Querying chooses the deepest reachable node.** For a query word, the source walks its characters in reverse. As long as the next child exists, one more suffix character is shared with at least one container word. At the first missing edge, no container word can match that longer suffix, because every inserted word with the already matched suffix is represented under the current node and none supplies the required child.

The last reached node therefore represents the longest common suffix attainable by the query. Its stored `idx` is the shortest container word among those sharing that suffix, and insertion order has preserved the earliest index among equally short words. Returning that one integer applies all three ranking levels in their required priority.

**A trace with the first example.** Insert `"abcd"`, `"bcd"`, and `"xbcd"`. All three share the reversed path `d -> c -> b`. At those nodes, `"bcd"` wins because length three is less than four. Query `"cd"` reaches `d -> c` and returns index 1. Query `"bcd"` reaches one level farther and still returns index 1. Query `"xyz"` cannot follow `z` from the root, so it returns the root's candidate, also index 1.

The second example shows why match length outranks container length. If one longer word reaches a deeper query path than all shorter words, traversal ends at that deeper node and returns its stored candidate. The root or shallower node's shorter candidate is irrelevant because it shares a shorter suffix.

**Why the structure is correct.** After all insertions, for every trie node, all and only the container words passing through that node share its represented suffix. The stored pair is the best word among that set under length and index order. A query's deepest reachable node represents its longest suffix occurring in at least one container word. Combining those two facts proves that `node.idx` at query termination is exactly the requested answer.

**Memory-oriented class design.** `__slots__ = ("children", "length", "idx")` prevents each node from receiving a normal per-instance attribute dictionary. A trie can contain hundreds of thousands of nodes, so this reduces overhead without changing the algorithm. The 26-child arrays still dominate actual memory.

## Complexity detail

Let:

$$
C=\sum_{w\in\texttt{wordsContainer}}\lvert w\rvert
$$

and:

$$
Q=\sum_{w\in\texttt{wordsQuery}}\lvert w\rvert.
$$

Each container character is processed once during insertion, and each query character is processed at most once before traversal ends. The time is $O(C+Q)$. Python slicing with `[::-1]` also takes linear time per word, but those costs sum to the same bounds.

At most one trie node is created per inserted character, plus the root, so the node count is $O(C)$. Each node stores 26 child references and two scalar fields. Since 26 is fixed, asymptotic auxiliary space is $O(C)$, though the constant factor is substantial. Reversed slices temporarily require space proportional to one current word; the maximum such length is already bounded by $C$ or $Q$ and does not exceed the overall stated storage.

The returned list uses $O(m)$ output space for $m=\lvert\texttt{wordsQuery}\rvert$.

## Alternatives and edge cases

- **Compare every query with every container word:** It is direct but can require $O(CQ)$-scale repeated suffix checks in unfavorable inputs.
- **Dictionary children:** Storing only existing edges can use much less memory for sparse tries, at the cost of hash lookups and dictionary overhead.
- **Sort reversed words:** Binary-searching prefix ranges is possible, but maintaining the shortest-and-earliest candidate for every query prefix is less direct.
- **No nonempty common suffix:** Traversal remains at the root and returns the globally shortest, earliest container word.
- **Query fully matched:** The deepest node reached after all query characters stores the best container word ending with the entire query.
- **Container word shorter than query:** It can still win if its whole text is the longest suffix any container supplies.
- **Equal container lengths:** Strict-length replacement preserves the first inserted, hence smallest index.
- **Duplicate container words:** They traverse identical paths; the earlier duplicate remains stored because lengths tie.
- **One-letter words:** They update both the root and one child, correctly serving empty- and one-character suffix queries.
- **All lowercase letters:** The `ord` offset and 26-child array depend on this contract.
- **Root initialization:** At least one container word is guaranteed, so the root's infinite placeholders are replaced before any query.
- **Match priority:** A deeper trie node always wins over a shallower one, even if the shallower node stores a shorter word.
- **Length priority within one node:** Only words sharing the same represented suffix compete by total word length.
- **Index priority within equal length:** Front-to-back insertion provides the tie-break implicitly.
- **Input mutation:** Container and query arrays are read only; reversed slices are temporary strings.
- **Large constant memory:** $O(C)$ hides 26 references per node. A map-based node may be preferable when memory limits are tight.
