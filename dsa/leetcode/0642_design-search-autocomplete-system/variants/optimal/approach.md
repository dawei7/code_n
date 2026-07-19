## General
**Store sentence frequencies once**

Keep a frequency map for complete sentences. Ranking compares `(-frequency, sentence)`, which places more frequent entries first and uses ordinary lexicographic order as the required tie-breaker.

**Cache three candidates at every trie node**

Insert each historical sentence character by character. Every visited prefix node stores only its three highest-ranked sentences. During initialization, and whenever one sentence's frequency increases, merge that sentence with the node's current cache, sort at most four candidates, and retain three.

**Follow the current prefix incrementally**

Maintain both the typed text and its current trie node. An ordinary character advances to one child and returns a copy of that child's cached list. If the prefix is absent, keep a null node and return an empty list until the sentence terminates.

**Learn completed input without rebuilding**

On `#`, increment the completed sentence's frequency and insert it along its trie path, creating missing nodes and refreshing only those prefix caches. Reset the typed text and active node to the root for the next sentence.

**Why the cached top three stay exact**

At initialization, repeated insertion considers every sentence for each of its prefixes, so each cache is exact. Later only one sentence's rank changes. Any unchanged sentence outside a cache still cannot outrank the unchanged cached members; considering the changed sentence together with the old top three is therefore sufficient to form the new top three. Induction preserves exact rankings after every submission.

## Complexity detail
Let `C` be the total initial sentence length and `Q` the number of streamed characters. Initialization visits $O(C)$ trie nodes. Ordinary input is $O(1)$ excluding the constant-size output; each submitted sentence is traversed once more, and total submitted length is at most `Q`, so the complete stream takes $O(C + Q)$ time. Trie nodes, cached references, and newly learned characters use $O(C + Q)$ space.

## Alternatives and edge cases
- **Scan all sentences per character:** filter the frequency map by prefix and sort matches; it is simple and correct but repeats corpus-wide work for every keystroke.
- **Trie nodes storing every matching sentence:** avoids corpus filtering but still sorts a potentially large candidate set on each query.
- **Heap per query:** selects the best three without fully sorting, but still examines every matching sentence unless rankings are cached.
- Equal frequencies use lexicographic sentence order, including spaces.
- Fewer than three matches return every available match without padding.
- A missing prefix returns an empty list until `#` resets the state.
- Completing an existing sentence increments rather than replaces its frequency.
- A newly learned sentence must affect future prefixes immediately after termination.
