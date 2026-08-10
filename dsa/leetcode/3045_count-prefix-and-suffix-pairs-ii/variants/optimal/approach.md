## General

**Encode prefix and suffix checks together.** For a word `s` of length $L$, consider the sequence

$$
(s[0],s[L-1]),\;
(s[1],s[L-2]),\;\ldots
$$

The source generates it with `zip(s, reversed(s))`. Each trie edge is labeled by one pair of characters: one read from the front and the corresponding one read from the back.

Suppose an earlier word `w` has length $\ell\le L$. Its paired sequence matches the first $\ell$ edges of `s`'s sequence exactly when:

- $w[d]=s[d]$ for all $0\le d<\ell$, so `w` is a prefix of `s`;
- $w[\ell-1-d]=s[L-1-d]$ for all those $d$, which after reindexing says `w` is a suffix of `s`.

Thus a single paired-character trie path enforces both conditions simultaneously.

**Process words from left to right.** Only pairs with $i<j$ count. The source inserts words in input order. While processing current word $j$, trie counters represent only earlier words, so every count added automatically satisfies the index condition.

**Interpret each node counter.** `node.cnt` counts how many earlier words end exactly at that trie node. It is incremented only after all paired characters of a word have been processed.

While walking the current word, after reaching depth $d$, the source adds that node's count to `ans`. Any earlier word ending there has length $d$ and a paired encoding equal to the current word's first $d$ paired edges, which is exactly the prefix-and-suffix property.

Counters at deeper nodes are not seen unless the current word is long enough, so a longer earlier word cannot incorrectly match a shorter current word.

**Create nodes only when necessary.** `children` is a dictionary keyed by a two-character tuple. Missing edges allocate a new `Node`. Shared paired prefixes reuse existing nodes, which is how many words are processed in total-length time.

**A trace with `"aba"` and `"ababa"`.** The paired sequence for `"aba"` is `('a','a'), ('b','b'), ('a','a')`. After insertion, its terminal node has count one.

For `"ababa"`, the sequence begins `('a','a'), ('b','b'), ('a','a')` as well. At depth three, the walk reaches that terminal node and adds one, correctly counting `"aba"` as both prefix and suffix.

**Duplicate words and self-overlap.** If the same word appeared several times earlier, its terminal count is greater than one, and all corresponding index pairs are added at once. A word may also have shorter border words; their counters occur at shallower nodes and are added during the same traversal.

The current word's counter is incremented only after its contributions are read, so it never pairs with itself. It becomes available for later indices.
Every added counter belongs to an earlier word whose entire paired path matches a prefix of the current path; the paired equality proves it is both prefix and suffix, so no invalid pair is counted. Conversely, every valid earlier word has exactly that matching paired path and a terminal counter at its length, which the current traversal reaches and adds. Therefore every valid index pair is counted exactly once.

## Complexity detail

Let

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

Each character position contributes one paired edge traversal, dictionary lookup, and constant counter work. Expected total time is $O(S)$.

At most one trie node is created per traversed position that introduces a new path, so there are $O(S)$ nodes and edges. Auxiliary space is $O(S)$. `reversed(s)` and `zip` are lazy iterators and do not copy strings.

Expected bounds rely on ordinary hash-dictionary performance. Recursion is not used, so very long words do not risk stack overflow.

## Alternatives and edge cases

- **Check every pair directly:** It can cost quadratic in word count times string length and is too slow for total length $5\cdot10^5$.
- **Two separate tries:** Intersecting prefix and suffix candidates requires additional bookkeeping; paired edges enforce both conditions in one traversal.
- **Rolling hashes of borders:** They can process lengths efficiently but introduce collision concerns unless verified.
- **Empty words:** They are outside the contract; every word contributes at least one edge.
- **Earlier word longer than current:** Its terminal node lies deeper than the current traversal and is never counted.
- **Equal words:** The entire paired path matches, so each earlier duplicate forms a valid pair.
- **Overlapping prefix and suffix:** Paired encoding naturally permits overlap.
- **Palindromic words:** Front and back characters often agree, but no special case is needed.
- **Short border plus long border:** Counters at both depths are added, representing different earlier indices or word lengths.
- **Index ordering:** Insertion after querying ensures only $i<j$ pairs count and prevents self-pairing.
- **Why depth equals earlier word length:** `zip(s,reversed(s))` yields exactly one pair per character, even after the front and back pointers cross. A terminal at depth $\ell$ therefore corresponds unambiguously to an earlier word of length $\ell$.
- **Counter rather than Boolean terminal:** Multiple identical earlier words occupy the same path. Storing their count lets one traversal add every distinct index pair instead of losing duplicates behind one terminal marker.
