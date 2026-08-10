## General

**What the data structure must remember**

The class receives operations over time, so this is not a problem where one
answer is computed from one input and then discarded. Every call to `insert`
changes the state that later calls to `search` and `startsWith` observe. The
essential distinction is between a complete stored word and a path that merely
exists because it is the beginning of a longer word. After inserting `apple`,
the letters of `app` are present in the structure, which makes
`startsWith("app")` true, but `search("app")` must remain false until `app`
itself is inserted.

A trie represents that distinction naturally. Its root stands for the empty
prefix. Following one edge labelled with a character extends the represented
prefix by that character. Thus, along the route for `apple`, successive nodes
represent `a`, `ap`, `app`, `appl`, and `apple`. Words with a common beginning
share the same initial nodes. Inserting `application` after `apple`, for
example, reuses the nodes for `a`, `ap`, and `app`; only the remainder needs a
different route.

**One `Trie` object is also one trie node**

The exact optimal implementation does not define a separate `TrieNode` class.
Every instance of `Trie` is a node, and the object constructed by `Trie()` is
the root node. Each node owns two fields:

- `children` is a list of exactly 26 positions. Position 0 represents `a`,
  position 1 represents `b`, and so on through position 25 for `z`. A `None`
  entry means that no inserted word continues through that letter from this
  node. A non-`None` entry points to another `Trie` instance.
- `is_end` records whether at least one inserted word ends at this exact node.
  It says nothing about whether the node has children. A node can be both a
  word ending and the start of longer stored words.

The fixed array is justified by the contract that every word and prefix uses
only lowercase English letters. For a character `c`, the expression
`ord(c) - ord('a')` converts it into the required index from 0 through 25.
This conversion is constant time, and direct indexing avoids searching among
the outgoing edges.

**Inserting a word**

`insert` begins with `node = self`, so traversal starts at the root. For each
character `c` in the word, it computes the corresponding child index. If that
child position is empty, this is the first inserted word that needs this exact
prefix, so the method creates a new `Trie` object and stores it there. Whether
the child was newly created or already existed, traversal then moves to that
child. Reusing an existing child is what makes common prefixes share storage.

Only after all characters have been consumed does the method set
`node.is_end = True`. That timing is crucial. Setting the flag on intermediate
nodes would incorrectly turn every prefix into a complete word. Conversely,
failing to set it at the final node would make the path discoverable by
`startsWith` but invisible to exact `search`.

Consider inserting `apple` into an empty trie. The method creates five nodes,
one for each successive prefix, and marks only the `apple` node as an ending.
Inserting `app` afterward walks through three already-existing nodes and marks
the `app` node. It neither deletes the two later nodes nor creates duplicates.
Consequently, both words remain stored. Inserting `apple` again simply follows
the same path and assigns `True` to a flag that is already true, so duplicate
insertion is harmless and needs no special case.

**One shared traversal answers both kinds of query**

Both query operations first need to answer the same lower-level question:
does a path spelling this entire string exist from the root? The helper
`_search_prefix` performs exactly that work. It starts from `self`, translates
each character to its array index, and follows the matching child. If a needed
child is `None`, the requested path cannot be completed, so the helper returns
`None` immediately. If every character is matched, it returns the node reached
after the final character.

Returning a node instead of merely a boolean preserves the one extra fact
needed by exact search: whether the path endpoint is marked as a stored-word
ending. It also prevents `search` and `startsWith` from duplicating the same
character loop.

`startsWith(prefix)` only checks whether `_search_prefix(prefix)` returned a
node. Reaching that node proves that some inserted word created every edge in
the requested path. Nodes are created only while inserting words and are never
removed, so the path must be a prefix of at least one previously inserted
word. The endpoint does not have to be marked `is_end`; `app` is a valid prefix
of `apple` even before `app` is inserted separately.

`search(word)` imposes both requirements. The helper must find the entire
path, and the returned endpoint must have `is_end` set. A missing path clearly
means the word was never inserted. An existing but unmarked endpoint means the
characters occur only as a proper prefix of some longer inserted word. The
expression `node is not None and node.is_end` checks in that safe order:
Python's short-circuit evaluation does not attempt to access `is_end` when the
helper returned `None`.

