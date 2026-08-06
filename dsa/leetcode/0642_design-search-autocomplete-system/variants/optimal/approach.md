## General
**Store sentence frequencies once**

Keep a frequency map for complete sentences. Ranking compares `(-frequency, sentence)`, which places more frequent entries first and uses ordinary lexicographic order as the required tie-breaker.

**Cache three candidates at every trie node**

Insert each historical sentence character by character. Every visited prefix node stores only its three highest-ranked sentences. During initialization, and whenever one sentence's frequency increases, merge that sentence with the node's current cache, sort at most four candidates, and retain three.

**Follow the current prefix incrementally**

Maintain both a list of typed characters and the current trie node. An ordinary character appends to the buffer, advances to one child, and returns a copy of that child's cached list. If the prefix is absent, keep a null node and return an empty list until the sentence terminates.

**Learn completed input without rebuilding**

On `#`, join the buffered characters once, increment the completed sentence's frequency, and insert it along its trie path. Create missing nodes and refresh only the caches on that path, then clear the buffer and reset the active node to the root for the next sentence. Joining once avoids the repeated prefix copies caused by immutable-string concatenation on every keystroke.

**Why the cached top three stay exact**

At initialization, repeated insertion considers every sentence for each of its prefixes, so each cache is exact. Later only one sentence's rank changes. Any unchanged sentence outside a cache still cannot outrank the unchanged cached members; considering the changed sentence together with the old top three is therefore sufficient to form the new top three. Induction preserves exact rankings after every submission.

## Complexity detail
Let `C` be the total initial sentence length and `Q` the number of streamed characters. Initialization visits $O(C)$ trie nodes. An ordinary character takes amortized $O(1)$ time to append and follow one trie edge, excluding the constant-size output. Joining and reinserting each submitted sentence is linear in that sentence's length; across the stream, those lengths sum to at most $Q$. The complete run therefore takes $O(C + Q)$ time. Trie nodes, cached references, the character buffer, and newly learned characters use $O(C + Q)$ space.

## Alternatives and edge cases
- **Scan all sentences per character:** filter the frequency map by prefix and sort matches; it is simple and correct but repeats corpus-wide work for every keystroke.
- **Trie nodes storing every matching sentence:** avoids corpus filtering but still sorts a potentially large candidate set on each query.
- **Heap per query:** selects the best three without fully sorting, but still examines every matching sentence unless rankings are cached.
- **Immutable string prefix:** appending with `current += c` is concise, but it repeatedly copies the growing prefix and takes $O(L^2)$ work for a sentence of length $L$.
- Equal frequencies use lexicographic sentence order, including spaces.
- Fewer than three matches return every available match without padding.
- A missing prefix returns an empty list until `#` resets the state.
- Completing an existing sentence increments rather than replaces its frequency.
- A newly learned sentence must affect future prefixes immediately after termination.
