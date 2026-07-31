## General

**Encode both ends in one trie path.** For a word $w$ of length $k$, form the sequence

$$
(w_0,w_{k-1}), (w_1,w_{k-2}), \ldots, (w_{k-1},w_0).
$$

Use each character pair as one trie edge. Store at every terminal node how many previously processed words end at that exact depth and path.

**Why a terminal on the current path is a valid earlier word.** Suppose a previous word $u$ has length $k$ and the current word is $v$. The first $k$ paired edges of $v$ are

$$
(v_0,v_{\lvert v\rvert-1}),\ldots,(v_{k-1},v_{\lvert v\rvert-k}).
$$

They equal the complete paired path of $u$ exactly when $u_t=v_t$ and $u_{k-1-t}=v_{\lvert v\rvert-1-t}$ for every $t$. The first equality says that $u$ is a prefix of $v$; the second says that $u$ is a suffix of $v$.

**Preserve index order while counting.** Process `words` from left to right. As the current word descends through the trie, add the terminal count of every reached node. Each such terminal represents an earlier word that is both a prefix and a suffix of the current word. Only after all characters are processed should the current terminal count be incremented, so a word never pairs with itself or with a later index.

Every count added by the traversal corresponds to an earlier terminal whose paired path matches the current word at both ends, and therefore to a valid pair. Conversely, every valid earlier word has exactly that paired-path equality, so its terminal is reached and counted once. Thus the accumulated total contains every valid pair exactly once.

## Complexity detail

Let $S$ be the sum of all word lengths. Each character contributes one trie transition during the single left-to-right pass, so the running time is $O(S)$. At most one new trie node is created per processed character, giving $O(S)$ auxiliary space.

## Alternatives and edge cases

- **Compare every pair:** Direct `startswith` and `endswith` checks are simple but require $O(n^2L)$ time for maximum word length $L$, which is incompatible with the large aggregate input.
- **Rolling hashes:** Matching prefix and suffix hashes can identify borders, but collision-safe handling or double hashing is more delicate than the exact paired-character trie.
- **KMP border chains:** Prefix-function links can enumerate every border of each word and combine them with counts of previous whole words in $O(S)$ time, but the bookkeeping is less direct.
- **One word:** No earlier index exists, so the answer is `0`.
- **Equal words:** Every earlier equal occurrence forms a valid pair because a string is both its own prefix and suffix.
- **Overlapping prefix and suffix:** The two occurrences may overlap; equality of the paired characters handles this without requiring disjoint regions.
- **Earlier word longer:** Its terminal lies deeper than the current traversal and is never reached.
- **Prefix only or suffix only:** A mismatched component of a paired edge prevents the trie path from matching, so neither one-sided case is counted.
- **Large answer:** Up to $n(n-1)/2$ pairs may qualify, which exceeds 32-bit signed range at the maximum $n$; the result must use an adequately wide integer type.