**Why the representation stays valid after every operation**

Initially, the root has no children and is not an ending, which exactly
represents an empty set of nonempty words. During an insertion, each existing
edge already denotes the correct next character, while every new edge is
placed in the position belonging to the current character. Therefore the path
after processing the first $k$ characters represents exactly the length-$k$
prefix of the inserted word. Marking the last node records precisely that the
complete word now belongs to the set. No other ending flag is changed, so no
unrelated word is invented or lost.

The query helper follows those same character-indexed edges. It can return a
node exactly when the requested string labels a root-to-node path. The ending
test then separates complete words from prefix-only paths. These facts explain
why all three public methods remain consistent even when words overlap, one
word is a prefix of another, or an insertion is repeated.

## Complexity detail

Let $L$ be the length of the word or prefix supplied to one operation. Each
method examines its input characters from left to right once. Array-index
calculation, child lookup, child assignment, and flag inspection are all
constant-time operations, so `insert`, `search`, and `startsWith` each take
$O(L)$ time. An unsuccessful query can stop earlier, but $O(L)$ is the worst
case and the promised bound.

Let $T$ be the total number of character nodes created across all inserted
words, excluding the always-present root. The trie has $T+1$ nodes. Every node
stores 26 child references and one boolean; because 26 is a fixed alphabet
constant, total persistent storage is $O(T)$. A single insertion allocates at
most $L$ new nodes and allocates none for a path that already exists. Query
operations allocate no trie nodes and use $O(1)$ temporary space because the
traversal is iterative and keeps only the current node and index. The fixed
child arrays may consume more memory than sparse maps in practice, but they do
not change the asymptotic $O(T)$ bound for this fixed alphabet.

## Alternatives and edge cases

- **Hash-map children:** Store only existing outgoing edges in a dictionary. This can save memory for sparse nodes and support larger alphabets, but dictionary entries have more per-edge overhead and lookups rely on expected constant-time hashing; the exact solution instead exploits the guaranteed 26-letter alphabet with direct array access.
- **Hash set of complete words:** Exact `search` is expected $O(L)$, but answering `startsWith` by scanning stored words can be far more expensive. Storing every prefix in a second set restores fast prefix checks while duplicating substantial string data.
- **Sorted set or balanced search tree:** Lexicographic ordering can locate the first candidate near a prefix, but operations generally introduce an $O(\log W)$ factor for $W$ stored words and compare strings. The trie makes work depend directly on the queried length.
- **Compressed trie or radix tree:** Collapsing single-child chains into string-labelled edges can reduce node overhead. It adds substring comparison and edge-splitting logic, which is unnecessary for the required operations and fixed constraints.
- **A word that extends an existing word:** Inserting `apple` after `app` follows the existing `app` path, leaves its ending flag true, and creates only the missing `l` and `e` nodes. Both exact searches remain true.
- **A word that is an existing word's prefix:** Inserting `app` after `apple` creates no nodes; it marks the already-present `app` endpoint. This is precisely why path existence and `is_end` must be separate facts.
- **Absent character in the middle:** `_search_prefix` returns `None` as soon as a required child is missing. Later characters cannot repair a broken root-to-node path, so early termination is both safe and efficient.
- **Duplicate insertion:** The same path is reused and the final boolean remains true. The structure models membership rather than insertion frequency, which is exactly what the contract asks.
- **Maximum-length strings and many calls:** Iterative traversal avoids recursion depth problems even when a string has length 2000. Shared prefixes can greatly reduce created nodes, while completely different suffixes correctly receive separate branches.
- **Lowercase-only precondition:** The index formula is valid because the reference contract excludes uppercase letters, punctuation, and other characters. Supporting a broader alphabet would require validation or a different child representation; silently feeding such input to this implementation would violate its contract.
- **Empty strings:** Public inputs are guaranteed nonempty. Internally, `_search_prefix("")` would return the root, making `startsWith("")` true and `search("")` depend on the root's flag, but those behaviors are outside the required input domain and need no special branch.
