## General
**Process possible building blocks before longer words**

Sort words by length and maintain a set of words already processed. When checking a word, every available set member is no longer than it, and the current word itself has not yet been inserted. Therefore any successful segmentation automatically uses at least two strictly smaller pieces rather than matching the word as one piece.

**Run word-break dynamic programming**

For a word of length `L`, let `reachable[end]` mean its prefix ending before index `end` can be assembled from processed words. Start with `reachable[0] = True`. From each reachable start, test later substrings; finding one in the set marks its end reachable. The whole word is concatenated exactly when `reachable[L]` becomes true.

**Why sorting enforces the dictionary rule**

Every component of a concatenation is shorter than the complete word, so all valid components have already entered the set. Conversely, every DP transition uses an actual earlier dictionary word, and chaining at least two such transitions decodes to the complete word. Thus no candidate is missed and no non-dictionary fragment is admitted.

**Add every checked word for future candidates**

Whether or not a word is itself concatenated, it remains a valid dictionary component for longer words. Append successful words to the answer, then insert every nonempty checked word into the building-block set.

## Complexity detail
For a word of length `L`, at most $O(L^2)$ substrings are tested, yielding $O(\sum_w |w|^2)$ time with hash-set lookup and substring costs under the usual model. The dictionary strings, result, and one $O(L)$ DP array use $O(\sum_w |w|)$ space.

## Alternatives and edge cases
- **Trie-guided DP:** walks dictionary prefixes without allocating each tested substring and can improve constant factors.
- **Memoized DFS:** recursively tries component endings and caches failed suffix positions with comparable polynomial work.
- **Unmemoized DFS:** recomputes the same suffix after many decompositions and can be exponential.
- **Remove and restore the current word:** permits arbitrary input order but requires explicit protection against using the whole word once.
- **Empty string:** skip it as a building block because it cannot advance a segmentation.
- **More than two pieces:** the same reachability chain handles any number of components.
- **Output order:** alternative valid algorithms may return the same set in another order.
