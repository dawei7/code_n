## General

**Each node represents one prefix**

A trie stores words by sharing their prefixes. The root represents the empty prefix. Following the child for `'a'` reaches the prefix `"a"`, then following `'p'` reaches `"ap"`, and so on.

Every node in the protected solution is another `Trie` object with three pieces of state:

- `children` is a fixed array of 26 child references, one for each lowercase letter;
- `v` counts how many stored word instances end exactly at this node;
- `pv` counts how many stored word instances pass through this node, meaning how many begin with the prefix represented by the node.

The two counters answer different questions. If the trie contains `"app"` and `"apple"`, the node for `"app"` has an exact-word count for `"app"`, while its prefix count includes both words.

**Map a character to one child slot**

For lowercase character `c`, `ord(c) - ord('a')` produces an index from 0 through 25. This gives constant-time access to the appropriate child without hashing at every node.

The lowercase-only input contract is essential: it guarantees every character maps inside the array.

**Insert one word instance**

Insertion starts at the root. For each character, it computes the child index and creates a new `Trie` node if that link is absent. It then moves into that child and increments the child's `pv`.

Incrementing after the move means the node for every nonempty prefix of the word gains one prefix instance. The root's `pv` is never changed. Empty prefixes are not queried under the constraints, so no root prefix count is needed.

After the final character, `node.v += 1` records one additional exact occurrence of the full word. Inserting the same word twice walks the same nodes and increments the same counters twice; duplicates are intentionally preserved.

**Use one traversal helper for both count operations**

`search(word)` follows the character path from the root. If a required child is missing, it returns `None` immediately. Otherwise, it returns the node representing the complete input string.

`countWordsEqualTo(word)` returns zero when search fails and otherwise returns `node.v`. A path may exist because of a longer word while `v` is zero; for example, storing only `"apple"` creates an `"app"` node but does not make `"app"` an exact stored word.

`countWordsStartingWith(prefix)` uses the same traversal but returns `node.pv`. Every inserted word beginning with that prefix incremented this counter on insertion, so no subtree scan is necessary.

**Erase exactly one existing instance**

The contract guarantees that every erased word exists. The method follows its path without missing-child checks. At every character node it decrements `pv` because one stored word no longer contributes to that prefix. At the terminal node it also decrements `v`.

Only one instance is removed. If `"apple"` was inserted twice, the first erase changes the exact and prefix counts from two to one; the second changes them to zero.

The implementation does not unlink nodes whose counters become zero. The old path remains allocated, but its counters make count queries return zero. A later insertion can reuse those nodes.

**Following the sample**

After inserting `"apple"` twice, every node on the path `a -> p -> p -> l -> e` has `pv = 2`, and the final `e` node has `v = 2`. The `"app"` node therefore reports two words starting with `"app"`, while the terminal node reports two exact `"apple"` instances.

Erasing once decrements every path prefix count and the terminal exact count to one. Erasing again makes them zero. The nodes still exist, but both required queries correctly report no stored instance.

**Why the counters remain correct**

Maintain two invariants:

1. a node's `v` equals the multiplicity of the exact word spelled by its root-to-node path;
2. a non-root node's `pv` equals the number of stored word instances whose paths include that node.

New nodes begin with zero counters. Insertion adds one to every included prefix and to the exact terminal. Valid erasure subtracts one from precisely the same counters. Count methods merely navigate to the relevant node and read the corresponding invariant. By induction over all operations, every returned count is exact.

## Complexity detail

Let $L$ be the length of the word or prefix supplied to an operation. `insert`, `erase`, `search`, and both count methods traverse one child per character, so each operation takes $O(L)$ time.

Let $S$ be the number of trie nodes ever created, at most one plus the total number of characters across inserted words before prefix sharing. Every node stores 26 references and two integers. Since 26 is fixed, total space is $O(S)$, matching the manifest.

Erasure does not reclaim nodes, so space depends on prefixes ever created rather than only currently stored words. The operation itself uses $O(1)$ auxiliary traversal state.

## Alternatives and edge cases

- **Dictionary children:** A hash map per node stores only present edges and may save sparse-node memory, but child lookup has hashing overhead.
- **Subtree counting on demand:** Traversing every descendant for a prefix query can be proportional to the entire stored dataset; `pv` makes the answer immediate after the path lookup.
- **Store a Boolean terminal flag:** It cannot represent duplicate word instances; integer `v` is required.
- **Physically prune on erase:** Nodes whose prefix count reaches zero can be unlinked, but the exact source deliberately retains them for simpler updates and possible reuse.
- **Insert duplicates:** Every occurrence increments both prefix and exact counts independently.
- **Word is a prefix of another:** Its node can have both a positive `v` and children leading to longer words.
- **Missing path:** `search` returns `None` and count methods return zero.
- **Existing path with zero exact count:** `countWordsEqualTo` returns zero even if longer words share the path.
- **Erasing one of several copies:** Counters decrease by one rather than resetting.
- **Guaranteed valid erase:** It permits traversal without defensive missing-child checks or negative-count protection.
- **Root prefix count:** It remains zero because empty prefixes are outside the input contract.
- **Maximum word length:** Iterative traversal avoids recursion-depth concerns for length 2000.
- **Lowercase alphabet:** It justifies fixed 26-way arrays and ordinal indexing.
- **Helper visibility:** `search` is an implementation helper; required public operations call it without changing trie state.
- **Object reuse:** Zero-count retained nodes can be populated again by later insertion.
